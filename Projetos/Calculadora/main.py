from typing import Optional, Tuple, Union
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.frame = ctk.CTkFrame(self, width=300, height=50, fg_color="#116", corner_radius=0)
        self.frame.pack()
        self.lb_title = ctk.CTkLabel(self.frame, text="Calculadora", font=('Roboto bold', 24))
        self.lb_title.place(x=90, y=10)

        self.span = ctk.CTkLabel(self, text='Está é uma calculadora simples baseada no Eval,\n não exija muito dela, uso apenas para aprendizagem.')
        self.span.pack(pady=5)

        self.entry = ctk.CTkEntry(self, width=250, font=('Roboto bold', 18))
        self.entry.pack(pady=20)

        self.result = ctk.CTkLabel(self, text="", text_color='teal', font=('Roboto bold', 20))
        self.result.pack()

        self.btn = ctk.CTkButton(self, width=250, text='Calcular'.upper(), command=self.calcular)
        self.btn.pack(pady=20)


    def calcular(self):
        self.result.configure(text=str(eval(self.entry.get())))

app = App()
app.geometry("300x300")
app.title('Calculadora Simples')
app.resizable(width=False, height=False)

app.mainloop()