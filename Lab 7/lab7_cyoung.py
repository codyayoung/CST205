# Cody Young
# (insert partner's name here)
# Team SCSI Logic - Ryan Dorrity, Sara Kazemi, Nathan Warren-Acord, Cody Young
# 2018-11-13

# Warmup
# Draws a "snowman" in a desert scene. Hilarious.
# def snowman():
	# Get desert background
	# Draw three circles of decrementing radius
	# Return pic 

# Problem 1 - Thanksgiving Card
# Makes a custom Thanksgiving card. 
# def thanksCard():
	# Get picture 1 (background)
	# Get picture 2 (turkey?)
	# Get picture 3 ()
	# Put picture 2 on 1
	# Put picture 3 on 1 


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