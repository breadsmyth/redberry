in vec3 position;
uniform float time;
uniform float day_length;
uniform float sunset_length;
out vec4 frag_color;

float lerp(float v0, float v1, float t)
{
    return (1 - t) * v0 + t * v1;
}

void main()
{
    float current_cycle_time = mod(time, day_length);
    float half_day = day_length / 2.0;
    float alpha;

    // Set alpha based on what time of day it is
    if (current_cycle_time < half_day - sunset_length)
    {
        // Daytime
        alpha = 0;
    }

    else if (current_cycle_time < half_day)
    {
        // Sunset
        alpha = (current_cycle_time - (half_day - sunset_length)) / sunset_length;
    }

    else if (current_cycle_time < day_length - sunset_length)
    {
        // Nighttime
        alpha = 1;
    }
    else
    {
        // Sunrise
        alpha = (day_length - current_cycle_time) / sunset_length;
    }

    float tmp_r = clamp(lerp(.5, 0, position.y / 60), 0, .5);
    float r = lerp(tmp_r, tmp_r/8.0, alpha);
    float g = lerp(.7, 0, alpha);
    float b = lerp(1, .1, alpha);

    frag_color = vec4(
        clamp(r, 0, .5),
        clamp(g, 0, .7),
        clamp(b, .1, 1),
        1);
}