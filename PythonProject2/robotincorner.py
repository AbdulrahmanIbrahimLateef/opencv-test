import cv2 as cv
import sys

#image img is the room the robot travels through
img = cv.imread(cv.samples.findFile("room.jpg"))
#image img2 is the path the robot should follow in the room
img2 = cv.imread(cv.samples.findFile("robotpath.jpg"))
if img is None:
    sys.exit("Could not read the image.")
if img2 is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("1.png", img)