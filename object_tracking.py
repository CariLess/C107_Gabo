import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")

#Cargar el rastreador
tracker = cv2.TrackerCSRT_create()
# Leer el primer cuadro del video
returned, img = video.read() 
# Seleccionar el cuadro delimitador en la imagen
bbox = cv2.selectROI("Rastreando",img ,False)
# Inicializar el rastreador en la imagen y el cuadro delimitador
tracker.init(img, bbox)

print(bbox)

def drawbox(img, bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img, (x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img, "Rastreando", (75,90), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

def goal_track(img, bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])

    # Obtener los puntos centrales del cuadro delimitador

    # Dibujar un pequeño círculo usando los puntos centrales

    # Calcular la distancia
    dist = math.sqrt(((c1-p1)**2) + (c2-p2)**2)
    print(dist)

    # El objetivo se alcanza si la distancia es menor a 20 puntos pixel
    if(dist<=20):
        cv2.putText(img,"Canasta",(300,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

    


while True:
    check,img = video.read()   

    # Actualizar el rastreador en la imagen y el cuadro delimitador
    success, bbox = tracker.update(img)

    if success:
        drawbox(img, bbox)
    else: 
        cv2.putText(img,"Perdido",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

    cv2.imshow("Resultado",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("¡Detenido!")
        break


video.release()
cv2.destroyALLwindows()
