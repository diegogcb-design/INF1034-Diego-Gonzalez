import pygame, sys
from pygame.locals import QUIT, KEYDOWN

# Iniciar PyGame
pygame.init()

clock = pygame.time.Clock()

# JANELA

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Atividade 11 - Animações")

# CARREGAR AS SPRITESHEETS

idle_spritesheet = pygame.image.load(
    "Atividade 11/character/idle/idle.png"
).convert_alpha()

running_spritesheet = pygame.image.load(
    "Atividade 11/character/running/running.png"
).convert_alpha()

jump_spritesheet = pygame.image.load(
    "Atividade 11/character/jumping/jump.png"
).convert_alpha()



# VARIÁVEIS DA ANIMAÇÃO 1 - IDLE

curr_frame_idle = 0
anim_time_idle = 0

# VARIÁVEIS DA ANIMAÇÃO 2 - RUNNING

curr_frame_run = 0
anim_time_run = 0

# Posição do personagem
x = 200
y = 250

# VARIÁVEIS DA ANIMAÇÃO 3 - JUMP

curr_frame_jump = 0
anim_time_jump = 0

run_jump_animation = False

# LOOP PRINCIPAL

while True:

    # EVENTOS

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # SPACE inicia a animação de pulo
        # apenas uma vez
        if event.type == KEYDOWN:

            if event.key == pygame.K_SPACE:

                if run_jump_animation == False:
                    run_jump_animation = True
                    curr_frame_jump = 0
                    anim_time_jump = 0


    # TEMPO

    clock.tick(60)

    dt = clock.get_time()

    # ANIMAÇÃO 1 - IDLE
    # Executada constantemente

    anim_time_idle = anim_time_idle + dt

    if anim_time_idle / 1000 > 0.15:

        curr_frame_idle = curr_frame_idle + 1

        # 7 frames
        if curr_frame_idle > 6:
            curr_frame_idle = 0

        anim_time_idle = 0

    # ANIMAÇÃO 2 
    # Executada enquanto D estiver pressionado

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:

        # Movimento para direita
        x = x + 3

        anim_time_run = anim_time_run + dt

        if anim_time_run / 1000 > 0.1:

            curr_frame_run = curr_frame_run + 1

            # 12 frames
            if curr_frame_run > 11:
                curr_frame_run = 0

            anim_time_run = 0

    # ANIMAÇÃO 3 
    # Executada uma vez ao pressionar SPACE

    if run_jump_animation:

        anim_time_jump = anim_time_jump + dt

        if anim_time_jump / 1000 > 0.1:

            curr_frame_jump = curr_frame_jump + 1

            # 13 frames
            if curr_frame_jump > 12:

                curr_frame_jump = 0
                run_jump_animation = False

            anim_time_jump = 0


    # DESENHAR NA TELA

    screen.fill((255, 255, 255))

    # ANIMAÇÃO 1 - IDLE
    # Spritesheet vertical
    screen.blit(
        idle_spritesheet,
        (50, 250),
        (0, 128 * curr_frame_idle, 128, 128)
    )

    # ANIMAÇÃO 2 - RUNNING
    # Spritesheet horizontal

    screen.blit(
        running_spritesheet,
        (x, y),
        (128 * curr_frame_run, 0, 128, 128)
    )

    # ANIMAÇÃO 3 - JUMP
    # Spritesheet horizontal

    if run_jump_animation:

        screen.blit(
            jump_spritesheet,
            (500, 250),
            (128 * curr_frame_jump, 0, 128, 128)
        )


    # Atualizar a tela
    pygame.display.update()