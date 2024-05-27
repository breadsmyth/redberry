from OpenGL.GL import *

from scene.object3d import Object3D
from opengl.attribute import Attribute


class Mesh(Object3D):
    def __init__(self, geometry, material):
        super().__init__()

        self.geometry = geometry
        self.material = material

        self.visible = True

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        for name, attribute in geometry.attributes.items():
            attribute.associate_variable(material.program, name)
        
        glBindVertexArray(0)


class Geometry:
    def __init__(self):
        self.attributes = {}
        self.vertex_count = None
    

    def add_attribute(self, data_type, name, data):
        self.attributes[name] = Attribute(data_type, data)
    

    def count_vertices(self):
        self.vertex_count = len(list(self.attributes.values())[0].data)


class Rectangle_Geometry(Geometry):
    def __init__(self, width=1, height=1):
        super().__init__()

        p0 = [-width/2, -height/2, 0]
        p1 = [ width/2, -height/2, 0]
        p2 = [-width/2,  height/2, 0]
        p3 = [ width/2,  height/2, 0]

        c0, c1, c2, c3 = [1, 1, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1]

        position_data = [p0, p1, p3, p0, p3, p2]
        color_data = [c0, c1, c3, c0, c3, c2]

        self.add_attribute('vec3', 'vertex_position', position_data)
        self.add_attribute('vec3', 'vertex_color', color_data)
        self.count_vertices()


class Box_Geometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        p0 = [-width/2, -height/2, -depth/2]
        p1 = [ width/2, -height/2, -depth/2]
        p2 = [-width/2,  height/2, -depth/2]
        p3 = [ width/2,  height/2, -depth/2]
        p4 = [-width/2, -height/2,  depth/2]
        p5 = [ width/2, -height/2,  depth/2]
        p6 = [-width/2,  height/2,  depth/2]
        p7 = [ width/2,  height/2,  depth/2]

        # colors for faces in order: x+, x-, y+, y-, z+, z-
        c1, c2 = [1, .5, .5], [.5, 0, 0]
        c3, c4 = [.5, 1, .5], [0, .5, 0]
        c5, c6 = [.5, .5, 1], [0, 0, .5]

        # texture coordinates
        T0, T1, T2, T3 = [0,0], [1,0], [0,1], [1,1]

        position_data = [
            p5,p1,p3,p5,p3,p7, p0,p4,p6,p0,p6,p2,
            p6,p7,p3,p6,p3,p2, p0,p1,p5,p0,p5,p4,
            p4,p5,p7,p4,p7,p6, p1,p0,p2,p1,p2,p3]

        color_data = [c1]*6 + [c2]*6 + [c3]*6 + [c4]*6 + [c5]*6 + [c6]*6

        uv_data = [T0,T1,T3, T0,T3,T2] * 6

        self.add_attribute('vec3', 'vertex_position', position_data)
        self.add_attribute('vec3', 'vertex_color', color_data)
        self.add_attribute('vec2', 'vertex_uv', uv_data)
        self.count_vertices()
