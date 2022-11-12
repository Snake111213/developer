from tkinter import Tk, StringVar, Radiobutton, Button,W

options = ['java','python','JS','GO','C#']
window = Tk()
window.geometry('220x150')
window.columnconfigure(1,weight=1)
window.columnconfigure(3,weight=3)
window.title('Select..')
var = StringVar()
var.set(0)

def reset():
    var.set(0)
    window.title('Select...')
    
def selected():
    window.title(f'{var.get()}')
    
for i in range(0, len(options)):
    Radiobutton(window, text=options[i], variable=var,value=options[i], command=selected).grid(padx=0,row=i,column=0,sticky=W)
    
Button(window, text="Reset", command=reset,width=15,height=5).grid(column=2,row=0,rowspan=5)

window.mainloop()