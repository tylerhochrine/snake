import os
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(padx=20, pady=20)
        self.create_widgets()

    def create_widgets(self):
        self.welcome_text = tk.Message(self, text="Snake\n", font=("Arial", 25), width=400)
        self.welcome_text.pack(anchor='center')

        self.start_game = tk.Button(self, text="Start Game",
                                    command=self.start_game, width=20)
        self.start_game.pack(anchor='center')

        self.options = tk.Button(self, text="Options",
                                 command=self.options, width=20)
        self.options.pack(anchor='center')

        self.quit = tk.Button(self, text="Quit",
                              command=self.master.destroy, width=20)
        self.quit.pack(anchor='center')

    def start_game(self):
        self.master.withdraw()
        os.system('python snake.py')
        self.master.deiconify()

    def options(self):
        options_window = Second(self.master)


class Second(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.bind("<Destroy>", self.on_destroy)

        self.master = master
        self.master.withdraw()

        self.master.title("Welcome To Snake!")

        self.geometry(f'{self.master.winfo_width()}x{self.master.winfo_height()}+{int(root.winfo_x())}+{int(root.winfo_y())}')
        self.minsize(300, 200)
        self.maxsize(900, 600)

        self.create_widgets()

    def create_widgets(self):
        self.options_text = tk.Message(self, text="Options\n", font=("Arial", 25), width=400)
        self.options_text.pack(anchor='center')

        self.save_changes = tk.Button(self, text="Save Changes",
                                                command=self.save_changes, width=20)
        self.save_changes.pack(anchor='center')

        self.quit = tk.Button(self, text="Back to Menu",
                                        command=lambda: [root.deiconify(), self.destroy()], width=20)
        self.quit.pack(anchor='center')

    def save_changes(self):
        print("changes saved")

    def on_destroy(self, event):
        if event.widget == self:
            self.master.deiconify()


root = tk.Tk()
app = Application(master=root)
app.master.title("Welcome To Snake!")

app_width = 600
app_height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

app.master.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
app.master.minsize(300, 200)
app.master.maxsize(900, 600)
app.mainloop()
