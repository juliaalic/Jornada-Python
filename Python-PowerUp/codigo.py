# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time
import pandas as pd
# pyautogui.write -> escrever um texto 
# pyautogui.press -> apertar 1 tecla 
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.5

# Abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")

# Entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)



# Passo 2: Fazer o Login
# Selecionar o campo de email
pyautogui.click(x=682, y=439)
# Escrever o seu email 
pyautogui.write("juiaagnomio@gmail.com")
pyautogui.press("tab") # Passando pro próximo campo
pyautogui.write("Senha123")
pyautogui.click(x=966, y=636) # clique no botão de login
time.sleep(3)


# Passo 3: Importar a base de produtos pra cadastrar
tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto 
for linha in tabela.index:
    # Clicar no campo de código
    pyautogui.click(x=604, y=298)
    # Pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # Preencher o campo 
    pyautogui.write(str(codigo))
    # Passar para o proximo campo 
    pyautogui.press("tab")
    # Preencher o campo 
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    # Dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim 