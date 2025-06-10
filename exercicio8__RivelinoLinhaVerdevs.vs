precision mediump float;
uniform vec2 u_resolution;

float plota(vec2 st, float pct) {
    float v1 = smoothstep(pct - 0.2, pct, st.y);
    float v2 = smoothstep(pct, pct + 0.02, st.y);

    return v1 - v2;
}

void main() {
    vec2 st = gl_FragCoord.xy / u_resolution;
    float valor = plota(st, st.x);
    vec3 color = valor * vec3(0.19, 0.90, 01.0);
    gl_FragColor = vec4(color, 1.0);
}