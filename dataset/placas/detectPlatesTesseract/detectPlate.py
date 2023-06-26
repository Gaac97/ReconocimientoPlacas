import cv2
import pytesseract
import sys

placa = []

argumentos = sys.argv
path = argumentos[0]



"""image = cv2.imread(path)
if image is None:
    print("No se pudo leer la imagen. Verifica la ruta y asegúrate de que el archivo exista.")
else:
    # Mostrar la imagen
    cv2.imshow("Imagen", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()"""


"""
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.blur(gray,(3,3))
canny = cv2.Canny(gray,150,200)
canny = cv2.dilate(canny,None,iterations=1)

#_,cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)#OpenCV 3
cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)#OpenCV 4
cv2.drawContours(image,cnts,-1,(0,255,0),2)

for c in cnts:
   area = cv2.contourArea(c)

x,y,w,h = cv2.boundingRect(c)
epsilon = 0.09*cv2.arcLength(c,True)
approx = cv2.approxPolyDP(c,epsilon,True)


if len(approx)==4 and area>9000:
  print('area=',area)
  #cv2.drawContours(image,[approx],0,(0,255,0),3)"""