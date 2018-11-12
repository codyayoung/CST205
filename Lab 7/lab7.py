# Ryan Dorrity, Cody Young
# Lab 7 
# 11/11/2018

<<<<<<< HEAD
############### Warm Up ####################
############################################

=======
# Main function
>>>>>>> ba09585e10b7f2a09ef02047bf529024a4d454c8
def main():
  snow = simpleCopy(getPic())
  snowman(snow)

<<<<<<< HEAD





=======
############### Warm Up ####################
############################################

def snowman(pic):  
  # Creates body of snowman  
  addArcFilled(pic, 810, 600, 300, 300, 0, 360, white)  
  addArcFilled(pic, 860, 400, 200, 200, 0, 360, white)  
  addArcFilled(pic, 910, 300, 100, 100, 0, 360, white)
  # Creates eyes of snowman  
  addArcFilled(pic, 930, 340, 20, 20, 0, 360, black)  
  addArcFilled(pic, 960, 340, 20, 20, 0, 360, black)  
  addArcFilled(pic, 940, 360, 20, 50, 0, 60, orange)
  # Creates hat
  addRectFilled(pic, 920, 200, 80, 100, black)
  addRectFilled(pic, 900, 280, 120, 20, black)
  explore(pic)

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
  pyCopy(border,canvas,0,0)
  
  explore(canvas)
  return canvas	
>>>>>>> ba09585e10b7f2a09ef02047bf529024a4d454c8

# Returns the picture given a directory
def getPic():
  return makePicture(pickAFile())
<<<<<<< HEAD
  
  
=======
    
>>>>>>> ba09585e10b7f2a09ef02047bf529024a4d454c8
# Makes empty picture
def simpleCopy(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  canvas = makeEmptyPicture(width, height)
  for x in range (0, width):
    for y in range (0, height):
      color = getColor(getPixel(pic, x, y))
      setColor(getPixel(canvas, x, y), color)
  #(canvas)
  return canvas
<<<<<<< HEAD

def snowman(pic):  
  # Creates body of snowman  
  addArcFilled(pic, 810, 600, 300, 300, 0, 360, white)  
  addArcFilled(pic, 860, 400, 200, 200, 0, 360, white)  
  addArcFilled(pic, 910, 300, 100, 100, 0, 360, white)
  # Creates eyes of snowman  
  addArcFilled(pic, 930, 340, 20, 20, 0, 360, black)  
  addArcFilled(pic, 960, 340, 20, 20, 0, 360, black)  
  addArcFilled(pic, 940, 360, 20, 50, 0, 60, orange)
  # Creates hat
  addRectFilled(pic, 920, 200, 80, 100, black)
  addRectFilled(pic, 900, 280, 120, 20, black)
  explore(pic)
=======
  
# Copies a source image to a new location in a blank target image.
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
    
	
>>>>>>> ba09585e10b7f2a09ef02047bf529024a4d454c8