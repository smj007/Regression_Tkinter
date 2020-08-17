from tkinter import *
from tkinter.ttk import *

from plotter import plot
from stats import stats_data

class App(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.widgets()

    def widgets(self):
        self.winfo_toplevel().title("Data")
        self.l1 = Label(self.master, text = "FileName")
        self.l2 = Label(self.master, text = "Label for X")
        self.l3 = Label(self.master, text = "Label for Y")

        self.l1.grid(row = 0)    
        self.l2.grid(row = 1)    
        self.l3.grid(row = 2)    

        self.entry_FName = Entry(self.master, width = 40)
        self.entry_X = Entry(self.master, width = 40)
        self.entry_Y = Entry(self.master, width = 40)

        self.entry_FName.grid(row = 0, column = 1, sticky = W) 
        self.entry_X.grid(row = 1, column = 1, sticky = W)  
        self.entry_Y.grid(row = 2, column = 1, sticky = W) 

        self.text_X = Text(self.master, width = 30) 
        self.text_Y = Text(self.master, width = 30) 

        self.text_X.grid(row = 3, column = 0)
        self.text_Y.grid(row = 3, column = 0)

        self.style = Style()
        self.style.map('D.TButton',
        foreground = [('pressed', 'red'), ('active', 'green')],
        background = [('pressed', '!disabled', 'black'), ('active', 'white')])

        self.btn = Button(self.master, text = "Plot Regression",
        style = "D.TButton")
        self.btn["command"] = self.show_graph
        self.btn.grid(row = 4, column = 0, sticky = W)

        self.stats = Button(self.master, text = "Show Em' Stats",
        style = "D.TButton")
        self.stats["command"] = self.show_stats
        self.stats.grid(row = 4, column = 1, sticky = W)

        self.quit = Button(self.master, text = "Quit",
        style = "D.TButton", command = self.master.destroy)
        self.quit.grid(row = 4, column = 1, sticky = E)



    def show_graph(self):
        plot(self.entry_FName.get(), self.entry_X.get(), self.entry_Y.get())


    def show_stats(self):
        stats_X, stats_Y = stats_data(self.entry_FName.get(), self.entry_X.get(), self.entry_Y.get()) 
        self.text_X.insert(INSERT, stats_X)  
        self.text_Y.insert(INSERT, stats_Y)  

root = Tk()
app = App(master = root)
app.mainloop()        