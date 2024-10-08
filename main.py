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

linha = 0

# para cada linha da minha tabela
for linha in tabela.index: 

#index é o n° das linhas, que o python faz automaticamente
    
    pyautogui.click(x=395, y=295)
    
    # codigo
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    # marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    # tipo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    # categoria
    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(int(categoria))
    pyautogui.press('tab')

    # preco unitario
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(float(preco_unitario))
    pyautogui.press('tab')

    # custo
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(float(custo))
    pyautogui.press('tab')

    # obs
    obs = tabela.loc[linha, 'obs']
    pyautogui.write(str(obs))
    pyautogui.press('tab')

    # clicar no enviar
    pyautogui.press('enter')
    pyautogui.scroll(5000)

# passo 5: repetir processos