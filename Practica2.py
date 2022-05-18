import numpy as np
from matplotlib import pyplot as plt
import math as ma
import cv2 #opencv
import os


imagen1 = cv2.imread('animada.png',cv2.IMREAD_UNCHANGED)
imagen2 = cv2.imread('color.png',cv2.IMREAD_UNCHANGED)

imagen3 = cv2.imread('imagen1_rsize.jpg',cv2.IMREAD_UNCHANGED)
imagen4 = cv2.imread('imagen2_rsize.jpg',cv2.IMREAD_UNCHANGED)
imagen5 = cv2.imread('imagen3_rsize.jpg',cv2.IMREAD_UNCHANGED)

new_width=500
new_height=450

dsize=(new_width,new_height)
output1=cv2.resize(imagen1,dsize)
cv2.imwrite('imagen3_rsize.jpg',output1)

dsize=(new_width,new_height)
output2=cv2.resize(imagen1,dsize)
cv2.imwrite('imagen1_rsize.jpg',output2)

output22=cv2.resize(imagen2,dsize)
cv2.imwrite('imagen2_rsize.jpg',output22)
cv2.imshow("imagen1", imagen1)
x=cv2.waitKey(0)

#Operaciones

while True:
#La suma
    if x == ord("d"):
        cv2.destroyAllWindows()
        output3=imagen3+imagen4
        cv2.imshow("Suma1", output3)
        output4=cv2.add(imagen3,imagen4)
        cv2.imshow("Suma2", output4)
        output5=np.add(imagen3,imagen4)
        cv2.imshow("Suma3", output5)
        x=cv2.waitKey(0)

#La resta
    if x == ord("d"):
        cv2.destroyAllWindows()
        output6=imagen3-imagen4
        cv2.imshow("Resta 1", output6)
        output7=np.subtract(imagen3,imagen4)
        cv2.imshow("resta2", output7)
        output8=cv2.subtract(imagen3,imagen4)
        cv2.imshow("resta3", output8)
        x=cv2.waitKey(0)
                
#La división
    if x == ord("d"):
        cv2.destroyAllWindows()
        output9=imagen3/imagen4
        cv2.imshow("div1", output9)
        output10=np.divide(imagen3,imagen4)
        cv2.imshow("div2", output10)
        output11=cv2.divide(imagen3,imagen4)
        cv2.imshow("div3", output11)
        x=cv2.waitKey(0)
                
#La Multiplicación
    if x == ord("d"):
        cv2.destroyAllWindows()
        output12=imagen3*imagen4
        cv2.imshow("Multi1", output12)
        output13=np.multiply(imagen3,imagen4)
        cv2.imshow("Multi2", output13)
        output14=cv2.multiply(imagen3,imagen4)
        cv2.imshow("Multi3", output14)
        x=cv2.waitKey(0)

#Raíz
    if x == ord("d"):
        cv2.destroyAllWindows()
        output16=imagen3*imagen4
        cv2.imshow("raiz1", output16)
        output17=np.multiply(imagen3,imagen4)
        cv2.imshow("raiz2", output17)
        output18=cv2.multiply(imagen3,imagen4)
        cv2.imshow("Raiz3", output18)
        x=cv2.waitKey(0)  
#Potencia
    if x == ord("d"):
        cv2.destroyAllWindows()
        output20=output14**2
        cv2.imshow("Potencia1", output20)
        output21=cv2.pow(output14,2)
        cv2.imshow("Potencia2", output21)
        output22=cv2.pow(output14,2)
        cv2.imshow("Potencia3", output22)
        x=cv2.waitKey(0)
#Conjunción
    if x == ord("d"):
        cv2.destroyAllWindows()
        output23=cv2.bitwise_and(imagen3,imagen4)
        cv2.imshow("Conjuncion3", output23)
        x=cv2.waitKey(0)
#Disyunción
    if x == ord("d"):
        cv2.destroyAllWindows()
        output24=cv2.bitwise_or(imagen3,imagen4)
        cv2.imshow("Disyuncion3", output24)
        x=cv2.waitKey(0)
#Negación
    if x == ord("d"):
        cv2.destroyAllWindows()
        output25=cv2.bitwise_not(imagen3)
        cv2.imshow("Negacion", output25)
        x=cv2.waitKey(0)
#Escalado
    if x == ord("d"):
        cv2.destroyAllWindows()
        output27=cv2.resize(imagen3,(500,200), interpolation=cv2.INTER_CUBIC)
        cv2.imshow("Escalado", output27)
        x=cv2.waitKey(0)
        
#Rotación
    if x == ord("d"):
        cv2.destroyAllWindows()
        ancho = imagen3.shape[1] 
        alto = imagen3.shape[0] 
        rotation= cv2.getRotationMatrix2D((ancho//5,alto//5),10,1)
        imagenSalida2 = cv2.warpAffine(imagen3,rotation,(ancho,alto))
        cv2.imshow("rotacion",imagenSalida2)
        x=cv2.waitKey(0)

               
    break
    


cv2.waitKey(0)
cv2.destroyAllWindows()
