from scene.mesh import Geometry


def load(filename) -> Geometry:
    with open(filename) as file:
        lines = file.readlines()
    
    vertices = []
    faces = []
    for line in lines:
        if line.startswith('v'):
            nums = line.split()
            vertices.append([float(n) for n in nums[1:]])

        elif line.startswith('f'):
            points = line.split()
            faces.append([int(p) for p in points[1:]])
    
    pos_data = []
    for face in faces:
        pos_data += [vertices[p-1] for p in face]
    
    # create the geometry
    geometry = Geometry()
    geometry.add_attribute('vec3', 'vertex_position', pos_data)
    geometry.count_vertices()

    return geometry
