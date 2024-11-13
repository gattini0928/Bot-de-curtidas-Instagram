import pyautogui as pg
from time import sleep
import webbrowser
from PIL import Image
import pyperclip as pclip
import os
from dotenv import load_dotenv

load_dotenv()

def login(email: str, senha: str):
    pg.click(1028,398)
    pg.write(email)
    sleep(0.5)
    pg.click(1026,463)
    pg.write(senha)
    pg.press('tab')
    pg.press('tab')
    pg.press('enter')

def fazer_comentario(comentario):
    pg.click(941,789, duration=0.5)
    pclip.copy(comentario) # Para permitir caracteres especiais
    pg.hotkey('ctrl', 'v')
    sleep(1)
    pg.click(1302,784,duration=0.5)

def like_e_comentar(posicao_like, cor_curtido, cor_nao_curtido):
    screenshot = pg.screenshot()  # Captura a tela a cada loop
    cor_pixel = screenshot.getpixel(posicao_like) # Acho o pixel na posição do like
    
    if cor_pixel == cor_curtido:
        print('Postagem já curtida')
    elif cor_pixel == cor_nao_curtido: # se a cor do pixel for a cor padrão curtir e comentar
        print('Curtindo Postagem ...')
        pg.click(posicao_like, duration=1)
        comentario = pg.prompt(text='Digite seu comentário', title='Fazer Comentário')
        fazer_comentario(comentario)
        sleep(5)
        print('Postagem Curtida! ...')
        sleep(1)
    else:
        print('Cor não encontrada')
        sleep(1)

def sair_do_instagram():
    pg.click(1546,186, duration=0.5)  # Acessa o menu do perfil
    sleep(2)
    pg.click(85,828, duration=0.5)   # Acessa as opções de sair
    sleep(0.5)
    pg.click(64,753)  # Confirma o logout
    sleep(2)

if __name__ == '__main__':
    email = os.getenv('email')
    senha = os.getenv('senha')
    posicao_like = (769, 658)
    cor_curtido = (255, 48, 64)
    cor_nao_curtido = (0, 0, 0)

    while True:
        # Abre o Instagram e faz login
        webbrowser.open('https://www.instagram.com/')
        conta = 'nike'
        sleep(2)
        login(email, senha)
        sleep(5)
        
        # Navega até a postagem
        pg.click(961, 567, duration=0.3)
        sleep(1)
        pg.moveTo(158, 369)
        pg.click()
        sleep(1)
        pg.write(conta)
        sleep(1)
        pg.move(0, 15)
        sleep(0.5)
        pg.click()
        sleep(5)
        pg.scroll(-1000)
        sleep(0.5)
        pg.click(556, 338, duration=1)
        sleep(3)
        
        # Verifica e executa o like
        like_e_comentar(posicao_like, cor_curtido, cor_nao_curtido)
        
        # Sai do Instagram após o processo de like
        sair_do_instagram()
        
        # Aguardar 24 horas para a próxima execução
        print('Aguardando 24 horas para a próxima execução')
        sleep(86400)