
import pygame, sys
from pygame.locals import QUIT
from random import randint


# Histograma 1 - Lista com 60 números aleatórios

nums1 = []

for i in range(60):
    nums1.append(randint(0, 100))

num_cat1 = 5


# Histograma 2 - Lista estática do professor

nums2 = [
    100, 120, 130, 120, 150, 100, 160, 200,
    190, 110, 115, 125, 135, 170, 130
]

# Vamos escolher aleatoriamente quais números serão usados.


nums2_aleatorios = []

for i in range(len(nums2)):
    if randint(0, 1) == 1:
        nums2_aleatorios.append(nums2[i])

num_cat2 = 4


# Histograma 3 - Lista criada pelo usuário

nums3 = []

quantidade = int(input("Quantos números deseja inserir? "))

while quantidade < 1:
    quantidade = int(input("Digite uma quantidade maior que zero: "))

for i in range(quantidade):
    num = int(input("Digite um número: "))
    nums3.append(num)

num_cat3 = 3


# FUNÇÃO PARA CONTABILIZAR OS NÚMEROS EM CADA FAIXA

def contabiliza_totais(nums, num_cat, num_min, num_max):

    # Cria uma lista de zeros para guardar os totais.
    lista_total = [0] * num_cat

    # Calcula o tamanho de cada categoria.
    tam_cat = (num_max - num_min) / num_cat

    # Evita divisão por zero quando todos os números são iguais.
    if tam_cat == 0:
        lista_total[0] = len(nums)
        return lista_total

    # Percorre todos os números da lista.
    for i in range(len(nums)):

        # O maior número pertence à última categoria.
        if nums[i] == num_max:
            lista_total[-1] += 1
            continue

        # Verifica a categoria correspondente a cada número.
        for i_cat in range(num_cat):

            # Calcula os limites da categoria.
            lim_inf = num_min + i_cat * tam_cat
            lim_sup = lim_inf + tam_cat

            # Verifica se o número pertence a essa faixa.
            if lim_inf <= nums[i] < lim_sup:
                lista_total[i_cat] += 1
                break

    return lista_total


# Calcula os totais de cada histograma.

total1 = contabiliza_totais(nums1, num_cat1, min(nums1), max(nums1))

# Usamos os limites da lista fixa original.
total2 = contabiliza_totais(
    nums2_aleatorios, num_cat2, min(nums2), max(nums2)
)

total3 = contabiliza_totais(nums3, num_cat3, min(nums3), max(nums3))


# FUNÇÃO PARA CRIAR CORES ALEATÓRIAS

def criar_cores(num_cat):
    cores = []

    for i in range(num_cat):
        cor = (
            randint(50, 230),
            randint(50, 230),
            randint(50, 230)
        )
        cores.append(cor)

    return cores


cores1 = criar_cores(num_cat1)
cores2 = criar_cores(num_cat2)
cores3 = criar_cores(num_cat3)


# INICIALIZAÇÃO DO PYGAME

pygame.init()

screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Atividade - Histogramas")

fonte = pygame.font.SysFont(None, 22)
fonte_titulo = pygame.font.SysFont(None, 28)


# FUNÇÃO PARA DESENHAR UM HISTOGRAMA

def draw(screen, lista_total, num_min, num_max, cores, titulo, pos_y):

    # Define as posições e o tamanho do gráfico.
    eixo_x = 100
    eixo_y = pos_y + 180
    largura = 800
    altura = 140

    num_cat = len(lista_total)

    # Desenha o título.
    texto = fonte_titulo.render(titulo, True, (255, 255, 255))
    screen.blit(texto, (100, pos_y))

    # Desenha os eixos X e Y.
    pygame.draw.line(
        screen, (255, 255, 255),
        (eixo_x, eixo_y), (eixo_x + largura, eixo_y), 2
    )

    pygame.draw.line(
        screen, (255, 255, 255),
        (eixo_x, eixo_y), (eixo_x, eixo_y - altura), 2
    )

    # Descobre o maior total para calcular a altura das barras.
    maior_total = max(lista_total)

    if maior_total == 0:
        maior_total = 1

    # Calcula a largura de cada categoria.
    largura_cat = largura / num_cat

    # Desenha as barras.
    for i in range(num_cat):

        x = eixo_x + i * largura_cat + 5

        # Calcula a altura proporcional à frequência.
        h = lista_total[i] * altura / maior_total

        # Desenha o retângulo de cada categoria.
        pygame.draw.rect(
            screen, cores[i],
            (x, eixo_y - h, largura_cat - 10, h)
        )

        # Escreve a frequência acima da barra.
        texto = fonte.render(str(lista_total[i]), True, (255, 255, 255))
        screen.blit(texto, (x + 10, eixo_y - h - 22))

    # Desenha as marcações do eixo X.
    for i in range(num_cat + 1):

        x = eixo_x + i * largura_cat

        pygame.draw.line(
            screen, (255, 255, 255),
            (x, eixo_y - 4), (x, eixo_y + 4), 2
        )

        valor = num_min + i * (num_max - num_min) / num_cat

        texto = fonte.render(str(round(valor, 1)), True, (255, 255, 255))
        screen.blit(texto, (x - 15, eixo_y + 10))

    # Desenha cinco divisões no eixo Y.
    for i in range(6):

        valor = maior_total * i / 5
        y = eixo_y - altura * i / 5

        pygame.draw.line(
            screen, (255, 255, 255),
            (eixo_x - 5, y), (eixo_x + 5, y), 2
        )

        texto = fonte.render(str(round(valor, 1)), True, (255, 255, 255))
        screen.blit(texto, (45, y - 8))


# LOOP PRINCIPAL DO PYGAME 

while True:

    # Verifica se o usuário fechou a janela.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Limpa a tela antes de desenhar.
    screen.fill((30, 30, 30))

    # Desenha os três histogramas em posições diferentes.
    draw(screen, total1, min(nums1), max(nums1),
         cores1, "Histograma 1 - Números aleatórios", 20)

    draw(screen, total2, min(nums2), max(nums2),
         cores2, "Histograma 2 - Lista estática", 280)

    draw(screen, total3, min(nums3), max(nums3),
         cores3, "Histograma 3 - Input do usuário", 540)

    # Atualiza a janela.
    pygame.display.update()
