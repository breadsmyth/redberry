from OpenGL.GL import *

import util.opengl
from util.attribute import Attribute
from util.uniform import Uniform


def init():
    # Get shaders
    with open('shaders/test_vertex_shader.vert') as file:
        vert_code = file.read()
    with open('shaders/test_fragment_shader.frag') as file:
        frag_code = file.read()


    global program
    program = util.opengl.compile(vert_code, frag_code)
    # glPointSize(10)
    # glLineWidth(4)
    glClearColor(.4, .7, .9, 1)


    # triangle data
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    pos_data = (
        (0, .2, 0),
        (.2, -.2, 0),
        (-.2, -.2, 0))

    global vertex_count
    vertex_count = len(pos_data)
    pos_attr = Attribute('vec3', pos_data)
    pos_attr.associate_variable(program, 'position')


    # uniforms
    global translation
    translation = Uniform('vec3', [-.5, 0, 0])
    translation.locate_variable(program, 'translation')

    global base_color
    base_color = Uniform('vec3', (1, 0, 0))
    base_color.locate_variable(program, 'base_color')


def test():
    # update game state
    translation.data[0] += .01
    if translation.data[0] > 1.2:
        translation.data[0] = -1.2

    # render scene
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glUseProgram(program)

    translation.upload()
    base_color.upload()
    glDrawArrays(GL_TRIANGLES, 0, vertex_count)
