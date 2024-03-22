from tkinter import *
from tkinter.ttk import *
from tkinter import font, colorchooser, filedialog, messagebox
import os

# Functions
file_url = ''


def new_file():
    global file_url
    file_url = ''
    textArea.delete(0.0, END)


def open_file():
    global file_url
    file_url = filedialog.askopenfilename(initialdir=str(os.getcwd), title='Select File',
                                          filetypes=(('Text File', 'txt'), ('All files', '*.*')))
    if file_url != '':
        with open(file_url, 'r') as file:
            textArea.insert(0.0, file.read())
    root.title(os.path.basename(file_url))


def save_file():
    if file_url == '':
        save_url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                            filetypes=(('Text File', 'txt'), ('All files', '*.*')))

        content = textArea.get(0.0, END)
        save_url.write(content)
        save_url.close()
    else:
        content = textArea.get(0.0, END)
        with open(file_url, 'w') as file:
            file.write(content)


def save_as_file():
    save_url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                        filetypes=(('Text File', 'txt'), ('All files', '*.*')))
    content = textArea.get(0.0, END)
    save_url.write(content)
    save_url.close()


def exit_app():
    if textArea.edit_modified():
        result = messagebox.askyesnocancel('Save changes', 'Do you wont save the changes?')
        if result is True:
            content = textArea.get(0.0, END)
            if file_url == '':
                save_url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                                    filetypes=(('Text File', 'txt'), ('All files', '*.*')))
                save_url.write(content)
                save_url.close()
            else:
                with open(file_url, 'w') as file:
                    file.write(content)
            root.destroy()
        elif result is False:
            root.destroy()
        else:
            pass
    else:
        root.destroy()


def status_bar_function(event):
    if textArea.edit_modified():
        words = len(textArea.get(0.0, END).split())
        characters = len(textArea.get(0.0, 'end-1c').replace(' ', ''))
        status_bar.config(text=f'Characters: {characters} Words: {words}')

    textArea.edit_modified(False)


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


def find():
    # functions
    def find_word():
        textArea.tag_delete('match')
        start_position = '1.0'
        word = find_entry_field.get()
        if word:
            while True:
                start_position = textArea.search(word, start_position, stopindex=END)
                if not start_position:
                    break
                end_position = f'{start_position}+{len(word)}c'
                textArea.tag_add('match', start_position, end_position)
                textArea.tag_config('match', foreground='red', background='yellow')
                start_position = end_position

    def replace_word():
        pass

    # GUI
    find_window = Toplevel()
    find_window.title('Find')
    find_window.geometry("450x250+500+200")
    find_window.resizable(False, False)

    label_frame = LabelFrame(find_window, text='Find/Replace')
    label_frame.pack(pady=50)

    find_label = Label(label_frame, text='Find')
    find_label.grid(row=0, column=0, padx=5, pady=5)
    find_entry_field = Entry(label_frame)
    find_entry_field.grid(row=0, column=1, padx=5, pady=5)

    replace_label = Label(label_frame, text='Replace')
    replace_label.grid(row=1, column=0, padx=5, pady=5)
    replace_entry_field = Entry(label_frame)
    replace_entry_field.grid(row=1, column=1, padx=5, pady=5)

    find_btn = Button(label_frame, text='Find', command=find_word)
    find_btn.grid(row=2, column=0, padx=5, pady=5)
    replace_btn = Button(label_frame, text='Replace', command=replace_word)
    replace_btn.grid(row=2, column=1, padx=5, pady=5)

    find_window.mainloop()


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
filemenu.add_command(label='New', accelerator='Ctrl+N', command=new_file)
filemenu.add_command(label='Open', accelerator='Ctrl+O', command=open_file)
filemenu.add_command(label='Save', accelerator='Ctrl+S', command=save_file)
filemenu.add_command(label='Save As', accelerator='Ctrl+Alt+S', command=save_as_file)
filemenu.add_separator()
filemenu.add_command(label='Exit', accelerator='Ctrl+Q', command=exit_app)
menubar.add_cascade(label='File', menu=filemenu)

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

textArea.bind('<<Modified>>', status_bar_function)

# Edit menu
editmenu = Menu(menubar, tearoff=False)
editmenu.add_command(label='Cut', accelerator='Ctrl+X', command=lambda: textArea.event_generate('<Control x>'))
editmenu.add_command(label='Copy', accelerator='Ctrl+C', command=lambda: textArea.event_generate('<Control c>'))
editmenu.add_command(label='Paste', accelerator='Ctrl+V', command=lambda: textArea.event_generate('<Control v>'))
editmenu.add_command(label='Clear', accelerator='Ctrl+Alt+X', command=lambda: textArea.delete(0.0, END))
editmenu.add_command(label='Find', accelerator='Ctrl+F', command=find)
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

root.mainloop()
