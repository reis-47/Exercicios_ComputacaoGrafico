#ifdef GL_ES
precision mediump float;
#endif

uniform float u_time;

void main() {
    float pulso = abs(sin(u_time));
    gl_FragColor = vec4(pulso, 0.0, 0.0, 1.0);
}