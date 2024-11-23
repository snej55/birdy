#version 330 core
        uniform sampler2D tex;
        uniform sampler2D noise;
        uniform float time;

        uniform float timeScale = 0.0001;
        uniform float angleConst = 1.5;
uniform float stripeImpact = 0.03;
uniform float stripeWidth = 60;
uniform float threshold = 0.43; // size of hole

        in vec2 uvs;
        out vec4 f_color;

        void main() {
            vec2 texCoords = vec2(uvs.x, uvs.y);  // can be used to warp screen
    vec2 noise_offset = vec2(texture(noise, vec2(texCoords.x, texCoords.y - time * timeScale)).r) * 0.5; 
            vec3 mult = texture(noise, uvs + (time * 0.001)).rgb;
            vec4 baseColor;
            vec2 shiftTexcoords = vec2(texCoords.x + sin(time * 0.2 * timeScale), texCoords.y * 2.0 - sin(time * 0.02 * timeScale));
            vec3 color1 = texture(noise, shiftTexcoords).rgb;
            shiftTexcoords = vec2(texCoords.x * 2.7 - sin(time * 0.05 * timeScale), texCoords.y * 1.7 - sin(time * 0.5 * timeScale)); // and here
            vec3 color2 = texture(noise, shiftTexcoords).rgb;
             shiftTexcoords = vec2(texCoords.x * 0.35 - sin(time * 0.4 * timeScale), texCoords.y * 0.35 - sin(time * 0.4 * timeScale)); // here as well
    vec3 color3 = texture(noise, shiftTexcoords).rgb;
    vec4 combinedColor = vec4(vec3((color1 + color2 * 0.5 + color3 * 0.5) * 0.5), 1.0);
    combinedColor = combinedColor * (distance(vec2(0.5, 0.5), texCoords) * 0.5 + 0.5) + sin((texCoords.x - texCoords.y * angleConst) * stripeWidth) * stripeImpact;
             if (combinedColor.r < threshold + 0.01) {
        baseColor = vec4(0.27450980392156865, 0.3568627450980392, 0.9058823529411765, 1.0);  // different colors
    } else if (combinedColor.r < threshold + 0.02) {
        baseColor = vec4(0.27450980392156865, 0.3568627450980392, 0.9058823529411765, 1.0);
    } else if (combinedColor.r < threshold + 0.05) {
        baseColor = vec4(0.13333333333333333, 0.17647058823529413, 0.5058823529411764, 1.0);
    } else if (combinedColor.r < threshold + 0.1) {
        baseColor = vec4(0.10588235294117647, 0.09411764705882353, 0.3254901960784314, 1.0);
    } else {
        baseColor = vec4(0.054901960784313725, 0.03529411764705882, 0.1843137254901961, 1.0);
    }
    
            f_color = vec4(texture(tex, uvs).rgb + combinedColor.rgb + mult, 1.0);
        }