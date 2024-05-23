from numpy.linalg import inv

from scene.object3d import Object3D
from opengl import matrix


class Camera(Object3D):
    def __init__(self,
                 angle_of_view,
                 aspect_ratio,
                 near,
                 far):
        super().__init__()

        self.projection_matrix = matrix.perspective(
            angle_of_view,
            aspect_ratio,
            near,
            far)
        self.view_matrix = matrix.identity()
    

    def update_view_matrix(self):
        self.view_matrix = inv(self.get_world_matrix())
