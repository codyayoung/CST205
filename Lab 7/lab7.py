# Ryan Dorrity, Cody Young
# Lab 7 
# 11/11/2018

# Main function
def main():
  snow = simpleCopy(getPic())
  snowman(snow)

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
  #Get first photo for background (leaf border, need to use it for chroma key) 
  pic = getPic()
  width = getWidth(pic)
  height = getHeight(pic)
  
  #Get second photo for border (photo)
  border = getPic()
  border_width = getWidth(border)
  border_height = getHeight(border)
  
  #Copy first photo onto empty canvas(leaf border), overlay photo  
  canvas = makeEmptyPicture(width, height)  
  pyCopy(border,canvas,0,0)
  addTextWithStyle(canvas,280,580,"Happy Thanksgiving!",makeStyle(serif,bold,36),red)                    
  chromaKey(pic,canvas)
  
  #Note: Change directory to your working directory
  explore(pic)
  #dir = "C:\Users\Cody\Documents\CSUMB\CST 205\CST 205 - Images\Image Functions\Lab 7/thanksgivingcard.png"
  #writePictureTo(pic, dir) 
  return pic	

# Returns the picture given a directory
def getPic():
  return makePicture(pickAFile())
    
# Makes empty picture
def simpleCopy(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  canvas = makeEmptyPicture(width, height)
  for x in range (0, width):
    for y in range (0, height):
      color = getColor(getPixel(pic, x, y))
      setColor(getPixel(canvas, x, y), color)

  return canvas
  
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
    	
############################################
# Parameters: pic is a greenscreen image, back is 
# the background image. 
def chromaKey(pic, back):
  for x in range (0, getWidth(pic)):
    for y in range(0, getHeight(pic)):
      pic_p = getPixel(pic, x, y)
      back_p = getPixel(back, x, y)
      if distance(makeColor(0, 0, 0), getColor(pic_p)) < 75:
        setColor(pic_p, getColor(back_p))
  
  return pic 