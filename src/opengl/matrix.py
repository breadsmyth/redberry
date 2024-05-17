import math
import numpy


def identity():
    return numpy.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]]).astype(float)
    
def translate(x, y, z):
    return numpy.array([
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]]).astype(float)
    
def rotate_x(angle):
    c = math.cos(angle)
    s = math.sin(angle)

    return numpy.array([
        [1, 0, 0, 0],
        [0, c, -s, 0],
        [0, s, c, 0],
        [0, 0, 0, 1]]).astype(float)
    
def rotate_y(angle):
    c = math.cos(angle)
    s = math.sin(angle)

    return numpy.array([
        [c, 0, s, 0],
        [0, 1, 0, 0],
        [-s, 0, c, 0],
        [0, 0, 0, 1]]).astype(float)
    
def rotate_z(angle):
    c = math.cos(angle)
    s = math.sin(angle)

    return numpy.array([
        [c, -s, 0, 0],
        [s, c, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]]).astype(float)
    
def scale(n):
    return numpy.array([
        [n, 0, 0, 0],
        [0, n, 0, 0],
        [0, 0, n, 0],
        [0, 0, 0, 1]]).astype(float)
    
def perspective(angle_of_view=60,
                aspect_ratio=1,
                near=0.1,
                far=1000):
    a = angle_of_view * math.pi / 180
    d = 1 / math.tan(a/2)
    r = aspect_ratio
    b = (near + far) / (near - far)
    c = 2 * near * far / (near - far)

    return numpy.array([
        [d/r, 0, 0, 0],
        [0, d, 0, 0],
        [0, 0, b, c],
        [0, 0, -1, 0]]).astype(float)
    