from level.blocktypes import blocktypes
from materials.mat_texture import Mat_Texture
from scene.mesh import Mesh, Box_Geometry
from scene.misc import Group
from opengl.texture import Texture


materials_cache = {}

def add_to_scene(level, scene):
    for chunk_key, chunk in level['chunks'].items():
        chunk_x_str, chunk_y_str = chunk_key.split(',')
        chunk_x = int(chunk_x_str)
        chunk_y = int(chunk_y_str)

        cur_chunk = Group()

        for block_key, block_index in chunk.items():
            block_x_str, block_y_str, block_z_str = block_key.split(',')
            block_x = int(block_x_str)
            block_y = int(block_y_str)
            block_z = int(block_z_str)

            block_name = level['block_dict'][block_index]

            block = blocktypes[block_name]

            # add material to cache
            if block_name not in materials_cache.keys():
                materials_cache[block_name] = Mat_Texture(Texture(block.texture))

            block_mesh = Mesh(Box_Geometry(), materials_cache[block_name])

            block_mesh.translate(block_x, block_y, block_z)
            cur_chunk.add(block_mesh)
        
        cur_chunk.translate(chunk_x*16, 0, chunk_y*16)
        scene.add(cur_chunk)
