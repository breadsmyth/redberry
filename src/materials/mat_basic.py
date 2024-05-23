from scene.material import Material


class Mat_Basic(Material):
    def __init__(self):
        with open('shaders/basic.vert') as file:
            vert_code = file.read()
        with open('shaders/basic.frag') as file:
            frag_code = file.read()
        
        super().__init__(vert_code, frag_code)

        self.add_uniform('vec3', 'base_color', [1, 1, 1])
        self.add_uniform('bool', 'use_vertex_colors', False)
        self.locate_uniforms()
