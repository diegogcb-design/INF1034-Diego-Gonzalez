import pygame, sys, os
from pygame.locals import QUIT

pygame.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Atividade 12")
clock = pygame.time.Clock()

pasta = os.path.dirname(__file__)

# tileset
tileset = pygame.image.load(
    os.path.join(
        pasta,
        "GandalfHardcore FREE Platformer Assets",
        "Floor Tiles1.png"
    )
).convert_alpha()

# pasta do personagem
pasta_personagem = os.path.join(
    pasta,
    "GandalfHardcore Character Asset Pack"
)

# partes do personagem
skin = pygame.image.load(
    os.path.join(
        pasta_personagem,
        "Character skin colors",
        "Male Skin1.png"
    )
).convert_alpha()

hair = pygame.image.load(
    os.path.join(
        pasta_personagem,
        "Male Hair",
        "Male Hair1.png"
    )
).convert_alpha()

shirt = pygame.image.load(
    os.path.join(
        pasta_personagem,
        "Male Clothing",
        "Shirt.png"
    )
).convert_alpha()

pants = pygame.image.load(
    os.path.join(
        pasta_personagem,
        "Male Clothing",
        "Pants.png"
    )
).convert_alpha()

shoes = pygame.image.load(
    os.path.join(
        pasta_personagem,
        "Male Clothing",
        "Shoes.png"
    )
).convert_alpha()


tile_size = 64

# jogador
pos_x = 100
pos_y = 100

largura_jogador = 40
altura_jogador = 55

velocidade = 0.25

# pulo
vel_y = 0
gravidade = 0.0015
forca_pulo = -0.65

no_chao = False
direita = True

# sprite
frame_largura = 64
frame_altura = 64


# antes o mapa estava direto no código
# mapa = [
#     "XXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXX",
#     "XXXXXXXXXGGXXX",
#     "XXXXXXXXXXXXXX",
#     "XXXXXGGXXXXXXX",
#     "XXXXXXXXXXXXXX",
#     "GGGGGGGGGGGGGG",
#     "GGGGGGGGGGGGGG",
# ]


# agora o mapa vem do txt
with open(os.path.join(pasta, "mapa.txt"), "r") as arquivo:
    mapa = [linha.strip() for linha in arquivo]


# antes fazíamos um if para cada letra
# if mapa[i][j] == "G":
#     screen.blit(
#         tileset,
#         (j * tile_size, i * tile_size),
#         (0, 0, tile_size, tile_size)
#     )

# agora os cortes ficam no dicionário
tiles = {
    "G": (0, 0, 64, 64),
    "T": (64, 0, 64, 64),
    "P": (128, 0, 64, 64)
}

# blocos que têm colisão
blocos_solidos = ["G", "T", "P"]

# camera
camera_x = 0


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    dt = clock.get_time()

    keys = pygame.key.get_pressed()

    andando = False


    # movimento horizontal
    old_pos_x = pos_x

    if keys[pygame.K_RIGHT]:
        pos_x += velocidade * dt
        direita = True
        andando = True

    elif keys[pygame.K_LEFT]:
        pos_x -= velocidade * dt
        direita = False
        andando = True


    collider_jogador = pygame.Rect(
        int(pos_x),
        int(pos_y),
        largura_jogador,
        altura_jogador
    )


    # colisão horizontal
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):

            if mapa[i][j] in blocos_solidos:

                collider_tile = pygame.Rect(
                    j * tile_size,
                    i * tile_size,
                    tile_size,
                    tile_size
                )

                if collider_jogador.colliderect(collider_tile):

                    pos_x = old_pos_x

                    collider_jogador = pygame.Rect(
                        int(pos_x),
                        int(pos_y),
                        largura_jogador,
                        altura_jogador
                    )


    # pulo
    if keys[pygame.K_SPACE] and no_chao:
        vel_y = forca_pulo
        no_chao = False


    # gravidade
    vel_y += gravidade * dt
    pos_y += vel_y * dt

    collider_jogador = pygame.Rect(
        int(pos_x),
        int(pos_y),
        largura_jogador,
        altura_jogador
    )

    no_chao = False


    # colisão vertical
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):

            if mapa[i][j] in blocos_solidos:

                collider_tile = pygame.Rect(
                    j * tile_size,
                    i * tile_size,
                    tile_size,
                    tile_size
                )

                if collider_jogador.colliderect(collider_tile):

                    # caindo
                    if vel_y > 0:
                        pos_y = i * tile_size - altura_jogador
                        vel_y = 0
                        no_chao = True

                    # bateu por baixo
                    elif vel_y < 0:
                        pos_y = i * tile_size + tile_size
                        vel_y = 0

                    collider_jogador = pygame.Rect(
                        int(pos_x),
                        int(pos_y),
                        largura_jogador,
                        altura_jogador
                    )


    # tamanho do mapa
    largura_mapa = len(mapa[0]) * tile_size


    # não sair do começo
    if pos_x < 0:
        pos_x = 0


    # não sair do final
    if pos_x + largura_jogador > largura_mapa:
        pos_x = largura_mapa - largura_jogador


    # camera segue o jogador
    camera_x = pos_x - 450


    # limite esquerdo da camera
    if camera_x < 0:
        camera_x = 0


    # limite direito da camera
    if camera_x > largura_mapa - 900:
        camera_x = largura_mapa - 900


    # caso o mapa seja menor que a tela
    if camera_x < 0:
        camera_x = 0


    # fundo
    screen.fill((120, 180, 220))


    # desenhar mapa
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):

            letra = mapa[i][j]

            if letra in tiles:

                screen.blit(
                    tileset,
                    (
                        j * tile_size - camera_x,
                        i * tile_size
                    ),
                    tiles[letra]
                )


    # animação do personagem
    if andando:

        # correndo
        frame_y = 128
        frame = (pygame.time.get_ticks() // 120) % 8
        frame_x = frame * 80

    else:

        # parado
        frame_y = 0
        frame = (pygame.time.get_ticks() // 200) % 5
        frame_x = frame * 80


    # juntar as partes do personagem
    personagem = pygame.Surface(
        (frame_largura, frame_altura),
        pygame.SRCALPHA
    )


    # pele
    personagem.blit(
        skin,
        (0, 0),
        (
            frame_x,
            frame_y,
            frame_largura,
            frame_altura
        )
    )


    # calça
    personagem.blit(
        pants,
        (0, 0),
        (
            frame_x,
            frame_y,
            frame_largura,
            frame_altura
        )
    )


    # camisa
    personagem.blit(
        shirt,
        (0, 0),
        (
            frame_x,
            frame_y,
            frame_largura,
            frame_altura
        )
    )


    # sapatos
    personagem.blit(
        shoes,
        (0, 0),
        (
            frame_x,
            frame_y,
            frame_largura,
            frame_altura
        )
    )


    # cabelo
    personagem.blit(
        hair,
        (0, 0),
        (
            frame_x,
            frame_y,
            frame_largura,
            frame_altura
        )
    )


    # antes estava assim:
    # if not direita:
    #     personagem = pygame.transform.flip(
    #         personagem,
    #         True,
    #         False
    #     )

    # o sprite original olha para esquerda
    # então viramos quando anda para direita
    if direita:
        personagem = pygame.transform.flip(
            personagem,
            True,
            False
        )


    # antes da camera estava assim:
    # screen.blit(
    #     personagem,
    #     (int(pos_x - 12), int(pos_y - 9))
    # )

    # desenhar considerando a camera
    screen.blit(
        personagem,
        (
            int(pos_x - camera_x - 12),
            int(pos_y - 9)
        )
    )


    pygame.display.update()