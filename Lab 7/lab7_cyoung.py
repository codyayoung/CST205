# Cody Young
# Ryan Dorrity 
# Team SCSI Logic - Ryan Dorrity, Sara Kazemi, Nathan Warren-Acord, Cody Young
# 2018-11-13
 
# Problem 1 - Thanksgiving Card
# Makes a custom Thanksgiving card. 
def thanksCard():
  #Get first photo for background
  pic = getPic()
  width = getWidth(pic)
  height = getHeight(pic)
  
  #Get second photo for border
  border = getPic()
  border_width = getWidth(border)
  border_height = getHeight(border)
  
  canvas = makeEmptyPicture(width, height)
  pyCopy(pic,canvas,0,0)
  
  show(canvas)
  return canvas
  

# ----------------
# Helper Functions
# ----------------

# Copies a source image to a new location in a target image.
def pyCopy(source, target, targetX, targetY):
  #Target width variable
  resultX = targetX
  for x in range(0, getWidth(source)):
    #Target height variable 
    resultY = targetY
    for y in range(0, getHeight(source)):
      target_pixels = getColor(getPixel(source, x, y))
      setColor(getPixel(target, resultX, resultY), target_pixels)
      resultY += 1
    resultX += 1
        
  return target
 
# Returns a picture.
def getPic():
  return makePicture(pickAFile())