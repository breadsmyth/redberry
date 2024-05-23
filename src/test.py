import config
from scene.renderer import Renderer
from scene.camera import Camera
from scene.mesh import Mesh, Box_Geometry
from scene.misc import Scene
from materials.mat_surface import Mat_Surface


def init():
    global renderer
    global mesh
    global scene
    global camera

    renderer = Renderer()
    scene = Scene()
    camera = Camera(
        angle_of_view=config.FOV,
        aspect_ratio=config.ASPECT_RATIO,
        near=0.1,
        far=1000)
    camera.set_position([0, 0, 4])

    box = Box_Geometry()
    mat = Mat_Surface({'use_vertex_colors': True})
    mesh = Mesh(box, mat)
    scene.add(mesh)


def run():
    # update game state
    mesh.rotate_y(0.0514)
    mesh.rotate_x(0.0337)

    renderer.render(scene, camera)
