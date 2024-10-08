# passo 1: entrar no sistema
import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.hotkey('win', 's')
pyautogui.write('opera')
pyautogui.press('enter')

# passo 2: login
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# pausa de 3 segundos pra pagina poder carregar
time.sleep(3)
pyautogui.click(x=427, y=409)
pyautogui.write('samuel@gmail.com')
pyautogui.press('tab')
pyautogui.write('123456789')
pyautogui.press('tab')
pyautogui.press('enter')

# passo 3: importar base de dados
import pandas

tabela = pandas.read_csv('produtos.csv')
print(tabela)

# passo 4: cadastrar produto

# passo 5: repetir processos