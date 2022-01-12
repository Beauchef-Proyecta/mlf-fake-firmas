import detectionV1
import RPIclass
import svg2gcode
import gcode_to_IK as ik
import os

# Mover el brazo
ik.robot(os.getcwd() + "/correte.gcode")
# QUE NO TE SAQUEN LA FOTO
raspi = RPIclass.Camera()
raspi.capture('test')

# Detectamos la firma
path = raspi.path
det = detectionV1.Detector(path)
det.add_img( [300, 800, 0, 1000] )
det.extract_contours()
det.save_img('test')

# Hacemos scp

# Convertimos JPG a SVG de forma manual
s= raw_input()  # Esperamos el input del usuario para continuar
if s=='1': ack = True

# Hacemos np.inverse(scp)

# Se sigue por convertir el SVG a GCODE
if ack:
    svg2gcode(os.getcwd() + "/test.svg")    
    ik.robot(os.getcwd() + "/test.gcode")
else:
    print('la cagaste en algo')
    pass

