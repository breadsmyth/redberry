from opengl import matrix


class Object3D:
    def __init__(self):
        self.transform = matrix.identity()
        self.parent = None
        self.children = []
    

    def add(self, child):
        self.children.append(child)
        child.parent = self
    

    def remove(self, child):
        self.children.remove(child)
        child.parent = None

    
    def get_world_matrix(self):
        if self.parent is None:
            return self.transform

        return self.parent.get_world_matrix() @ self.transform
    

    def get_descendants(self):
        descendants = []
        to_process = [self]

        while len(to_process) > 0:
            node = to_process.pop(0)
            descendants.append(node) 

            to_process = node.children + to_process
        
        return descendants


    def apply_transform(self, matrix, local=True):
        if local:
            self.transform = self.transform @ matrix
        else:
            self.transform = matrix @ self.transform
    

    def translate(self, x, y, z, local=True):
        self.apply_transform(
            matrix.translate(x, y, z),
            local)
    

    def rotate_x(self, angle, local=True):
        self.apply_transform(
            matrix.rotate_x(angle),
            local)
    

    def rotate_y(self, angle, local=True):
        self.apply_transform(
            matrix.rotate_y(angle),
            local)
    

    def rotate_z(self, angle, local=True):
        self.apply_transform(
            matrix.rotate_z(angle),
            local)


    def scale(self, n, local=True):
        self.apply_transform(
            matrix.scale(n),
            local)


    def get_position(self):
        'returns position relative to parent'
        return [
            self.transform.item((0, 3)),
            self.transform.item((1, 3)),
            self.transform.item((2, 3))]
    
    
    def get_world_position(self):
        'returns global (absolute) position'
        world_transform = self.get_world_matrix()
        return [
            world_transform.item((0, 3)),
            world_transform.item((1, 3)),
            world_transform.item((2, 3))]

    
    def set_position(self, position):
        self.transform.itemset((0, 3), position[0])
        self.transform.itemset((1, 3), position[1])
        self.transform.itemset((2, 3), position[2])
