import math
from OpenGL.GL import *

import opengl.shaders
from opengl.attribute import Attribute
from opengl.uniform import Uniform
from opengl import matrix

import config
import input


def init():
    # Get shaders
    with open('shaders/3d_shader.vert') as file:
        vert_code = file.read()
    with open('shaders/3d_shader.frag') as file:
        frag_code = file.read()


    global program
    program = opengl.shaders.compile(vert_code, frag_code)
    # glPointSize(10)
    # glLineWidth(4)
    glClearColor(.4, .7, .9, 1)
    glEnable(GL_DEPTH_TEST)


    # triangle data
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    pos_data = (
        (0, .2, 0),
        (.1, -.2, 0),
        (-.1, -.2, 0))

    global vertex_count
    vertex_count = len(pos_data)
    pos_attr = Attribute('vec3', pos_data)
    pos_attr.associate_variable(program, 'position')


    # uniforms
    global model_matrix
    model_matrix = Uniform('mat4', matrix.translate(0, 0, -1))
    model_matrix.locate_variable(program, 'model_matrix')

    global projection_matrix
    projection_matrix = Uniform('mat4', matrix.perspective())
    projection_matrix.locate_variable(program, 'projection_matrix')


    # speed
    global move_speed  # units per second
    move_speed = .5
    global turn_speed  # radians per second
    turn_speed = 90 * (math.pi / 180)


def run():
    # update game state
    move_amount = move_speed * config.DELTA_TIME
    turn_amount = turn_speed * config.DELTA_TIME

    # global translation
    if input.is_key_pressed('w'):
        model_matrix.data = matrix.translate(0, move_amount, 0) @ model_matrix.data
    if input.is_key_pressed('a'):
        model_matrix.data = matrix.translate(-move_amount, 0, 0) @ model_matrix.data
    if input.is_key_pressed('s'):
        model_matrix.data = matrix.translate(0, -move_amount, 0) @ model_matrix.data
    if input.is_key_pressed('d'):
        model_matrix.data = matrix.translate(move_amount, 0, 0) @ model_matrix.data
    if input.is_key_pressed('z'):
        model_matrix.data = matrix.translate(0, 0, move_amount) @ model_matrix.data
    if input.is_key_pressed('x'):
        model_matrix.data = matrix.translate(0, 0, -move_amount) @ model_matrix.data

    # global rotation (around the origin)
    if input.is_key_pressed('q'):
        model_matrix.data = matrix.rotate_z(turn_amount) @ model_matrix.data
    if input.is_key_pressed('e'):
        model_matrix.data = matrix.rotate_z(-turn_amount) @ model_matrix.data

    # local translation
    if input.is_key_pressed('i'):
        model_matrix.data = model_matrix.data @ matrix.translate(0, move_amount, 0)
    if input.is_key_pressed('k'):
        model_matrix.data = model_matrix.data @ matrix.translate(0, -move_amount, 0)
    if input.is_key_pressed('j'):
        model_matrix.data = model_matrix.data @ matrix.translate(-move_amount, 0, 0)
    if input.is_key_pressed('l'):
        model_matrix.data = model_matrix.data @ matrix.translate(move_amount, 0, 0)

    # local rotation (around object center)
    if input.is_key_pressed('u'):
        model_matrix.data = model_matrix.data @ matrix.rotate_z(turn_amount)
    if input.is_key_pressed('o'):
        model_matrix.data = model_matrix.data @ matrix.rotate_z(-turn_amount)



    # render scene
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glUseProgram(program)

    projection_matrix.upload()
    model_matrix.upload()
    glDrawArrays(GL_TRIANGLES, 0, vertex_count)
