uniform mat4 projection_matrix;
uniform mat4 view_matrix;
uniform mat4 model_matrix;

uniform vec2 uv_repeat;
uniform vec2 uv_offset;

in vec3 vertex_position;
in vec2 vertex_uv;
out vec2 uv;

void main()
{
    gl_Position = projection_matrix * view_matrix * model_matrix * vec4(vertex_position, 1.0);
    uv = vertex_uv * uv_repeat + uv_offset;
}
