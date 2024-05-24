in vec3 position;
out vec4 frag_color;

void main()
{
    vec3 color = mod(position, 1.0);
    frag_color = vec4(color, 1.0);
}
