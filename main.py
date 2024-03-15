from tkinter import *

root = Tk()

# Window configuration
root.title("Text Editor")  # title of window
root.geometry("1200x620+10+10")  # window size
root.resizable(False, False)  # don't make it  resizable

# Menu bar
menubar = Menu(root)
root.config(menu=menubar)

# File menu
filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label='New', accelerator='Ctrl+N')
filemenu.add_command(label='Open', accelerator='Ctrl+O')
filemenu.add_command(label='Save', accelerator='Ctrl+S')
filemenu.add_command(label='Save As', accelerator='Ctrl+Alt+S')
filemenu.add_separator()
filemenu.add_command(label='Exit', accelerator='Ctrl+Q')
menubar.add_cascade(label='File', menu=filemenu)

# Edit menu
editmenu = Menu(menubar, tearoff=False)
editmenu.add_command(label='Cut', accelerator='Ctrl+X')
editmenu.add_command(label='Copy', accelerator='Ctrl+C')
editmenu.add_command(label='Past', accelerator='Ctrl+V')
editmenu.add_command(label='Clear', accelerator='Ctrl+Alt+X')
editmenu.add_command(label='Find', accelerator='Ctrl+F')
menubar.add_cascade(label='Edit', menu=editmenu)

# View menu
show_toolbar = BooleanVar()
show_statusbar = BooleanVar()
viewmenu = Menu(menubar, tearoff=False)
viewmenu.add_checkbutton(label='Tool Bar', variable=show_toolbar, onvalue=True, offvalue=False)
viewmenu.add_checkbutton(label='Status Bar', variable=show_statusbar, onvalue=True, offvalue=False)
menubar.add_cascade(label='View', menu=viewmenu)

# Themes menu
thememenu = Menu(menubar, tearoff=False)
theme_choice = StringVar()
light_image = PhotoImage(file='images/light.gif')
thememenu.add_radiobutton(label='Light', image=light_image,variable=theme_choice, compound=LEFT)
dark_image = PhotoImage(file='./images/dark.gif')
thememenu.add_radiobutton(label='Dark Default', image=dark_image,variable=theme_choice, compound=LEFT)

menubar.add_cascade(label='Theme', menu=thememenu)
root.mainloop()
