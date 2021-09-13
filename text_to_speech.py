import tkinter
import pyttsx3

root = tkinter.Tk()
root.geometry('300x220')
root.title('FramesandPackets Text To Speech App')
root.configure(background='#b9bdc9')    #we can use hex color values :D

Header_Label = tkinter.Label(root, text="\nText To Speech",
                            fg = "#141416",
                            bg = "#b9bdc9",
                            font = "Helvetica 12 bold").pack()


Msg = tkinter.StringVar()
enter_t = tkinter.Label(root,text ="Enter Text:",
                font = 'Helvetica 10 bold',
                bg ='#b9bdc9').place(x=100,y=80)

entry_field = tkinter.Entry(root ,textvariable = Msg, width ='35').place(x=35,y=100)

def exit():
    root.destroy()

def restart():
    Msg.set("")

def Text_to_speech():
    message_get = Msg.get()
    engine = pyttsx3.init()
    engine.say(message_get)
    engine.runAndWait()

tkinter.Button(root, text = "Play!", font = 'Helvetica 10 bold' , command = Text_to_speech ,width = '6', bg = '#445768', fg = '#e2e2e2').place(x=15,y=140)
tkinter.Button(root, font = 'Helvetica 10 bold',text = 'Clear Text!', width = '9' , command = restart, bg = '#445768', fg = '#e2e2e2').place(x=105 , y = 140)
tkinter.Button(root, font = 'Helvetica 10 bold',text = 'Exit!', width = '6' , command = exit, bg = '#c00d11').place(x=210 , y = 140)

Footer_Label = tkinter.Label(root, text="created by @framesandpackets",
                             fg = "#141416",
                             bg = "#b9bdc9",
                             font = "Helvetica 8").place(x=135 , y = 200)

root.mainloop()
