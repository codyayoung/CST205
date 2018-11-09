def halfBetter():
  file = pickAFile()
  pic = makePicture(file)
  for x in range(0, getWidth(pic)):
    for y in range(getHeight(pic)/2, getHeight(pic)):
      p = getPixel(pic, x, y)
      r = getRed(p)
      setRed(p, r*0.5)
  repaint(pic)
  writePictureTo(pic, "C://Users//Cody//Desktop//420noscopesmlgpro_shrekt_edition.jpg")
  