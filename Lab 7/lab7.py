# Ryan Dorrity, Cody Young
# Lab 7 
# 11/11/2018

############### Warm Up ####################
############################################

def main():
  snow = simpleCopy(getPic())
  snowman(snow)







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
  #(canvas)
  return canvas

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