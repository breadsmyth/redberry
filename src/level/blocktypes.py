blocktypes = {}

class Block:
    def __init__(self, name, texture):
        self.name = name
        self.texture = texture


    def render(self):
        pass


blocktypes['base.dirt'] = Block('base.dirt', 'textures/dirt.png')
blocktypes['base.grass'] = Block('base.grass', 'textures/grass.png')
blocktypes['base.stone'] = Block('base.stone', 'textures/stone.png')
