import tkinter as tk

class Funcs:
    def add(self, num):
        self.equacao_txt = self.equacao_txt + str(num)
        self.equacao_label.set(self.equacao_txt)
        print(self.equacao_txt)
    def limpar(self):
        self.equacao_txt = ''
        self.equacao_label.set(self.equacao_txt)
    def igual(self):
        self.equacao_txt = eval(self.equacao_txt)
        self.equacao_label.set(self.equacao_txt)
class App(Funcs):
    def __init__(self):
        self.root = tk.Tk()
        self.estilizacao()
        self.config()
        self.tela()
        self.bts()
        self.root.mainloop()
    def estilizacao(self):
        self.visor_bg = '#1A2C33'
        self.app_bg = '#2B4E4F'
        self.bt_bg = '#17301E'
    def config(self):
        self.root.geometry('450x450')
        self.root.title('Calculadora')
        self.root.configure(bg=self.app_bg)
        self.equacao_txt = ''
        self.equacao_label = tk.StringVar()
    def tela(self):
        self.visor = tk.Label(self.root, bg=self.visor_bg, font='20',width=45,height=5, textvariable=self.equacao_label)
        self.visor.pack()
    def bts(self):
        #Local aonde os botões vão ficar
        self.frame_bt = tk.Frame(self.root)
        self.frame_bt.pack()
        #Botões
        self.bt_1 = tk.Button(self.frame_bt, text=1, font=('Times', 10), bg=self.bt_bg, command=lambda:self.add(1))
        self.bt_1.grid(row=0, column=0)
        self.bt_2 = tk.Button(self.frame_bt, text=2, font=('Times', 10), bg=self.bt_bg, command=lambda: self.add(2))
        self.bt_2.grid(row=0, column=1)
        self.bt_3 = tk.Button(self.frame_bt, text=3, font=('Times', 10), bg=self.bt_bg, command=lambda: self.add(3))
        self.bt_3.grid(row=0, column=2)
        self.bt_4 = tk.Button(self.frame_bt, text=4, font=('Times', 10), bg=self.bt_bg, command=lambda: self.add(4))
        self.bt_4.grid(row=1, column=0)
        self.bt_5 = tk.Button(self.frame_bt, text=5, font=('Times', 10), bg=self.bt_bg, command=lambda: self.add(5))
        self.bt_5.grid(row=1, column=1)
        self.bt_6 = tk.Button(self.frame_bt, text=6, font=('Times', 10), bg=self.bt_bg, command=lambda: self.add(6))
        self.bt_6.grid(row=1, column=2)
        self.bt_7 = tk.Button(self.frame_bt, text=7, font=('Times', 10), bg=self.bt_bg, command=lambda: self.add(7))
        self.bt_7.grid(row=2, column=0)
        self.bt_8 = tk.Button(self.frame_bt, text=8, font=('Times', 10), bg=self.bt_bg, command=lambda: self.add(8))
        self.bt_8.grid(row=2, column=1)
        self.bt_9 = tk.Button(self.frame_bt, text=9, font=('Times', 10), bg=self.bt_bg, command=lambda: self.add(9))
        self.bt_9.grid(row=2, column=2)
        self.bt_0 = tk.Button(self.frame_bt, text=0, font=('Times', 10), bg=self.bt_bg, command=lambda: self.add(0))
        self.bt_0.grid(row=3, column=1)
        self.bt_limpar = tk.Button(self.frame_bt, text='C', font=('Times', 10), bg=self.bt_bg, command=self.limpar)
        self.bt_limpar.grid(row=3, column=0)
App()