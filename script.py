import tkinter as tk

janela = tk.Tk()
janela.title("calculadora")
janela.geometry("300x400")

def calcular():
    try:
        num =float(numero1.get())
        num2 = float(numero2.get())
        operacao = soma.get()
        if operacao =="+":
            valor = num + num2
        elif operacao =="-":
            valor = num - num2
        elif operacao =="*":
            valor = num * num2
        elif operacao =="/":
            valor = num / num2
    except ValueError:
         valor = "Entrada inválida"

    resultado.config(text=f"Resultado: {valor}")

label = tk.Label(janela, text="Calculadora", font=("Arial", 20))
label.pack(pady=10)

numero1 = tk.Entry(janela)
numero1.pack(pady=5)

soma = tk.Entry(janela)
soma.pack(pady=5)

numero2= tk.Entry(janela)
numero2.pack(pady=5)

resultado = tk.Label(janela , fg ="green", font=("Arial", 16))
resultado.pack(pady=10)

botao = tk.Button(janela, text="Calcular", command=calcular)
botao.pack(pady=10)

janela.mainloop()