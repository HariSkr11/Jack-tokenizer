from Tokenizer import *
from tkinter import *
from tkinter import ttk
ws = Tk()
filename = ""
def get_input():
    filename=disp_tf.get()
    Tokenizer.read_lines(filename)
    L2 = Label(ws,text="Tokenizing successful",background="#2C3333",foreground="#E7F6F2")
    L2.place(x=140,y=230)
def close():
    ws.destroy()
ws.title('Jack Tokenizer')
ws.geometry('380x300')
ws.config(bg='#2C3333')
lABEL_FR = LabelFrame(ws,background="#395B64").pack(expand="yes",fill="both")
l1 = Label(lABEL_FR,text=" JACK TOKENIZER ",background="#2C3333",foreground = "#E7F6F2", font = ("Comic Sans MS", 14,"bold")).pack()
name_label = Label(ws,text = "ENTER THE PATH OF THE JACK FILE TO BE TOKENIZED",background="#2C3333",foreground="#E7F6F2",font=("Comic Sans MS",9)).place(x=10,y=50)
disp_tf = ttk.Entry(lABEL_FR,textvariable=filename,width=20,background="#A5C9CA",foreground="#2C3333",font=('Comic Sans MS', 14))
disp_tf.place(x=70,y=110)
btn = Button(ws,text='SUBMIT',relief=SOLID,command=get_input,background="#2C3333",foreground="#E7F6F2")
btn1 = Button(ws,text='CLOSE',relief=SOLID,command=close,background="#2C3333",foreground="#E7F6F2")
btn.place(x=130,y=170)
btn1.place(x=200,y=170)
ws.mainloop()
