import pygame

pygame.init()

largura, altura = 400, 300

tela = pygame.display.set_mode((largura, altura))

branca = (255, 255, 255)
vermelho = (255, 0, 0)
x, y = largura//2, altura//2
tamanho = 30
velocidade = 3

carregando = True
while carregando:
    for evento in pygame.event.get():
        if evento.type == pygame.quit:
            carregando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        x = x - velocidade
    if teclas[pygame.K_RIGHT]:
        x+=velocidade
    if teclas[pygame.K_UP]:
        y-=velocidade
    if teclas[pygame.K_DOWN]:
        y+=velocidade

    tela.fill(branca)

    pygame.draw.rect(tela, vermelho, (x, y, tamanho, tamanho))

    pygame.display.flip()

    pygame.time.Clock().tick(30)


pygame.quit()
