
from tkinter import *
import os
from tkinter import ttk,filedialog,messagebox
from tkinter.filedialog import asksaveasfile
tk = Tk()

def convert_img_pdf(filename):
    from PIL import Image
    img_rgb = list(map(lambda x: Image.open(x).convert('RGB').rotate(-90),image_list))
    img_rgb[-1].save(filename,save_all=True, append_images=img_rgb[:-1])

def load_tkiner_window():
    tk.geometry("250x350")
    tk.resizable(False, False)
    tk.title('PDF Covert')
    Lb1 = Listbox(tk,height=8, width=26, bg="bisque3")
    Lb1.place(x=45, y=110)
    ttk.Label(tk, text = "PDF Convertor",font=(None, 15)).place(x=60, y=30)
    ttk.Button(tk,text="Select IMG..", width=25,command=lambda: img_dialog_box(Lb1)).place(x=45, y=70)
    ttk.Button(tk,text="Delete..", width=25,command=lambda: delete_file(Lb1)).place(x=45, y=250)
    ttk.Button(tk, text="Submit", width=25, command=lambda: save_dialog_box()).place(x=45, y=280)
    ttk.Label(tk, text="Developed By Andrey",font=(None, 10)).place(x=5, y=325)
    tk.mainloop()

def save_dialog_box():
    if not image_list:
        messagebox.showinfo("Error",'No file selected')
    else:
        file = asksaveasfile(initialfile='Untitled.pdf',
                             defaultextension=".pdf", filetypes=[("PDF document", "*.pdf")])
        if file:
            convert_img_pdf(file.name)


def img_dialog_box(Lb1):
    global count
    filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(
    ("JPG", "*.jpg"), ("PNG", "*.png"), ("JPG", "*.jpeg")))
    if filename != '':
        image_list.append(filename)
        Lb1.insert(count,os.path.basename(filename))
        print(image_list)
        count += 1
def delete_file(Lb1):
    global count
    if not not image_list:
        image_list.pop(-1)
        Lb1.delete(count-1)
        count -=1
    print(image_list)
if __name__ == '__main__':
    count = 0
    image_list = []
    load_tkiner_window()