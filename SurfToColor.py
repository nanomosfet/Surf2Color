#!/usr/bin/python
import RPi.GPIO as GPIO
import webcolors
from bs4 import BeautifulSoup as bs4
import urllib
import time



GPIO.setmode(GPIO.BCM)
GPIO.setup([2, 3, 4], GPIO.OUT)
R = GPIO.PWM(2,60)
G = GPIO.PWM(3,60)
B = GPIO.PWM(4,60)
R.start(50)
G.start(50)
B.start(50)

while(1):
	soup = bs4(urllib.urlopen('http://www.surfline.com/surf-forecasts/southern-california/south-san-diego_2953'))

	rgb = webcolors.hex_to_rgb(str(soup.select("div.day-slider-container div[style*=background] ")[0])[62:69])

	r = float(rgb[0])/256*100
	g =float(rgb[1])/256*100
	b  =float(rgb[2])/256*100 
	print(r,g,b)
	R.ChangeDutyCycle(100-r)
	G.ChangeDutyCycle(100-g)
	B.ChangeDutyCycle(100-b)
	time.sleep(10000)


	

