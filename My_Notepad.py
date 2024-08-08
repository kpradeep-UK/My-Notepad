import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser

class My_Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("My Notepad")
        self.root.geometry("850x650")

        self.text_area = tk.Text(self.root, wrap='word', undo=True)
        self.text_area.pack(fill='both', expand=True)

        self.scrollbar = tk.Scrollbar(self.text_area)
        self.text_area.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text_area.yview)
        self.scrollbar.pack(side='right', fill='y')

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        self.file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        self.file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app, accelerator="Alt+F4")

        # Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut_text, accelerator="Ctrl+X")
        self.edit_menu.add_command(label="Copy", command=self.copy_text, accelerator="Ctrl+C")
        self.edit_menu.add_command(label="Paste", command=self.paste_text, accelerator="Ctrl+V")
        self.edit_menu.add_command(label="Undo", command=self.undo_text, accelerator="Ctrl+Z")
        self.edit_menu.add_command(label="Redo", command=self.redo_text, accelerator="Ctrl+Y")

        # Help menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.about_app)

        # Bind keyboard shortcuts
        self.root.bind("<Control-n>", lambda event: self.new_file())
        self.root.bind("<Control-o>", lambda event: self.open_file())
        self.root.bind("<Control-s>", lambda event: self.save_file())
        self.root.bind("<Control-x>", lambda event: self.cut_text())
        self.root.bind("<Control-c>", lambda event: self.copy_text())
        self.root.bind("<Control-v>", lambda event: self.paste_text())
        self.root.bind("<Control-z>", lambda event: self.undo_text())
        self.root.bind("<Control-y>", lambda event: self.redo_text())

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.root.title("New File")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[
                ("All Files", "*.*"),
                ("Text Files", "*.txt"),
                ("Word Document", "*.docx"),
                ("Python", "*.py"),
                ("C", "*.c"),
                ("C++", "*.cpp")
            ]
        )

        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.root.title(f"{file_path} - My Notepad")

    def open_file(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[
                ("All Files", "*.*"),
                ("Text Files", "*.txt"),
                ("Word Document", "*.docx"),
                ("Python", "*.py"),
                ("C", "*.c"),
                ("C++", "*.cpp")
            ]
        )

        if file_path:
            with open(file_path, 'r') as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())
            self.root.title(f"{file_path} - My Notepad")

    def exit_app(self):
        self.root.quit()

    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")

    def undo_text(self):
        self.text_area.event_generate("<<Undo>>")

    def redo_text(self):
        self.text_area.event_generate("<<Redo>>")

    def about_app(self):
        about_window = tk.Toplevel(self.root)
        about_window.title("About Notepad")
        about_window.geometry("400x200")

        label = tk.Label(about_window, text="Notepad by Pradeep Kumar K\n", font=("Arial",14,"bold"))
        label.pack(anchor='w')

        linkedin_label = tk.Label(about_window, text="Linked In:")
        linkedin_label.pack(anchor='w')

        linkedin_link = tk.Label(about_window, text="https://www.linkedin.com/in/pradeep-kumar-k-5440a7222/", fg="blue", cursor="hand2")
        linkedin_link.pack(anchor='w')
        linkedin_link.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.linkedin.com/in/pradeep-kumar-k-5440a7222/"))

        github_label = tk.Label(about_window, text="GitHub: ")
        github_label.pack(anchor='w')

        github_link = tk.Label(about_window, text="https://github.com/kpradeep-UK", fg="red", cursor="hand2")
        github_link.pack(anchor='w')
        github_link.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/kpradeep-UK"))

        email_label = tk.Label(about_window, text="Email: ")
        email_label.pack(anchor='w')

        email_link = tk.Label(about_window, text="pradeepkumarb2003@gmail.com", fg="green", cursor="hand2")
        email_link.pack(anchor='w')
        email_link.bind("<Button-1>", lambda e: webbrowser.open_new("mailto:pradeepkumarb2003@gmail.com"))

if __name__ == "__main__":
    root = tk.Tk()
    np = My_Notepad(root)
    root.mainloop()
