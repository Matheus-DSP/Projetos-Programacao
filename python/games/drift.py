import pygame
import math
import sys

pygame.init()

# ==========================================
# CONFIGURAÇÕES
# ==========================================

LARGURA = 900
ALTURA = 700

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Drift no Cone")

relogio = pygame.time.Clock()

# ==========================================
# CORES
# ==========================================

FUNDO = (35, 35, 35)
PISTA = (70, 70, 70)
BRANCO = (255, 255, 255)
VERMELHO = (220, 40, 40)
AZUL = (40, 120, 255)
PRETO = (20, 20, 20)
LARANJA = (255, 140, 20)
AMARELO = (255, 220, 40)

# ==========================================
# FONTE
# ==========================================

fonte = pygame.font.SysFont("arial", 30, bold=True)
fonte_grande = pygame.font.SysFont("arial", 55, bold=True)

# ==========================================
# CONE
# ==========================================

cone_x = LARGURA // 2
cone_y = ALTURA // 2

cone_raio = 22

# ==========================================
# CARRO
# ==========================================

carro_x = cone_x + 180
carro_y = cone_y

carro_largura = 35
carro_altura = 65

angulo = 0

# ==========================================
# DRIFT
# ==========================================

velocidade_angular = 1.5

pontuacao = 0

jogo_ativo = True

# ==========================================
# FUNÇÃO DESENHAR CARRO
# ==========================================

def desenhar_carro():

    carro = pygame.Surface(
        (carro_largura, carro_altura),
        pygame.SRCALPHA
    )

    # Corpo do carro
    pygame.draw.rect(
        carro,
        VERMELHO,
        (5, 5, 25, 55),
        border_radius=8
    )

    # Vidro
    pygame.draw.rect(
        carro,
        AZUL,
        (9, 18, 17, 18),
        border_radius=3
    )

    # Rodas
    pygame.draw.rect(
        carro,
        PRETO,
        (0, 10, 7, 15)
    )

    pygame.draw.rect(
        carro,
        PRETO,
        (28, 10, 7, 15)
    )

    pygame.draw.rect(
        carro,
        PRETO,
        (0, 40, 7, 15)
    )

    pygame.draw.rect(
        carro,
        PRETO,
        (28, 40, 7, 15)
    )

    # Faróis
    pygame.draw.rect(
        carro,
        AMARELO,
        (8, 3, 7, 5)
    )

    pygame.draw.rect(
        carro,
        AMARELO,
        (20, 3, 7, 5)
    )

    # Girar carro
    carro_rotacionado = pygame.transform.rotate(
        carro,
        -angulo
    )

    retangulo = carro_rotacionado.get_rect(
        center=(carro_x, carro_y)
    )

    tela.blit(
        carro_rotacionado,
        retangulo
    )


# ==========================================
# FUNÇÃO DESENHAR CONE
# ==========================================

def desenhar_cone():

    # sombra
    pygame.draw.circle(
        tela,
        PRETO,
        (cone_x + 5, cone_y + 5),
        cone_raio
    )

    # base
    pygame.draw.ellipse(
        tela,
        PRETO,
        (
            cone_x - 28,
            cone_y + 8,
            56,
            15
        )
    )

    # cone
    pygame.draw.polygon(
        tela,
        LARANJA,
        [
            (cone_x, cone_y - 35),
            (cone_x - 22, cone_y + 12),
            (cone_x + 22, cone_y + 12)
        ]
    )

    # faixa branca
    pygame.draw.polygon(
        tela,
        BRANCO,
        [
            (cone_x - 12, cone_y - 5),
            (cone_x + 12, cone_y - 5),
            (cone_x + 17, cone_y + 5),
            (cone_x - 17, cone_y + 5)
        ]
    )


# ==========================================
# RESETAR JOGO
# ==========================================

def reiniciar():

    global carro_x
    global carro_y
    global angulo
    global pontuacao
    global jogo_ativo

    carro_x = cone_x + 180
    carro_y = cone_y

    angulo = 0

    pontuacao = 0

    jogo_ativo = True


# ==========================================
# LOOP PRINCIPAL
# ==========================================

rodando = True

while rodando:

    dt = relogio.tick(60) / 1000

    # ======================================
    # EVENTOS
    # ======================================

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:

            rodando = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_ESCAPE:

                rodando = False

            if evento.key == pygame.K_SPACE:

                reiniciar()

    # ======================================
    # JOGO
    # ======================================

    if jogo_ativo:

        # ==================================
        # MOVIMENTO CIRCULAR
        # ==================================

        angulo += velocidade_angular

        raio = 180

        radianos = math.radians(angulo)

        carro_x = (
            cone_x +
            math.cos(radianos) * raio
        )

        carro_y = (
            cone_y +
            math.sin(radianos) * raio
        )

        # ==================================
        # PONTUAÇÃO
        # ==================================

        pontuacao += velocidade_angular * 0.5

        # ==================================
        # COLISÃO
        # ==================================

        distancia = math.sqrt(
            (carro_x - cone_x) ** 2 +
            (carro_y - cone_y) ** 2
        )

        if distancia < 55:

            jogo_ativo = False

    # ======================================
    # DESENHAR
    # ======================================

    tela.fill(FUNDO)

    # círculo da área de drift
    pygame.draw.circle(
        tela,
        PISTA,
        (cone_x, cone_y),
        250
    )

    # marca do círculo
    pygame.draw.circle(
        tela,
        BRANCO,
        (cone_x, cone_y),
        180,
        2
    )

    desenhar_cone()

    if jogo_ativo:

        desenhar_carro()

        texto_pontos = fonte.render(
            f"DRIFT: {int(pontuacao)}",
            True,
            BRANCO
        )

        tela.blit(
            texto_pontos,
            (25, 25)
        )

        instrucoes = fonte.render(
            "ESPAÇO = Reiniciar | ESC = Sair",
            True,
            BRANCO
        )

        tela.blit(
            instrucoes,
            (25, ALTURA - 50)
        )

    else:

        texto_gameover = fonte_grande.render(
            "💥 VOCÊ BATEU!",
            True,
            VERMELHO
        )

        tela.blit(
            texto_gameover,
            (
                LARGURA // 2 -
                texto_gameover.get_width() // 2,
                220
            )
        )

        texto_score = fonte.render(
            f"Pontuação: {int(pontuacao)}",
            True,
            AMARELO
        )

        tela.blit(
            texto_score,
            (
                LARGURA // 2 -
                texto_score.get_width() // 2,
                300
            )
        )

        texto_restart = fonte.render(
            "PRESSIONE ESPAÇO PARA TENTAR NOVAMENTE",
            True,
            BRANCO
        )

        tela.blit(
            texto_restart,
            (
                LARGURA // 2 -
                texto_restart.get_width() // 2,
                370
            )
        )

    pygame.display.flip()


pygame.quit()
sys.exit()