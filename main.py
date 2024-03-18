from tkinter import *
from tkinter.ttk import *
from tkinter import font, colorchooser

# Functions
fontsize = 12
fontstyle = 'arial'


def font_style(event):
    global fontstyle
    fontstyle = font_family_variable.get()
    textArea.config(font=(fontstyle, fontsize))


def font_size(event):
    global fontsize
    fontsize = size_variable.get()
    textArea.config(font=(fontstyle, fontsize))


def bold_text():
    text_property = font.Font(font=textArea['font']).actual()
    if text_property['weight'] == 'normal':
        textArea.config(font=(fontstyle, fontsize, 'bold'))
    if text_property['weight'] == 'bold':
        textArea.config(font=(fontstyle, fontsize, 'normal'))


def italic_text():
    text_property = font.Font(font=textArea['font']).actual()
    if text_property['slant'] == 'roman':
        textArea.config(font=(fontstyle, fontsize, 'italic'))
    if text_property['slant'] == 'italic':
        textArea.config(font=(fontstyle, fontsize, 'roman'))


def underline_text():
    text_property = font.Font(font=textArea['font']).actual()
    if text_property['underline'] == 0:
        textArea.config(font=(fontstyle, fontsize, 'underline'))
    if text_property['underline'] == 1:
        textArea.config(font=(fontstyle, fontsize,))


def color_select():
    chosen_color = colorchooser.askcolor()
    textArea.config(fg=str(chosen_color[1]))


def align_right():
    data = textArea.get(0.0, END)
    textArea.tag_config('right', justify=RIGHT)
    textArea.delete(0.0, END)
    textArea.insert(INSERT, data, 'right')


def align_left():
    data = textArea.get(0.0, END)
    textArea.tag_config('left', justify=LEFT)
    textArea.delete(0.0, END)
    textArea.insert(INSERT, data, 'left')


def align_center():
    data = textArea.get(0.0, END)
    textArea.tag_config('center', justify=CENTER)
    textArea.delete(0.0, END)
    textArea.insert(INSERT, data, 'center')


# UI
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
editmenu.add_command(label='Paste', accelerator='Ctrl+V')
editmenu.add_command(label='Clear', accelerator='Ctrl+Alt+X')
editmenu.add_command(label='Find', accelerator='Ctrl+F')
menubar.add_cascade(label='Edit', menu=editmenu)

# View menu
show_toolbar = BooleanVar()
show_statusbar = BooleanVar()
viewmenu = Menu(menubar, tearoff=False)
viewmenu.add_checkbutton(
    label='Tool Bar', variable=show_toolbar, onvalue=True, offvalue=False)
viewmenu.add_checkbutton(
    label='Status Bar', variable=show_statusbar, onvalue=True, offvalue=False)
menubar.add_cascade(label='View', menu=viewmenu)

# Themes menu
thememenu = Menu(menubar, tearoff=False)
theme_choice = StringVar()
light_image = PhotoImage(file='images/light.gif')
thememenu.add_radiobutton(label='Light', image=light_image,
                          variable=theme_choice, compound=LEFT)
dark_image = PhotoImage(file='images/dark.gif')
thememenu.add_radiobutton(
    label='Dark Default', image=dark_image, variable=theme_choice, compound=LEFT)
menubar.add_cascade(label='Theme', menu=thememenu)

# Toolbar section
tool_bar = Label(root)
tool_bar.pack(side=TOP, fill=X)
font_families = font.families()
font_family_variable = StringVar()
font_family_combobox = Combobox(tool_bar, width=30, values=font_families, state='readonly',
                                textvariable=font_family_variable)
font_family_combobox.current(font_families.index('Arial'))
font_family_combobox.grid(row=0, column=0, padx=5)

size_variable = IntVar()
font_size_combobox = Combobox(tool_bar, width=14, textvariable=size_variable, state='readonly',
                              values=tuple(range(8, 75)))
font_size_combobox.current(4)
font_size_combobox.grid(row=0, column=1, padx=5)

font_family_combobox.bind('<<ComboboxSelected>>', font_style)
font_size_combobox.bind('<<ComboboxSelected>>', font_size)

# Buttons section
bold_image = PhotoImage(file='images/bold.png')
boldButton = Button(tool_bar, image=bold_image, command=bold_text)
boldButton.grid(row=0, column=2, padx=5)

italic_image = PhotoImage(file='images/italic.png')
italicButton = Button(tool_bar, image=italic_image, command=italic_text)
italicButton.grid(row=0, column=3, padx=5)

underline_image = PhotoImage(file='images/underline.png')
underlineButton = Button(tool_bar, image=underline_image, command=underline_text)
underlineButton.grid(row=0, column=4, padx=5)

font_color_image = PhotoImage(file='images/font_color.png')
font_colorButton = Button(tool_bar, image=font_color_image, command=color_select)
font_colorButton.grid(row=0, column=5, padx=5)

left_align_image = PhotoImage(file='images/left.png')
left_alignButton = Button(tool_bar, image=left_align_image, command=align_left)
left_alignButton.grid(row=0, column=6, padx=5)

center_align_image = PhotoImage(file='images/center.png')
center_alignButton = Button(tool_bar, image=center_align_image, command=align_center)
center_alignButton.grid(row=0, column=7, padx=5)

right_align_image = PhotoImage(file='images/right.png')
right_alignButton = Button(tool_bar, image=right_align_image, command=align_right)
right_alignButton.grid(row=0, column=8, padx=5)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
textArea = Text(root, yscrollcommand=scrollbar.set, font=('arial', 12))
textArea.pack(fill=BOTH, expand=True)
scrollbar.config(command=textArea.yview)

status_bar = Label(root, text='Status Bar')
status_bar.pack(side=BOTTOM)

root.mainloop()
