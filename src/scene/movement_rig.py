from math import pi

import config
import input
from scene.object3d import Object3D


class Movement_Rig(Object3D):
    def __init__(self, move_speed):
        super().__init__()

        self.look_attachment = Object3D()
        self.children = [self.look_attachment]
        self.look_attachment.parent = self
        self.move_speed = move_speed

        # this keeps track of how far our pitch is
        self.total_pitch = 0

        # key mappings
        self.KEY_MOVE_FORWARDS  = 'w'
        self.KEY_MOVE_LEFT      = 'a'
        self.KEY_MOVE_BACKWARDS = 's'
        self.KEY_MOVE_RIGHT     = 'd'

        input.capture_mouse()


    def add(self, child):
        self.look_attachment.add(child)
    

    def remove(self, child):
        self.look_attachment.remove(child)
    

    def update(self):
        pos_delta = self.move_speed * config.DELTA_TIME

        if input.is_key_pressed(self.KEY_MOVE_FORWARDS):
            self.translate(0, 0, -pos_delta)
        if input.is_key_pressed(self.KEY_MOVE_LEFT):
            self.translate(-pos_delta, 0, 0)
        if input.is_key_pressed(self.KEY_MOVE_BACKWARDS):
            self.translate(0, 0, pos_delta)
        if input.is_key_pressed(self.KEY_MOVE_RIGHT):
            self.translate(pos_delta, 0, 0)

        # mouse rotation
        dx, dy = input.get_mouse_delta()
        ROTATION_SCALE_FACTOR = 100 / config.MOUSE_SENSITIVITY  # magic number
        PITCH_LIMIT = pi / 2

        yaw = dx / ROTATION_SCALE_FACTOR
        pitch = dy / ROTATION_SCALE_FACTOR

        # clamp pitch to be between +PITCH_LIMIT and -PITCH_LIMIT
        self.total_pitch += pitch

        if self.total_pitch >= PITCH_LIMIT:
            pitch -= (self.total_pitch - PITCH_LIMIT)
            self.total_pitch = PITCH_LIMIT

        if self.total_pitch <= -PITCH_LIMIT:
            pitch -= (self.total_pitch + PITCH_LIMIT)
            self.total_pitch = -PITCH_LIMIT
        
        # for pitch rotations, only rotate the look_attachment so that
        # we still move relative to the ground even while looking
        # straight up at the sky, as we expect to
        self.look_attachment.rotate_x(-pitch)
        self.rotate_y(-yaw)

