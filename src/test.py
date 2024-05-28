from math import pi

import config
from materials.mat_texture import Mat_Texture
from materials.mat_sky import Mat_Sky
from opengl.texture import Texture
from scene import obj_loader
from scene.renderer import Renderer
from scene.camera import Camera
from scene.material import Material
from scene.mesh import Mesh, Box_Geometry
from scene.misc import Scene
from scene.movement_rig import Movement_Rig


def init():
    global renderer
    global scene
    global camera

    renderer = Renderer(clear_color=(0, 0, 0))
    scene = Scene()
    camera = Camera(
        angle_of_view=config.FOV,
        aspect_ratio=config.ASPECT_RATIO,
        near=0.1,
        far=1000)

    global rig
    rig = Movement_Rig(move_speed=5)
    rig.add(camera)
    rig.set_position([0, 1.7, 8])
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

    cube = Box_Geometry()
    texture = Texture('textures/test.png')
    cube_material = Mat_Texture(texture)

    cube_mesh = Mesh(cube, cube_material)
    cube_mesh.translate(-4, 0, 0)
    scene.add(cube_mesh)

    big_cube = Mesh(cube, cube_material)
    big_cube.scale(10)
    big_cube.translate(1, 0.5, -1)
    big_cube.rotate_y(15)
    scene.add(big_cube)

    grass = Box_Geometry(width=100, height=1, depth=100)
    grass_texture = Texture('textures/grass.png')
    grass_material = Mat_Texture(grass_texture, {'uv_repeat': [100, 100]})
    grass_mesh = Mesh(grass, grass_material)
    grass_mesh.translate(0, -1, 0)
    scene.add(grass_mesh)

    global sky_material
    sky = Box_Geometry(width=200, height=200, depth=200)
    sky_material = Mat_Sky()
    sky_mesh = Mesh(sky, sky_material)
    sky_mesh.rotate_y(pi / 2)
    scene.add(sky_mesh)

def run():
    # update game state
    mesh.rotate_y(0.01)

    rig.update()
    # update sky mesh (is there a better way to do this? TODO)
    sky_material.uniforms['time'].data = config.TOTAL_TIME
    renderer.render(scene, camera)
