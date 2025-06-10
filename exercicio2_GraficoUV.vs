#ifdef GL_ES
// Em ambientes WebGL/GL ES, precisamos declarar a precisão de floats.
// Aqui usamos precisão média (“mediump”), o suficiente para a maioria dos efeitos.
precision mediump float;
#endif

// Uniform injetado pela aplicação (ou pelo glsl-canvas) contendo
// a resolução da viewport em pixels: (largura, altura)
uniform vec2 u_resolution;

void main() {
    vec2 st = gl_FragCoord.xy / u_resolution;
    gl_FragColor = vec4(st.x, st.y, 0.0, 1.0);
}