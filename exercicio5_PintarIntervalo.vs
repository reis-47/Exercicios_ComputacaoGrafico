precision mediump float;
uniform vec2 u_resolution;
void main() {
    vec2 st = gl_FragCoord.xy / u_resolution.xy;
    vec3 color = vec3(1.0, 0.40, 1.0);

    if(st.x > 0.10 && st.x < 0.50){
        color = vec3(1.0);
    }
    gl_FragColor = vec4(color, 1.0);
}