import linedraw
import cv2

lines = linedraw.sketch("images/Cristiano_Ronaldo_Signature_JPG.jpg")

#lines = linedraw.sketch("images/Firma_Profe.jpeg")

#lines = linedraw("images/Cristiano_Ronaldo_Signature_JPG.jpg")

linedraw.visualize(lines) 
