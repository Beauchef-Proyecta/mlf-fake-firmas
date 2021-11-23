import linedraw
import cv2

lines = linedraw.sketch("images/Cristiano_Ronaldo_Signature_JPG.jpg")

#lines = linedraw.sketch("images/Firma_Profe.jpeg")

linedraw.visualize(lines) 
