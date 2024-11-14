import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / (altura ** 2)
        categoria = classificar_imc(imc)
        resultado_label.config(text=f"Seu IMC é {imc:.2f} e você está na categoria: {categoria}")
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor, insira valores numéricos válidos.")

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")

# Labels e entradas para peso e altura
tk.Label(janela, text="Peso (kg):").grid(row=0, column=0, padx=10, pady=10)
entry_peso = tk.Entry(janela)
entry_peso.grid(row=0, column=1, padx=10, pady=10)

tk.Label(janela, text="Altura (m):").grid(row=1, column=0, padx=10, pady=10)
entry_altura = tk.Entry(janela)
entry_altura.grid(row=1, column=1, padx=10, pady=10)

# Botão para calcular IMC
botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
botao_calcular.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Label para exibir o resultado
resultado_label = tk.Label(janela, text="")
resultado_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Iniciar o loop principal da janela
janela.mainloop()
