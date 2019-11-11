from math import *

"""
nx, ny, nz  = input("pyramidNormal x,y,z ").split()
nx, ny, nz = float(nx), float (ny), float (nz)

a = float(input("pyramidApex.y "))
qx, qy, qz  = input("Q x,y,z ").split()
qx, qy, qz = float(qx), float (qy), float (qz)
"""

nx = -34
ny = -5
nz = 0
a = -100
qx = 168
qy = -300
qz = 290.98

c0 = (nx * qx + ny * qy + nz * qz - a * ny) * (nx * qx + ny * qy + nz * qz - a * ny) 
c1 = (a * ny) * (a * ny)
k1 = (c0 - c1) * (  nx * nx + nz * nz )
k2 = (c0 - c1) * ( ny * ny  + nz * nz )
k3 = -2 * a * nx * ny * (c0 - c1) +2 * c1 * nz * (nz * qx - qz * nx)
k4 = 2 * (c0 - c1) * nx * ny
k5 = -2 * a * ny * ny * (c0 - c1) +2* c1* nz * (nz * qy - qz * ny)
k6 = (c0 - c1)* a * a * ny * ny - c1 * nz *nz * (qx*qx + qy*qy + qz*qz) + 2*a*c1*qz*ny*nz

c3 = -( nz * (nz * qy - ny * qz) - nx * (ny * qx - nx * qy)) / (nz * (nx * qz - nz * qx) - ny * (ny * qx - nx * qy))
c4 = - a* ny * (ny * qx - nx * qy)/ (nz * (nx * qz - nz * qx) - ny * (ny * qx - nx * qy))


aa = k1 + k2 * c3 * c3 + k4 * c3
bb = 2 * k2 * c3 * c4 + k3 + k4 * c4 + k5 * c3
cc = k2 * c4 * c4 + k5 * c4 + k6


if(aa==0):
    x = -cc/bb
    y = c3 * x + c4
    z = (a * ny - nx * x - ny * y) / nz
elif(aa!=0):
    x1 = (-bb + sqrt(bb * bb -4 * aa * cc))/(2*aa)
    x2 = (-bb - sqrt(bb * bb -4 * aa * cc))/(2*aa)
    y1 = c3 * x1 + c4
    y2 = c3 * x2 + c4
    z1 = (a * ny - nx * x1 - ny * y1) / nz
    z2 = (a * ny - nx * x2 - ny * y2) / nz

m1 =(nx*qx + ny*qy +nz*qz -a*ny)/sqrt((qx-x1)*(qx-x1) + (qy-y1)*(qy-y1) + (qz-z1)*(qz-z1))
l1 = -a * ny / sqrt(x1*x1 + y1*y1 +z1*z1)

m2 =(nx*qx + ny*qy +nz*qz -a*ny)/sqrt((qx-x2)*(qx-x2) + (qy-y2)*(qy-y2) + (qz-z2)*(qz-z2))
l2 = -a * ny / sqrt(x2*x2 + y2*y2 +z2*z2)

if( m1==l1 ):
    print(x1, y1, z1)
elif( m2 == l2 ):
    print(x2, y2, z2)
else:
    print(m1, l1)
    print(m2, l2)
