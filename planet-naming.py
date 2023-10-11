import cv2

img = cv2.imread("solar-system.jpg")




cv2.putText(img,
        "Sun",(100,90),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,
        "Mercury",(125,235),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,
        "Venus",(200,250),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,
        "Earth",(295,255),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,
        "Moon",(326,187),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,
        "Mars",(390,247),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,
        "Jupiter",(580,365),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,
        "Saturn",(775,290),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,
        "Uranus",(980,279),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,
        "Neptune",(1125,275),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))

cv2.imshow("output",img)
cv2.waitKey(0)