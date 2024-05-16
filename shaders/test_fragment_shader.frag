uniform vec3 base_color;
out vec4 frag_color;

void main()
{
    frag_color = vec4(base_color.r, base_color.g, base_color.b, 1.0);
}
