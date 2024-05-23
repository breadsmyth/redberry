uniform mat4 projection_matrix;
uniform mat4 view_matrix;
uniform mat4 model_matrix;

in vec3 vertex_position;
in vec3 vertex_color;
out vec3 color;

void main()
{
    gl_Position = projection_matrix * view_matrix * model_matrix * vec4(vertex_position, 1.0);
    color = vertex_color;
}