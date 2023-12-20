from tkinter import *

def mostrar_mensagem():
    label.config(text= 'Olá, mundo!')

root = Tk()

# Configuração da janela principal
root.geometry('500x700')
root.title('My first App')
root.config(bg = 'lightblue')

label = Label(root, text= "Bem vindo à minha primeira interface em python!", font=('Arial', 18))
label.pack(pady=20)

# Criando um botão
botao = Button(root, text="Clique aqui", command= mostrar_mensagem)
botao.pack(pady=10)

# Iniciando o loop principal para que a interface continue rodando
root.mainloop()