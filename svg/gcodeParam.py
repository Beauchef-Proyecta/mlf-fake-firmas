import math
import os
class svgParam:
    def __init__(self, gcode = '', home = (0,0,0), dim = 1):
        self.gcode = gcode
        self.home = home
        self.x, self.y, self.z = home
        self.dim = dim
        self.ratio = 1 
    
    def parametrizadorInador(self):   
        def seisInador(n):       # funcion auxiliar para asegurar 6 digitos decimales
            s = str(n)
            dot = s.index('.') 
            preDot, postDot = s[:dot+1], s[(dot+1):]
            if len(postDot) <= 6:       # Si tiene 6 decimales o menos agergamos 0 a la cola hasta llegar a 6
                while len(postDot) < 6:     # Al llegar a 6 sale del loop (si tiene 6 desde un inicio se lo salta)
                    postDot += '0'
                return preDot+postDot
            else:       # Si tiene mas de 6 decimales se trunca al sexto
                postDot = postDot[:6]
                return preDot + postDot
        with open(self.gcode, 'r+') as f:
            newG = ''
            G = f.readlines()
            h = self.z
            for line in G:
                if line[:2] == 'G1' and 'X' in line and 'Y' in line:    # Instruccion de movimiento
                    print(line)
                    xpos, ypos = line.index('X'), line.index('Y')
                    xval, yval = float(line[xpos+1:ypos-1]), float(line[ypos+1:len(line)-2])
                    paramX = seisInador(self.x + self.ratio * xval)   # Se aseguran 6 decimales
                    paramY = seisInador(self.y + self.ratio * yval)   # Se aseguran 6 decimales
                    newG += line[0:xpos] + 'X{} '.format(paramX) + 'Y{} '.format(paramY) + 'Z{};'.format(h) + '\n'
                else:
                    newG += line
            f.truncate(0)
            f.seek(0)   # Cursos al inicio del archivo
            f.write(newG)    # Sobreescribimos con el archivo modificado

        
                     


