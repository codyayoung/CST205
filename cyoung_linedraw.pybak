# Cody Young
# Line Drawing Function - JES 
# 2018-11-13

import math 

# Converts an image to black and white, and then turns pixels to black or white to simulate a pencil/pen drawn sketch. 
def lineDraw():
  #Input picture, get height and width variables 
  pic = getPic()
  show(pic)
  height = getHeight(pic)
  width = getWidth(pic)
  print("Height: %d" % height)
  print("Width: %d" % width) 
  
  #Convert to grayscale and return pic
  betterBnW(pic)
  
  #Threshold value for luminance (difference)
  threshold = 9
  
  for x in range (0, width-1):
    for y in range(0, height-1):
      source = getPixel(pic, x, y)                          #Get current pixel 
      source_lum = getLuminance(source)                   #Luminance of current pixel
      if x >= width: 
        target_right = getLuminance(getPixel(pic, x, y))    #If at last pixel on border, use it instead    
      else:
        target_right = getLuminance(getPixel(pic, x+1, y))  #Pixel one to right (width + 1)
      if y >= height:
        target_below = getLuminance(getPixel(pic, x, y))    #If at last pixel on border, use it instead
      else:      
        target_below = getLuminance(getPixel(pic, x, y+1))  #Pixel one below (height + 1)    
      
      diff_right = abs(source_lum - target_right)
      diff_below = abs(source_lum - target_below)
      
      #If luminance difference of right and below pixels are greater than threshold, set pixel to black, else set to white 
      if diff_right > threshold and diff_below > threshold:   
        setColor(source, black)
      else:
        setColor(source, white)
        
  repaint(pic)
  #Note: Change 'dir' to your working directory
  dir = "C:\Users\Cody\Documents\CSUMB\CST 205\CST 205 - Images\Image Functions\linedrawn.jpg"
  writePictureTo(pic, dir)
  
  return pic

# ----------------  
# Helper Functions
# ----------------
# Returns the luminance value of a pixel 
def getLuminance(pixel):
  r = getRed(pixel)
  g = getGreen(pixel)
  b = getBlue(pixel)
  
  luminance = (0.299 * r) + (0.587 * g) + (0.114 * b)
  
  return luminance 
  
# Converts an image to grayscale 
def betterBnW(pic):
  pixels = getPixels(pic)
  
  for p in pixels:
    grayscale = ((getRed(p) * 0.299) + (getGreen(p) * 0.587) + (getBlue(p) * 0.114))
    setColor = (p, makeColor(grayscale, grayscale, grayscale))
    
  return pic

def getPic():
  return makePicture(pickAFile())
  
