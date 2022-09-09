from tkinter import messagebox
import pywhatkit
import tkinter as tk
from tkinter import *
    
window = tk.Tk()
window.title("Bot for Whatsapp")
window.geometry("1000x500")
Label(window, text='Enter Number: ').grid(row=0)
Label(window, text='Enter Message Text: ').grid(row=1)
Label(window, text='Enter Hour: ').grid(row=2)
Label(window, text='Enter Minutes: ').grid(row=3)
Label(window, text='Enter Message for image: ').grid(row=4)
Label(window, text='Enter Group ID: ').grid(row=5)
Label(window, text='Enter name of image: ').grid(row=6)
phone_number = Entry(window)
text_message = Entry(window)
name_image = Entry(window)
hour = Entry(window)
min = Entry(window)
message_for_image = Entry(window)
id_group = Entry(window)
phone_number.grid(row=0, column=1)
text_message.grid(row=1, column=1)
hour.grid(row=2, column=1)
min.grid(row=3, column=1)
message_for_image.grid(row=4, column=1)
id_group.grid(row=5, column=1)
name_image.grid(row=6, column=1)
name_image.config(state="disabled")
phone_number.config(state="disabled")
text_message.config(state="disabled")
hour.config(state="disabled")
min.config(state="disabled")
id_group.config(state="disabled")
message_for_image.config(state="disabled")
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()

def CheckClicked1():
    if CheckVar1.get():
        phone_number.config(state="normal")
        text_message.config(state="normal")
        hour.config(state="normal")
        min.config(state="normal")
        button["state"] = NORMAL
    else:
        phone_number.config(state="disabled")
        text_message.config(state="disabled")
        hour.config(state="disabled")
        min.config(state="disabled")
        button["state"] = DISABLED

def CheckClicked2():
    if CheckVar2.get():
        id_group.config(state="normal")
        text_message.config(state="normal")
        hour.config(state="normal")
        min.config(state="normal")
        button2["state"] = NORMAL
    else:
        id_group.config(state="disabled")
        text_message.config(state="disabled")
        hour.config(state="disabled")
        min.config(state="disabled")
        button2["state"] = DISABLED

def CheckClicked3():
    if CheckVar3.get():
        phone_number.config(state="normal")
        message_for_image.config(state="normal")
        name_image.config(state="normal") 
        button3["state"] = NORMAL
    else:
        phone_number.config(state="disabled")
        message_for_image.config(state="disabled")
        name_image.config(state="disabled")
        button3["state"] = DISABLED

C1 = Checkbutton(window, text = "Message", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20 ,command=CheckClicked1)
C2 = Checkbutton(window, text = "Message to Group", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20,command=CheckClicked2)
C3 = Checkbutton(window, text = "Message with Image", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20,command=CheckClicked3)
C1.grid(row=0,column=3)
C2.grid(row=0,column=2)
C3.grid(row=0,column=4)

def send_message_only():
    if not phone_number.get():
        messagebox.showerror("Error","The field Number cannot be empty")
    elif not text_message.get():
        messagebox.showerror("Error","The field Message cannot be empty")
    elif not hour.get():
        messagebox.showerror("Error","The field Hour cannot be empty")
    elif not min.get():
        messagebox.showerror("Error","The field Min cannot be empty")
    else:
        message = str(text_message.get())
        number = str(phone_number.get())
        hours = int(hour.get())
        minutes = int(min.get())
        pywhatkit.sendwhatmsg(number,message,hours,minutes)    
        
def send_message_to_group():
    if not text_message.get():
        messagebox.showerror("Error","The field Message cannot be empty")
    elif not hour.get():
        messagebox.showerror("Error","The field Hour cannot be empty")
    elif not min.get():
        messagebox.showerror("Error","The field Min cannot be empty")
    elif not id_group.get():
        messagebox.showerror("Error","The field Group ID cannot be empty")
    else:
        id = str(id_group.get())
        message = str(text_message.get())
        hours = int(hour.get())
        minutes = int(min.get())
        pywhatkit.sendwhatmsg_to_group(id_group,message,hours,minutes)    
        
def send_image():
    if not phone_number.get():
        messagebox.showerror("Error","The field Number cannot be empty")
    else:
        number = str(phone_number.get())
        message = str(message_for_image.get())
        image = str(name_image.get())
        if message_for_image.get():
            pywhatkit.sendwhats_image(number,image,message,15)
        else:
            pywhatkit.sendwhats_image(number,image,15)
    
button = tk.Button(window, text='Send message only', width=25, command=send_message_only)
button2 = tk.Button(window, text='Send message to group', width=25, command=send_message_to_group)
button3 = tk.Button(window, text='Send image', width=25, command=send_image)
button["state"] = DISABLED
button2["state"] = DISABLED
button3["state"] = DISABLED
button.grid(row=3,column=2)
button2.grid(row=4,column=2)
button3.grid(row=5,column=2)
button4 = tk.Button(window, text='Exit', width=25, command=window.destroy)
button4.grid(row=6,column=3)
window.mainloop()