from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Tkinter Demo")
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        tab1 = Menu(menu)
        tab1.add_command(label="Tab1 Action", command=self.tab1_action)
        menu.add_cascade(label="Tab 1", menu=tab1)

        tab2 = Menu(menu)
        tab2.add_command(label="Tab2 Action", command=self.tab2_action)
        menu.add_cascade(label="Tab 2", menu=tab2)

        tab3 = Menu(menu)
        tab3.add_command(label="Tab3 Action", command=self.tab3_action)
        menu.add_cascade(label="Tab 3", menu=tab3)

    def client_exit(self):
        exit()

    def tab1_action(self):
        t = Toplevel(self)
        t.wm_title("Tab1 Window")
        l = Label(t, text="This is new window from Tab1 Action")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)

    def tab2_action(self):
        with open('description.txt', 'r') as myfile:
            data=myfile.read()
            t = Toplevel(self)
            t.wm_title("Tab2 Window")
            text = Text(t)
            text.insert(INSERT,data)
            text.pack()

    def tab3_action(self):
        text = Text(self)
        text.insert(INSERT, "This run a python function")
        text.pack()

if __name__ == '__main__':
    root = Tk()
    root.geometry("400x300")
    app = Window(root)
    root.mainloop()
