# Cody Young
# Lab 7
# Line Drawing Function
# 2018-11-13

import math 

# Main function
# Converts an image to black and white, and then turns pixels to black or white to simulate a "line drawn" effect. 
def lineDraw(pic):
	#Input picture, get height and width variables 
	pic = getPic()
	height = getHeight(pic)
	width = getWidth(pic)
	
	#Convert to grayscale and return pic
	betterBnW(pic)
	
	#Threshold value for luminance (difference)
	lum_threshold = 50 
	
	for x in range (0, width):
		for y in range(0, height):
			source= getPixel(pic, x, y)
			source_lum = getLuminance(source)										#Luminance of current pixel 
			target_right = getLuminance(getPixel(pic, x+1, y)		#Pixel one to the right (width + 1)
			target_below = getLuminance(getPixel(pic, x, y+1)		#Pixel one below (height + 1)
			
			diff_right = abs(source_lum - target_right)
			diff_below = abs(source_lum - target_below)
			
			#If difference is greater than threshold, set pixel to black, else set to white 
			if diff_right > lum_threshold and diff_below > lum_threshold:		
				setColor(source, black)
			else:
				setColor(source, white)
	
	return pic
		
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
		setColor = (p, makeColor(grayscale, grayscale, graycscale)
		
	return pic

def getPic():
	return makePicture(pickAFile())
	