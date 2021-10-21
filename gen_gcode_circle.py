# Este srcript genera codigo G para dibujar una circunferencia de altura 
# constante z con centro (x0, y0). Genera n_points puntos y da la opción de plotear

from numpy import cos, sin, pi, round
import matplotlib.pyplot as plt


def gen_circle_points(n_points, r, z, center):
    x0, y0 = center
    x = []
    y = []
    theta = 0
    dt = 2 * pi / n_points

    for i in range(n_points + 1):
        x.append(round(x0 - r * cos(theta), 1))
        y.append(round(y0 - r * sin (theta), 1))
        theta += dt
        print('G1 X' + str(x[i]) + ' Y' + str(y[i]) + ' Z' + str(z))

    return [x, y]

ns, rs, zs, x0s, y0s, plot = input("Enter: Npoints radius zheight center [plot?] y/n\n").split()
n = int(ns)
r = float(ns)
z = float(rs)
x0 = float(x0s)
y0 = float(y0s)

x, y = gen_circle_points(n, r, z, (x0, y0))

if (plot == 'y'):
    plt.plot(x, y)
    plt.scatter(0, 0, color='k')
    plt.axis('scaled')
    plt.show()

