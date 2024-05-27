from OpenGL.GL import *

from scene.mesh import Mesh


class Renderer:
    def __init__(self, clear_color=(0,0,0)):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_MULTISAMPLE)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        r,g,b = clear_color
        glClearColor(r, g, b, 1)
    

    def render(self, scene, camera):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        camera.update_view_matrix()

        # get all mesh objects in the scene
        meshes = [obj for obj in scene.get_descendants() if isinstance(obj, Mesh)]

        for mesh in meshes:
            if not mesh.visible:
                continue

            glUseProgram(mesh.material.program)
            glBindVertexArray(mesh.vao)

            mesh.material.uniforms['model_matrix'].data = mesh.get_world_matrix()
            mesh.material.uniforms['view_matrix'].data = camera.view_matrix
            mesh.material.uniforms['projection_matrix'].data = camera.projection_matrix

            for uniform in mesh.material.uniforms.values():
                uniform.upload()
            
            glDrawArrays(
                mesh.material.settings['draw_style'],
                0,
                mesh.geometry.vertex_count)
