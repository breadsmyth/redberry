in vec3 vertex_position;
out vec3 position;
uniform mat4 model_matrix;
uniform mat4 view_matrix;
uniform mat4 projection_matrix;

void main()
{
    vec4 pos = vec4(vertex_position, 1.0);
    gl_Position = projection_matrix * view_matrix * model_matrix * pos;
    position = vertex_position;
}
