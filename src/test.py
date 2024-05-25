import config
from scene import obj_loader
from scene.renderer import Renderer
from scene.camera import Camera
from scene.material import Material
from scene.mesh import Mesh
from scene.misc import Scene
from scene.movement_rig import Movement_Rig


def init():
    global renderer
    global scene
    global camera

    renderer = Renderer()
    scene = Scene()
    camera = Camera(
        angle_of_view=config.FOV,
        aspect_ratio=config.ASPECT_RATIO,
        near=0.1,
        far=1000)

    global rig
    rig = Movement_Rig(move_speed=5)
    rig.add(camera)
    rig.set_position([0, 1.5, 8])
    scene.add(rig)

    model = obj_loader.load('models/teapot.obj')

    with open('shaders/point.vert') as file:
        vert_code = file.read()
    with open('shaders/point.frag') as file:
        frag_code = file.read()

    material = Material(vert_code, frag_code)
    material.locate_uniforms()

    global mesh
    mesh = Mesh(model, material)
    scene.add(mesh)


def run():
    # update game state
    mesh.rotate_y(0.01)

    rig.update()
    renderer.render(scene, camera)
