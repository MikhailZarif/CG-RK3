import math
import numpy as np


def Rotation(x, y, alpha):
    matrix = np.array([[math.cos(alpha), math.sin(-1 * alpha), 0], [math.sin(alpha), math.cos(alpha), 0], [0, 0, 1]])
    M1 = np.array([[1, 0, x], [0, 1, y], [0, 0, 1]])
    M2 = np.array([[1, 0, -1 * x], [0, 1, -1 * y], [0, 0, 1]])
    A = M1.dot(matrix)
    A = A.dot(M2)
    return A


def Normalize(Xa, Ya, Za, Xb, Yb, Zb, Xc, Yc, Zc):
    Ny = (Zb - Za) * (Xc - Xa) - (Zc - Za) * (Xb - Xa)
    Nz = -((Yb - Ya) * (Xc - Xa) - (Yc - Ya) * (Xb - Xa))
    Nx = -(Nz * (Zb - Za) + Ny * (Yb - Ya)) / (Xb - Xa)
    Test = -(Nz * (zc - za) + Ny * (yc - ya)) / (xc - xa)

    if Test != Nx:
        raise Exception(ValueError)
    else:
        return Nx, Ny, Nz


def point_in_projection(Xa, Ya, Za, Xb, Yb, Zb, Xc, Yc, Zc, x, y):
    first_equation = (Xa - x) * (Yb - Ya) - (Xb - Xa) * (Ya - y)
    second_equation = (Xb - x) * (Yc - Yb) - (Xc - Xb) * (Yb - y)
    third_equation = (Xc - x) * (Ya - Yc) - (Xa - Xc) * (Yc - y)
    if first_equation < 0 and second_equation < 0 and third_equation < 0:
        return True
    else:
        return False

