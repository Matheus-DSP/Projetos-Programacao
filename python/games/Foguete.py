
import pygame
import random
import sys

pygame.init()


# CONFIGURAÇÕES
LARGURA = 800
ALTURA = 900

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("🚀 Foguete de Combate")

relogio = pygame.time.Clock()

# Cores
PRETO = (10, 10, 25)
BRANCO = (255, 255, 255)
VERDE = (50, 255, 100)
VERMELHO = (255, 70, 70)
AMARELO = (255, 230, 50)
AZUL = (50, 150, 255)
MARROM = (50, 150, 255)

fonte = pygame.font.Font(None, 36)
fonte_grande = pygame.font.Font(None, 70)

# JOGADOR
jogador = pygame.Rect(
    LARGURA // 2 - 25,
    ALTURA - 70, 50, 40
)

velocidade_jogador = 10

# TIROS
tiros = []
velocidade_tiro = 10
municao = 50
MAX_MUNICAO = 50

# INIMIGOS
inimigos = []
velocidade_inimigo = 3

# CAIXA DE MUNICAO
caixa_municao = []
velocidade_caixa = 3
tempo_municao = 0
intervalo_municao = 600

# ESTRELAS
estrelas = []

for _ in range(80):
    estrelas.append([
        random.randint(0, LARGURA),
        random.randint(0, ALTURA),
        random.randint(1, 3)
    ])

# JOGO
pontuacao = 0
vidas = 3
recorde = 0
rodando = True
game_over = False
tempo_inimigo = 0

def criar_inimigo():
    x = random.randint(0, LARGURA - 40)

    inimigo = pygame.Rect(
        x,
        -40,
        40,
        30
    )
    
    inimigos.append(inimigo)

def desenhar_jogador():
    # Corpo da nave
    pygame.draw.polygon(
        tela,
        AZUL,
        [
            (jogador.centerx, jogador.top),
            (jogador.left, jogador.bottom),
            (jogador.right, jogador.bottom)
        ]
    )

    # Janela da nave
    pygame.draw.circle(
        tela,
        AMARELO,
        (jogador.centerx, jogador.top + 18),
        6
    )


def desenhar_inimigo(inimigo):
    pygame.draw.polygon(
        tela,
        VERMELHO,
        [
            (inimigo.left, inimigo.top + 10),
            (inimigo.left + 10, inimigo.top),
            (inimigo.right - 10, inimigo.top),
            (inimigo.right, inimigo.top + 10),
            (inimigo.right - 5, inimigo.bottom),
            (inimigo.centerx, inimigo.bottom - 8),
            (inimigo.left + 5, inimigo.bottom)
        ]
    )

    pygame.draw.circle(
        tela,
        AMARELO,
        (inimigo.left + 10, inimigo.centery),
        4
    )

    pygame.draw.circle(
        tela,
        AMARELO,
        (inimigo.right - 10, inimigo.centery),
        4
    )


def reiniciar():
    global pontuacao, vidas, game_over, recorde, municao, tempo_municao

    pontuacao = 0
    vidas = 3
    municao = 50
    tempo_municao = 0
    recorde = carregar_recorde()
    game_over = False

    jogador.x = LARGURA // 2 - 25
    jogador.y = ALTURA - 70

    tiros.clear()
    inimigos.clear()
    caixa_municao.clear()


def carregar_recorde():
    try:
        with open("recorde.txt", "r") as arquivo:
            return int(arquivo.read())
    except:
        return 0

def criar_caixa_municao():
    x = random.randint (20, LARGURA - 50)

    caixa = pygame.Rect(
        x, - 30, 30, 30
    )

    caixa_municao.append(caixa)

def desenhar_caixa_municao(caixa):
    # caixa
    pygame.draw.rect(tela, MARROM, caixa)

    # municao
    pygame.draw.rect(tela, BRANCO, 
                     (caixa.centerx - 3,
             caixa.top + 5, 
             6, 
             caixa.height - 10
             )
    )

    pygame.draw.rect( tela, BRANCO,
        ( caixa.left + 5, caixa.centery - 3, caixa.width - 10, 6)
    )
# LOOP PRINCIPAL
while rodando:

    relogio.tick(60)

    # EVENTOS
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_SPACE and not game_over and municao > 0:
                tiro = pygame.Rect(
                    jogador.centerx - 3,
                    jogador.top - 10,
                    6,
                    15
                )

                tiros.append(tiro)

                municao -= 1

            if evento.key == pygame.K_r and game_over:
                reiniciar()

    # JOGADOR
    if not game_over:

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            jogador.x -= velocidade_jogador

        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            jogador.x += velocidade_jogador

        # Impede sair da tela
        if jogador.left < 0:
            jogador.left = 0

        if jogador.right > LARGURA:
            jogador.right = LARGURA

    # TIROS
    if not game_over:

        for tiro in tiros[:]:

            tiro.y -= velocidade_tiro

            if tiro.bottom < 0:
                tiros.remove(tiro)

    # CRIAR INIMIGOS
    if not game_over:

        tempo_inimigo += 1

        if tempo_inimigo >= 35:
            criar_inimigo()
            tempo_inimigo = 0

            # CRIAR CAIXAS DE MUNIÇÃO
    if not game_over:

        tempo_municao += 1

    if tempo_municao >= intervalo_municao:
        criar_caixa_municao()
        tempo_municao = 0

    # MOVER INIMIGOS
    if not game_over:

        for inimigo in inimigos[:]:

            inimigo.y += velocidade_inimigo

            # Inimigo chegou ao jogador
            if inimigo.top > ALTURA:

                inimigos.remove(inimigo)
                vidas -= 1

                if vidas <= 0:
                    game_over = True

            # Colisão com a nave
            elif inimigo.colliderect(jogador):

                inimigos.remove(inimigo)
                vidas -= 1

                if vidas <= 0:
                    game_over = True

                    # MOVER CAIXAS DE MUNIÇÃO
    if not game_over:

        for caixa in caixa_municao[:]:

            caixa.y += velocidade_caixa

        # Remove se sair da tela
            if caixa.top > ALTURA:
                caixa_municao.remove(caixa)

    # COLISÃO DOS TIROS
    if not game_over:

        for tiro in tiros[:]:

            for inimigo in inimigos[:]:

                if tiro.colliderect(inimigo):

                    if tiro in tiros:
                        tiros.remove(tiro)

                    if inimigo in inimigos:
                        inimigos.remove(inimigo)

                    pontuacao += 10

                    if pontuacao > recorde:
                        recorde = pontuacao

                    break

        # COLISÃO COM CAIXA DE MUNIÇÃO
        for tiro in tiros[:]:

            for caixa in caixa_municao[:]:

                if tiro.colliderect(caixa):

                    if tiro in tiros:
                        tiros.remove(tiro)

                    if caixa in caixa_municao:
                        caixa_municao.remove(caixa)

                    # Recupera 20 munições
                    municao += 20

                    # Não deixa passar de 50
                    if municao > MAX_MUNICAO:
                        municao = MAX_MUNICAO

                    break


    # ESTRELAS
    for estrela in estrelas:

        estrela[1] += estrela[2]

        if estrela[1] > ALTURA:
            estrela[0] = random.randint(0, LARGURA)
            estrela[1] = 0

    # DESENHAR
    tela.fill(PRETO)

    # Estrelas
    for estrela in estrelas:

        pygame.draw.circle(
            tela,
            BRANCO,
            (estrela[0], estrela[1]),
            estrela[2] // 2 + 1
        )

    # Jogador
    if not game_over:
        desenhar_jogador()

    # Tiros
    for tiro in tiros:
        pygame.draw.rect(
            tela,
            AMARELO,
            tiro
        )

    # Inimigos
    for inimigo in inimigos:
        desenhar_inimigo(inimigo)

    # Caixas de munição
    for caixa in caixa_municao:
        desenhar_caixa_municao(caixa)

    # HUD
    texto_pontos = fonte.render(
        f"Pontuação: {pontuacao}",
        True,
        BRANCO
    )

    texto_recorde = fonte.render(
        f"Recorde: {recorde}",
        True,
        BRANCO
)

    texto_vidas = fonte.render(
        f"Vidas: {vidas}",
        True,
        BRANCO
    )

    texto_municao = fonte.render(
    f"Munição: {municao}",
    True,
    BRANCO
)

    tela.blit(texto_pontos, (20, 20))
    tela.blit(texto_vidas, (650, 20))
    tela.blit(texto_recorde, (20, 60))
    tela.blit(texto_municao, (650, 60))

    # GAME OVER
    if game_over:

        texto_game_over = fonte_grande.render(
            "GAME OVER",
            True,
            VERMELHO
        )

        texto_final = fonte.render(
            f"Pontuação final: {pontuacao}",
            True,
            BRANCO
        )

        texto_restart = fonte.render(
            "Pressione R para jogar novamente",
            True,
            BRANCO
        )

        tela.blit(
            texto_game_over,
            (
                LARGURA // 2 - texto_game_over.get_width() // 2,
                220
            )
        )

        tela.blit(
            texto_final,
            (
                LARGURA // 2 - texto_final.get_width() // 2,
                300
            )
        )

        tela.blit(
            texto_restart,
            (
                LARGURA // 2 - texto_restart.get_width() // 2,
                350
            )
        )

    pygame.display.flip()


pygame.quit()
sys.exit()