import pygame
from functions import Naves, Player, Missil
from time import sleep
from random import randint,choice


pygame.init()

#delimitando tamanho da janela
largura = 1300 
altura = 650



#tempo fps
tempo = pygame.time.Clock()
FPS = 60
# som de fundo
som_fundo = pygame.mixer.music.load('sounds/som_fundo.mp3')
pygame.mixer.music.play(-1)

#setando o tamanho da janela e titulo
tela = pygame.display.set_mode((largura,altura ))
pygame.display.set_caption('Space')

#background
bg = pygame.image.load('imagens/background_03.jpg').convert_alpha()
bg = pygame.transform.scale(bg,(largura,altura))

# imagens_inimigos
img_inimigo_1 = 'imagens/nave_2.png'
img_inimigo_2 = 'imagens/nave_3.png'
img_inimigo_3 = 'imagens/nave_4.png'

# imagem do jogador
img_player='imagens/nave_1.png'

#armazenando as sprites num grupo do pygame
todas_sprites = pygame.sprite.Group()
missil_grupo = pygame.sprite.Group()
grupo_player = pygame.sprite.Group()

#loop for para duplicar as imagens


inimigo_2 = Naves(img_inimigo_2, 1300, randint (100, 500), 270, randint (4, 10))
inimigo_3 = Naves(img_inimigo_3, 1300, randint (100, 500), 180, randint (4, 10))
inimigo_1 = Naves(img_inimigo_1,1300,randint (100, 500), 90, randint (4, 10) )
todas_sprites.add(inimigo_1)
todas_sprites.add(inimigo_2)
todas_sprites.add(inimigo_3)
nave_player = Player(img_player, largura - 1200, altura/2)

grupo_player.add(nave_player)

def vida_inimigo():
    for inimigo in todas_sprites:
        # Define as coordenadas iniciais e finais da barra de vida
        x_vida = inimigo.rect.x
        y_vida = inimigo.rect.y - 10
        largura_vida = inimigo.rect.width - 20
        altura_vida = 5
        
        # Calcula a porcentagem de vida restante do inimigo
        porcentagem_vida = inimigo.vida / inimigo.vida_maxima
        
        # Define as cores da barra de vida (branco e vermelho)
        cor_vida_branco = (255, 255, 255)
        cor_vida_vermelho = (255, 255*(1-porcentagem_vida), 255*(1-porcentagem_vida))
        
        # Desenha a barra de vida branca na tela
        pygame.draw.rect(tela, cor_vida_branco, (x_vida, y_vida, largura_vida, altura_vida))
        
        # Desenha a barra de vida vermelha sobre a branca, com base na porcentagem de vida restante do inimigo
        pygame.draw.rect(tela, cor_vida_vermelho, (x_vida, y_vida, largura_vida*porcentagem_vida, altura_vida))

def colisao_missi_e_inimigo(colisoes, placar):
    if colisoes:
        limite_itens = 3
        for missil, inimigos in colisoes.items():
            missil.kill()
            for inimigo in inimigos:
                inimigo.vida -= 50
                if inimigo.vida <= 0:
                    inimigo.kill()
                    placar+=1 
                    if len(todas_sprites) < limite_itens:
                        inimigo_2 = Naves(img_inimigo_2, 1300, randint (100, 500), 270, randint (4, 9))
                        inimigo_3 = Naves(img_inimigo_3, 1300, randint (100, 500), 180, randint (4, 9))
                        inimigo_1 = Naves(img_inimigo_1,1300,randint (100, 500), 90, randint (4, 9) )
                        lista = [inimigo_1, inimigo_2, inimigo_3]
                    
                        todas_sprites.add(lista)
           

     
  
#condição
t = True
tempo_frame = 10
run = True
disparou = True
placar = 0
while run:
    tela.blit(bg,(0,0))
    # desenhar placar
    font = pygame.font.SysFont('Arial', 60)
    text = font.render('Placar', True, (255, 255, 255))
    tela.blit(text, (50, 100))
    contador = font.render(f'{placar}', True, (255, 255, 255))
    tela.blit(contador, (100, 170))
    tempo.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False     
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False 
            if event.key == pygame.K_SPACE:
                nave_player.som_disparo()
                missil_grupo.add(nave_player.criar_missil())

    
    vida_inimigo()
   # colisoes = pygame.sprite.groupcollide(missil_grupo, todas_sprites, True, pygame.sprite.collide_mask)
    colisoes = pygame.sprite.groupcollide(missil_grupo, todas_sprites, False, False, pygame.sprite.collide_mask)
    
    colisao_missi_e_inimigo(colisoes,placar)
    colisao_player = pygame.sprite.spritecollide(nave_player, todas_sprites, True, pygame.sprite.collide_mask)
    
        
    grupo_player.draw(tela)
    todas_sprites.draw(tela)
    missil_grupo.draw(tela)
    grupo_player.update()
    missil_grupo.update()
    todas_sprites.update()
    pygame.display.update()