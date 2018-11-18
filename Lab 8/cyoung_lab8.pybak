# Cody Young
# Sara Kazemi
# Lab 8 
# SCSI Logic
# 2018-11-20

# Used for testing stuff.
def main():
  test = getSound()
  #changeVolume(test, 0.25)
  #maxSample(test)
  #maxVolume(test)
  #increaseVolume(test)
  #decreaseVolume(test)
  #goToEleven(test)
  
  explore(test)
 
# Increases volume of a sound.
def increaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * 2)
  
  return sound
	
# Decreases volume of a sound.	
def decreaseVolume(sound):	
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * 0.25)
  
  return sound

# Changes volume of a sound by a multiplying factor.
# For example, a factor value of 2.00 multiplies all sample values by 2.
def changeVolume(sound,factor):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * factor)
    
  return sound
  
# Finds the maximum sample value in a sound, and returns it.
def maxSample(sound):
  #Create an array to hold sample levels(values)
  levels = []        
  
  for i in range(1, getLength(sound)):
    levels.append(getSampleValueAt(sound, i))
  
  #Assign variable to max sample value and return
  peak = max(levels)        
  print("Maximum sample value: %d" % peak)      
  return peak

# Increases sound to the maxium value.
def maxVolume(sound):
  #Get max sample value
  peak_value = maxSample(sound)
  
  #Maximum value for 16-bit depth audio (change for different bit depths)
  max_possible_sample_value = 32767
  factor = float(max_possible_sample_value/peak_value)
  
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * factor)
  
  return sound
                   
# Increases volume of each sample in sound to "eleven".
# Endorsed by Nigel Tufnel and those who don't let volume knobs stop them.
def goToEleven(sound):
  st_factor = maxSample(sound)
  
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * st_factor)
  
  return sound
                 					
# Returns sound from file.
def getSound():
  return makeSound(pickAFile())
  
  
  