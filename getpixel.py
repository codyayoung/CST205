def getPixelsofRange():
  filename = pickAFile()
  pic = makePicture(filename)
  for i in range(0, 5):
    for j in range(0, 5):
      pix = getPixel(pic, i, j)
      print(pix)
      