import tkinter as tk

window = tk.Tk()
# Cria um widget de caixa de texto
text_box = tk.Text(window)
text_box.pack()



input1 = tk.Entry(window)


input1.pack()


input2 = tk.Entry(window)


input2.pack()


input3 = tk.Entry(window)


input3.pack()


input4 = tk.Entry(window)


input4.pack()


# Cria um botão


button = tk.Button(window, text="Clique aqui", command=button_click)
button.pack()

# Inicia o loop principal da janela

window.mainloop()