precision mediump float;
uniform vec2 u_resolution;
uniform vec2 u_mouse;

void main() {
    vec2 st = gl_FragCoord.xy / u_resolution;
    vec2 mouse_normalized = u_mouse / u_resolution;
    gl_FragColor = vec4(mouse_normalized.x, 0.0, 1.0, 1.0);
}