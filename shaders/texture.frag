uniform vec3 base_color;
uniform sampler2D texture;

in vec2 uv;
out vec4 frag_color;

void main()
{
    vec4 color = vec4(base_color, 1.0) * texture2D(texture, uv);
    if (color.a < 0.1)
        discard;

    frag_color = color;
}
