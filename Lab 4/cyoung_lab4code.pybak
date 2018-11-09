# Cody Young
# CST 205
# Lab 4
# 2018-11-6

# Problem 1
# Mirroring Functions

# Does a vertical half mirror. Copies left hand side of image to right hand side. 
def mirrorHalfVertical():
  file = pickAFile()
  pic = makePicture(file)
  
  #Get width and height of source image 
  width = getWidth(pic)
  height = getHeight(pic)
  #Create empty picture to hold result
  result = makeEmptyPicture(width, height)
  
  #Get color of pixels from half left side of image(width) and full height of image
  for x in range(0, width/2 + 1):     
    for y in range(0, height):     
      result_pixels = getColor(getPixel(pic, x, y))
      setColor(getPixel(result, x, y), result_pixels)
      setColor(getPixel(result, width - x - 1, y), result_pixels)
      
  #writePictureTo(result, "C:\Users\Cody\Documents\CSUMB\CST 205\Lab 4\problem1_verthalf.jpg")    
  show(result)

# Does a horizontal half mirror. Copies bottom half of the image to the top half.
def mirrorHalfHorizontal():
  file = pickAFile()
  pic = makePicture(file)
  
  #Get width and height of source image 
  width = getWidth(pic)
  height = getHeight(pic)
  #Create empty picture to hold result
  result = makeEmptyPicture(width, height)
  
  #Get color of pixels from bottom half of image(half height), and full width of image
  for x in range(0, width):
    for y in range(0, height):
      result_pixels = getColor(getPixel(pic, x, y))
      setColor(getPixel(result, x, y), result_pixels)
      setColor(getPixel(result, x, height - y - 1), result_pixels)
      
  #writePictureTo(result, "C:\Users\Cody\Documents\CSUMB\CST 205\Lab 4\problem1_horzhalf.jpg")    
  show(result)  

# Does a four way mirror. Executes a horizontal half mirror first, then a vertical half mirror.
def fourWayMirror():
  file = pickAFile()
  pic = makePicture(file)
  
  #Get width and height of source image 
  width = getWidth(pic)
  height = getHeight(pic)
  
  #Create empty picture to hold result
  result = makeEmptyPicture(width, height)
        
  #Horizontal half mirror
  for x in range(0, width):
    for y in range(0, height):
      result_pixels = getColor(getPixel(pic, x, y))
      setColor(getPixel(result, x, y), result_pixels)
      setColor(getPixel(result, x, height - y - 1), result_pixels)
  
  #Vertical half mirror
  for x in range(0, width/2 + 1):     
    for y in range(0, height):     
      result_pixels = getColor(getPixel(result, x, y))
      setColor(getPixel(result, x, y), result_pixels)
      setColor(getPixel(result, width - x - 1, y), result_pixels)
                          
  #writePictureTo(result, "C:\Users\Cody\Documents\CSUMB\CST 205\Lab 4\problem1_4waymirror.jpg")
  show(result)
  return result
  
# Problem 2
# Copying Pictures

# Simple function that returns a picture object.
def simplePic():
  mypic = makeEmptyPicture(576,1024)
  for x in range (0, getWidth(mypic)):
    for y in range (0, getHeight(mypic)):
      setColor(getPixel(mypic, x, y), blue)
  show(mypic)
  return mypic

# Copies a source picture and returns a picture object.
def simpleCopy(source):
  source = makePicture(pickAFile())
  
  #Create empty target picture
  width = getWidth(source)
  height = getHeight(source)
  result = makeEmptyPicture(width, height)
  
  #Copy all pixels from source to target
  for x in range (0, width):
    for y in range (0,height):
      result_pixels = getColor(getPixel(source, x, y))
      setColor(getPixel(result, x, y), result_pixels)
  
  #writePictureTo(result, "C:\Users\Cody\Documents\CSUMB\CST 205\Lab 4\problem2_copy.jpg")        
  show(source)    
  show(result)
  return source 
  return result

# Problem 3
# Rotates a picture.
def rotatePic():
  source = makePicture(pickAFile())
  
  #Create empty target picture
  width = getWidth(source)
  height = getHeight(source)
  result = makeEmptyPicture(height, width)
  
  #Copy all pixels from source to target
  for x in range (0, width):
    for y in range (0, height):
      result_pixels = getColor(getPixel(source, x, height-y-1))
      setColor(getPixel(result, height-y-1, width-x-1), result_pixels)
  
  #writePictureTo(result, "C:\Users\Cody\Documents\CSUMB\CST 205\Lab 4\problem3_rotate.jpg")        
  show(source)
  show(result)
  return source 
  return result

# Problem 4
# Resizes(shrinks)a copy of a photo.
def shrink():
  source = makePicture(pickAFile())
  
  #Get width and height of original picture
  width = getWidth(source)
  height = getHeight(source)
  print("Original width: %d" % width)
  print("Original height: %d" % height)
  
  result_width = 0
  result_height = 0
  
  #Get dimensions for resulting image
  for x in range(0,width,2):
    result_width = result_width + 1
  for y in range(0,height,2):
    result_height = result_height + 1
  
  print("Resulting width: %d" % result_width)
  print("Resulting height: %d" % result_height)
  
  #Create blank image with target dimensions 
  result = makeEmptyPicture(result_width, result_height)
    
  #Sample half of pixels from original image, and copy to new resized image
  #Result image width 
  result_x = 0                        
  for x in range(0,width,2):
    #Result image height
    result_y = 0
    for y in range(0,height,2):
     result_pixels = getColor(getPixel(source, x, y))
     setColor(getPixel(result, result_x, result_y), result_pixels)
     result_y = result_y + 1    #Increment by 1 in target image 
    result_x = result_x + 1     #Increment by 1 in target image   
    
  #writePictureTo(result, "C:\Users\Cody\Documents\CSUMB\CST 205\Lab 4\problem4_shrink.jpg")
  show(source)
  show(result)
  return result
  
    
  
   
 
   
  

  
  
      
