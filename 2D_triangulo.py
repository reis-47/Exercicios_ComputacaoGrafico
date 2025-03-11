import pygame  # Importa a biblioteca Pygame para gerenciar gráficos e entrada do usuário
from pygame.locals import *  # Importa constantes do Pygame para eventos de teclado e mouse
from OpenGL.GL import *  # Importa funções do OpenGL para renderização gráfica
from OpenGL.GLUT import *  # Importa GLUT para utilitários gráficos do OpenGL
from OpenGL.GLU import *  # Importa GLU para operações gráficas auxiliares

# Variáveis de posição do triângulo
x = 0  # Posição inicial no eixo X
y = 0  # Posição inicial no eixo Y
r = 0  # Ângulo de rotação do triângulo

# Variáveis de escala (tamanho do triângulo)
ex = 2  # Escala no eixo X
ey = 2  # Escala no eixo Y
ez = 2  # Escala no eixo Z (afeta o zoom)

# Controle de zoom (posição no eixo Z)
zoom = -6  # Distância inicial do triângulo

# Função de inicialização do OpenGL
def init():
    glClearColor(1, 1, 1, 1)  # Define a cor de fundo branco (R=1, G=1, B=1, A=1)
    glClearDepth(1.0)  # Define a profundidade máxima para renderização
    glEnable(GL_DEPTH_TEST)  # Habilita o teste de profundidade para ocultação de objetos
    glDepthFunc(GL_LEQUAL)  # Define o tipo de teste de profundidade
    glShadeModel(GL_SMOOTH)  # Habilita sombreamento suave
    glMatrixMode(GL_PROJECTION)  # Define a matriz de projeção (perspectiva)
    glLoadIdentity()  # Reinicializa a matriz de projeção
    gluPerspective(45, 640/480, 0.1, 100)  # Configuração da perspectiva
    glMatrixMode(GL_MODELVIEW)  # Define a matriz de visualização

# Função para desenhar o triângulo
def draw():
    glLoadIdentity()  # Reinicia a matriz de visualização

    # Aplica transformações (movimentação, rotação e escala)
    glTranslatef(x, y, zoom)  # Aplica o zoom com base na variável global
    glRotatef(r, 1, 1, 0)  
    glScalef(ex, ey, ez)  

    # Desenha o triângulo
    glBegin(GL_TRIANGLES)
    glColor3f(0, 0, 0)  # Cor preta
    glVertex3f(4, 5, 4)  
    glVertex3f(-5, -5, 4)  
    glVertex3f(5, -5, 4)  
    glEnd()  

# Função principal do programa
def main():
    pygame.init()  # Inicializa o Pygame
    pygame.display.set_mode((640, 480), DOUBLEBUF | OPENGL)  
    init()  # Inicializa o OpenGL

    global x, y, r, ex, ey, ez, zoom  # Declara as variáveis globais

    running = True  
    while running:
        for event in pygame.event.get():  # Captura eventos
            if event.type == pygame.QUIT:  # Fecha a janela
                running = False  
            if event.type == KEYDOWN:  # Se uma tecla for pressionada
                if event.key == K_ESCAPE:
                    running = False  
                if event.key == K_d:  
                    x += -0.2  
                if event.key == K_a:  
                    x += 0.2  
                if event.key == K_w:  
                    y += 0.2  
                if event.key == K_s:  
                    y += -0.2  
                if event.key == K_z:  # Aproxima o triângulo
                    zoom += 0.2  
                if event.key == K_x:  # Afasta o triângulo
                    zoom -= 0.2  

            if event.type == MOUSEBUTTONDOWN:  # Zoom com rolagem do mouse
                if event.button == 4:  # Scroll para cima
                    ex += 0.2  
                    ey += 0.2  
                    ez += 0.2  
                if event.button == 5:  # Scroll para baixo
                    ex -= 0.2  
                    ey -= 0.2  
                    ez -= 0.2  

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpa a tela
        draw()  # Desenha o triângulo
        pygame.display.flip()  # Atualiza a tela
        pygame.time.wait(10)  # Pequena pausa

        r -= 10  # Atualiza a rotação

    pygame.quit()  # Fecha o Pygame

# Executa o programa
if __name__ == "__main__":
    main()
