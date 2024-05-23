uniform vec3 base_color;
uniform bool use_vertex_colors;

in vec3 color;
out vec4 frag_color;

void main()
{
    vec4 temp_color = vec4(base_color, 1.0);

    if (use_vertex_colors)
        temp_color *= vec4(color, 1.0);

    frag_color = temp_color;
}