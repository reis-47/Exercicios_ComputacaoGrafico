precision mediump float;
uniform vec2 u_resolution;

void main() {
    vec2 st = gl_FragCoord.xy / u_resolution;
    float res = step(0.3, st.x);
    vec3 color = vec3(res); 
    gl_FragColor = vec4(color, 0.20);
}