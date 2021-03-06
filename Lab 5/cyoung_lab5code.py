# Cody Young
# CST 205
# Lab 5
# 2018-11-6

import random

#Warmup
#Copies a source image to a bigger target image.
def simpleCopy(source):
  source = makePicture(pickAFile())
  
  #Create empty target picture
  width = getWidth(source)
  height = getHeight(source)
  result = makeEmptyPicture(width * 2, height * 2)
  
  #Copy all pixels from source to target
  for x in range (0, width):
    for y in range (0,height):
      result_pixels = getColor(getPixel(source, x, y))
      setColor(getPixel(result, x, y), result_pixels)
         
  show(source)    
  show(result)
  return source 
  return result 

# Problem 1
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
  
# Problem 2
# Creates a 8.5 x 11 collage from source photos and applies random effects.
def makeCollage():
  #Create blank target image 
  target = makeEmptyPicture(2550,3300)
  target_width = getWidth(target)
  target_height = getHeight(target)
  
  #Get images for collage, place in array(list) of pixel objects 
  pictures = list()
  for i in range(0,8):
    pictures.append(getSource())
    
  #Apply random effect to image
  j=0
  for pics in pictures:
    randomEffect(pictures[j])
    j+=1
  
  #Add pictures to collage
  #Left column
  target = pyCopy(pictures[0], target, 0, 0)
  target = pyCopy(pictures[1], target, 0, 825) 
  target = pyCopy(pictures[2], target, 0, 1650) 
  target = pyCopy(pictures[3], target, 0, 2475) 
  
  #Right column 
  target = pyCopy(pictures[4], target, 1275, 0) 
  target = pyCopy(pictures[5], target, 1275, 825) 
  target = pyCopy(pictures[6], target, 1275, 1650) 
  target = pyCopy(pictures[7], target, 1275, 2475)   
                                 
  # Note: Change the dir variable to reflect your own working directory
  dir = "C:\Users\Cody\Documents\CSUMB\CST 205\Lab 5\collage.jpg"
  writePictureTo(target,dir) 
  return target
  
# ----------------                   
# Helper Functions - Image Manipulations 
# ----------------

# Applies a random effect to a source image. Returns image.  
def randomEffect(source):
  choice = random.randint(0,8)
  if choice == 0:
    roseColoredGlasses(source)
  elif choice == 1:
    mirrorHalfVertical(source)
  elif choice == 2:
    mirrorHalfHorizontal(source)
  elif choice == 3:
    fourWayMirror(source)
  elif choice == 4:
    makeNegative(source)
  elif choice == 5:
    betterBnW(source)
  elif choice == 6:
    moreRed(source, 75)
  elif choice == 7:
    lessRed(source, 50)
  else:
    return source
  
# Improved grayscale function using weights  
def betterBnW(pic):
   pixels = getPixels(pic)
   for p in pixels:
      # Find opposite of color by subtracting from max and multiply by weight
      newColor =  (getRed(p) * 0.299 + getGreen(p) * 0.587 + getBlue(p) * 0.114) / 3
      setColor(p, makeColor(newColor, newColor, newColor))
   return pic

# Does a four way mirror. Executes a horizontal half mirror first, then a vertical half mirror.
def fourWayMirror(pic):
  #Get width and height of source image 
  width = getWidth(pic)
  height = getHeight(pic)
        
  #Horizontal half mirror
  for x in range(0, width):
    for y in range(0, height):
      result_pixels = getColor(getPixel(pic, x, y))
      setColor(getPixel(pic, x, height - y - 1), result_pixels)
  
  #Vertical half mirror
  for x in range(0, width/2 + 1):     
    for y in range(0, height):     
      result_pixels = getColor(getPixel(pic, x, y))
      setColor(getPixel(pic, width - x - 1, y), result_pixels)
                              
  return pic

# Does a vertical half mirror. Copies left hand side of image to right hand side. 
def mirrorHalfVertical(pic):
  #Get width and height of source image 
  width = getWidth(pic)
  height = getHeight(pic)

  #Get color of pixels from half left side of image(width) and full height of image
  for x in range(0, width/2 + 1):     
    for y in range(0, height):     
      result_pixels = getColor(getPixel(pic, x, y))
      setColor(getPixel(pic, width - x - 1, y), result_pixels)
      
  return pic

# Does a horizontal half mirror. Copies bottom half of the image to the top half.
def mirrorHalfHorizontal(pic):
  #Get width and height of source image 
  width = getWidth(pic)
  height = getHeight(pic)

  #Get color of pixels from bottom half of image(half height), and full width of image
  for x in range(0, width):
    for y in range(0, height):
      result_pixels = getColor(getPixel(pic, x, y))
      setColor(getPixel(pic, x, height - y - 1), result_pixels)
          
  return pic

# Reduces amount of redness by the percentage passed in to the parameter        
def lessRed(pic, percent):
   pixels = getPixels(pic)
   for p in pixels:
    r = getRed(p)
    # Reduce red value and set new value 
    setRed(p, r - (r * (percent/100)))
    
   return pic 

# Increases amount of redness by the percentage passed in to the parameter      
def moreRed(pic, percent):
   pixels = getPixels(pic)
   for p in pixels:
    r = getRed(p)
    setColorWrapAround(0)
    newRed = r + (r * (percent/100))
    setRed(p, newRed)
    
   return pic 

# Alters the picture so that it is the negative of the original
def makeNegative(pic):
   pixels = getPixels(pic)
   for p in pixels:
    # Find opposite of color by subtracting from max
     r = 255 - getRed(p) 
     g = 255 - getGreen(p) 
     b = 255 - getBlue(p)
     setColor(p, makeColor(r, g, b))
     
   return pic

# Makes an image appear pink
def roseColoredGlasses(pic):
   pixels = getPixels(pic)
   for p in pixels:
     myRed = getRed(p) 
     myGreen = getGreen(p) * .50
     myBlue = getBlue(p) * .75
     setColor(p, makeColor(myRed, myGreen, myBlue))
     
   return pic 

# Gets a picture from a directory and creates a picture object. 
def getSource():
  return makePicture(pickAFile())
