precision mediump float;
uniform vec2 u_resolution;
float plota(vec2 st) {
    return smoothstep(0.2, 0.9, st.x);
}
void main() {
    vec2 st = gl_FragCoord.xy / u_resolution;
    float pct = plota(st);
    vec3 color = pct * vec3(0.40, 0.570, 1.0);
    gl_FragColor = vec4(color, 1.0);
}