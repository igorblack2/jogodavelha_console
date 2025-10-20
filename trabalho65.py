import tkinter as tk
from tkinter import messagebox

# =================== Variáveis globais ===================
placar_x = 0
placar_o = 0
jogador_atual = "X"

# =================== Funções do jogo ===================
def verificar_vitoria():
    # Verifica linhas, colunas e diagonais
    for i in range(3):
        if botoes[i][0]["text"] == botoes[i][1]["text"] == botoes[i][2]["text"] != "":
            anunciar_vencedor(botoes[i][0]["text"])
            return
        if botoes[0][i]["text"] == botoes[1][i]["text"] == botoes[2][i]["text"] != "":
            anunciar_vencedor(botoes[0][i]["text"])
            return
    if botoes[0][0]["text"] == botoes[1][1]["text"] == botoes[2][2]["text"] != "":
        anunciar_vencedor(botoes[0][0]["text"])
        return
    if botoes[0][2]["text"] == botoes[1][1]["text"] == botoes[2][0]["text"] != "":
        anunciar_vencedor(botoes[0][2]["text"])
        return
    # Verifica empate
    if all(botoes[i][j]["text"] != "" for i in range(3) for j in range(3)):
        messagebox.showinfo("Empate", "O jogo terminou empatado!")

def anunciar_vencedor(jogador):
    global placar_x, placar_o
    messagebox.showinfo("Vencedor", f"O jogador {jogador} venceu!")
    if jogador == "X":
        placar_x += 1
        label_placar_x.config(text=f"X: {placar_x}")
    else:
        placar_o += 1
        label_placar_o.config(text=f"O: {placar_o}")
    reiniciar_tabuleiro()

def reiniciar_tabuleiro():
    for i in range(3):
        for j in range(3):
            botoes[i][j].config(text="")
    global jogador_atual
    jogador_atual = "X"

def zerar_placar():
    global placar_x, placar_o
    placar_x = 0
    placar_o = 0
    label_placar_x.config(text=f"X: {placar_x}")
    label_placar_o.config(text=f"O: {placar_o}")
    reiniciar_tabuleiro()

def mostrar_creditos():
    messagebox.showinfo("Créditos", "Jogo da Velha em Python\nDesenvolvido por Igor Santos")

def alternar_jogador():
    global jogador_atual
    jogador_atual = "O" if jogador_atual == "X" else "X"

def jogada(i, j):
    if botoes[i][j]["text"] == "":
        botoes[i][j]["text"] = jogador_atual
        verificar_vitoria()
        alternar_jogador()

# =================== Configuração da janela ===================
janela = tk.Tk()
janela.title("Jogo da Velha Completo")
janela.resizable(False, False)

# =================== Placar ===================
label_placar_x = tk.Label(janela, text=f"X: {placar_x}", font=("Arial", 14))
label_placar_x.grid(row=0, column=0, padx=10, pady=10)
label_placar_o = tk.Label(janela, text=f"O: {placar_o}", font=("Arial", 14))
label_placar_o.grid(row=0, column=2, padx=10, pady=10)

# =================== Botões extras ===================
botao_reiniciar = tk.Button(janela, text="Reiniciar Partida", font=("Arial", 12), command=reiniciar_tabuleiro)
botao_reiniciar.grid(row=0, column=1, padx=5)
botao_zerar = tk.Button(janela, text="Zerar Placar", font=("Arial", 12), command=zerar_placar)
botao_zerar.grid(row=1, column=1, padx=5, pady=5)
botao_creditos = tk.Button(janela, text="Créditos", font=("Arial", 12), command=mostrar_creditos)
botao_creditos.grid(row=2, column=1, padx=5, pady=5)

# =================== Tabuleiro ===================
botoes = [[None for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        botoes[i][j] = tk.Button(janela, text="", width=10, height=4,
                                 font=("Arial", 20),
                                 command=lambda i=i, j=j: jogada(i, j))
        botoes[i][j].grid(row=i+3, column=j, padx=5, pady=5)

# =================== Inicia o jogo ===================
janela.mainloop()
