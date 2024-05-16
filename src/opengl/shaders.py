from OpenGL.GL import *


def compile_shader(shader_code, shader_type):
    shader_code = '#version 330\n' + shader_code

    shader = glCreateShader(shader_type)
    glShaderSource(shader, shader_code)
    glCompileShader(shader)

    # was compilation successful?
    success = glGetShaderiv(shader, GL_COMPILE_STATUS)
    if not success:
        error_msg = glGetShaderInfoLog(shader)
        glDeleteShader(shader)
        error_msg = '\n' + error_msg.decode('utf-8')
        raise Exception(error_msg)
    
    return shader


def compile(vert_code, frag_code):
    vert_shader = compile_shader(vert_code, GL_VERTEX_SHADER)
    frag_shader = compile_shader(frag_code, GL_FRAGMENT_SHADER)

    program = glCreateProgram()

    glAttachShader(program, vert_shader)
    glAttachShader(program, frag_shader)

    glLinkProgram(program)

    # was link successful?
    success = glGetProgramiv(program, GL_LINK_STATUS)
    if not success:
        error_msg = glGetProgramInfoLog(program)
        glDeleteProgram(program)
        # error_msg = '\n' + error_msg.decode('utf-8')
        raise Exception(error_msg)

    return program


def print_info():
    print('  Vendor: ' + glGetString(GL_VENDOR).decode('utf-8'))
    print('Renderer: ' + glGetString(GL_RENDERER).decode('utf-8'))
    print('OpenGL version supported: ' + glGetString(GL_VERSION).decode('utf-8'))
    print('  GLSL version supported: ' + glGetString(GL_SHADING_LANGUAGE_VERSION).decode('utf-8'))
