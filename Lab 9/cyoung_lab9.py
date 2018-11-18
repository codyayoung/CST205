# Cody Young
# Lab 9 
# SCSI Logic
# 2018-11-20

# Main
# Used for testing purposes
def main():
  test = getSound()
  explore(test)
  #testclip = clip(test, 50000, 100000)
  #explore(testclip)
  #reversed = reverse(test)
  #explore(reversed)
  
# Problem 1
# Copies a sample between the start and stop index of a source sound into a new clip.
def clip(source, start, end):
  #Get length of clip (number of samples and source sampling rate, make empty sound for clip
  clip_length = end - start
  clip = makeEmptySound(clip_length, int(getSamplingRate(source)))
  
  #Set target index value for copying
  target_index = 0

  #Copy samples from start to end index in source to target clip, starting at index 0 in target
  for i in range(start, end):
    value = getSampleValueAt(source, i)
    setSampleValueAt(clip, target_index, value)
    target_index = target_index + 1
    
  return clip

# Problem 2
# Splices a clip into a longer clip.
def copy(source,target,start):
  #Get source length
  source_length = getLength(source)
  #Set initial target index value for copying
  target_index = start
  
  #Splicing function
  for i in range(0, source_length):
    value = getSampleValueAt(source, i)
    setSampleValueAt(target, target_index, value)
    target_index += 1
    
# Problem 3
# Makes a sound collage from several clips. I used clips from four games and a movie.
def soundCollage():
  #Get five audio sources, make five clips, get sampling rate and total length
  source1 = getSound()
  source2 = getSound()
  source3 = getSound()
  source4 = getSound()
  source5 = getSound()
  
  metalgearalert = clip(source1, 0, 42742)
  persona = clip(source2, 28366, 698271)
  kungfu = clip(source3, 921300, 1770450)
  sf_win = clip(source4, 0, 93186)
  ff_victory = clip(source5, 20026, 374344)
  
  #Clip lengths
  mg_len = getLength(metalgearalert)
  p_len = getLength(persona)
  kf_len = getLength(kungfu)
  sfwin_len = getLength(sf_win)
  ffv_len = getLength(ff_victory)
  
  #Sampling rate
  sample_rate = int(getSamplingRate(source2))
  #Silence buffer and number of samples needed for a (second * factor) of silence
  silence_buf = 100000
  silence_duration = int(0.1 * getSamplingRate(source2))
  
  #Total length of all five clips
  total_length = mg_len + p_len + kf_len + sfwin_len + ffv_len + silence_buf
  
  #Create empty target sound for "compilation", and copy five audio clips 
  collage = makeEmptySound(total_length, sample_rate)
  copy(metalgearalert, collage, 0)
  copy(persona, collage, mg_len)
  copy(kungfu, collage, mg_len + p_len)
  copy(sf_win, collage, mg_len + p_len + kf_len)
  copy(ff_victory, collage, mg_len + p_len + kf_len + sfwin_len)
  
  #Note: change to working directory on current machine 
  #dir = "C:\Users\Cody\Documents\CSUMB\CST 205\CST 205 - Sound\Lab 9\output/fightcollage.wav"
  #writeSoundTo(collage, dir)
  explore(collage)
  return collage
 
# Problem 4
# Reverses an input sound.
def reverse(sound):
  #Get source length, create empty target sound and get length 
   source_length = getLength(sound)
   reversed = makeEmptySound(source_length, int(getSamplingRate(sound)))
   target_length = getLength(reversed)
   print("Source length: %d" % source_length)
   print("Target length: %d" % target_length)
   
   #Assign as source index for clarity 
   source_index = source_length
   
   #Reverse sound by copying end to start
   for i in range(0, target_length):
     value = getSampleValueAt(sound, source_index - 1)
     setSampleValueAt(reversed, i, value)
     source_index -= 1

   return reversed      
  
# ----------------
# Helper Functions
# ----------------
# Changes volume of a sound by a multiplying factor. 
def changeVolume(sound,factor):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * factor)
    
  return sound

# Returns sound from file.
def getSound():
  return makeSound(pickAFile()) 	