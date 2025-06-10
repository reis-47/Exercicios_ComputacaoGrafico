precision mediump float;
uniform vec2 u_resolution;

float plota(vec2 st, float pct) {
    float v1 = smoothstep(pct - 0.02, pct, st.y);
    float v2 = smoothstep(pct, pct + 0.02, st.y);
    return v1 - v2;
}

void main() {
    vec2 st = gl_FragCoord.xy / u_resolution;
    float y = st.x;
    float valor = plota(st, y);
    vec3 lineColor = vec3(1.0, 1.0, 0.51);
    vec3 backgroundColor = vec3(0.20, 0.30, 0.60);
    vec3 color = mix(backgroundColor, lineColor, valor);
    gl_FragColor = vec4(color, 1.0);
}