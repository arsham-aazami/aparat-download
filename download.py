import requests
import tkinter
from tkinter import Entry , Button ,Label ,messagebox
class dawnload :
    def __init__(self,Link,Format):
       self.Link=Link
       self.Format=Format 
    def dawnload(self):
        data=requests.get(self.Link).content
        Formatfile=f'./data.{self.Format}'
        with open(Formatfile , "wb") as f:
            f.write(data)
def dawnload ():
    try:
        dawnloadlink=dawnload(entryl.get() , entryf.get())
        dawnloadlink.dawnload()
        messagebox.showinfo("dawnload-state","your dawnload is complete !")
    except:
         messagebox.showerror("dawnload-state","your dawnload is not complete !")
    

window=tkinter.Tk()
window.geometry("400x155")
window.resizable(False,False)
window.eval('tk::PlaceWindow . center')
window.title("dawnload")
label=Label(master=window , text="please enter your link :" , justify="left" , anchor="w" ,font=("Arial" , 10))
label.pack(fill="x" ,padx=5 )
entryl = Entry(master=window,bd=4,font=("Arial",10))
entryl.pack(fill="x" ,padx=5,pady=5)
labelf=Label(master=window , text="please enter your format :" , justify="left" , anchor="w" ,font=("Arial" , 10))
labelf.pack(fill="x" ,padx=5 )
entryf = Entry(master=window,bd=4,font=("Arial",10))
entryf.pack(fill="x" ,padx=5,pady=5)

btn=Button(master=window  , text="dawnload" ,bg="green" , font=("Arial",10) ,command=dawnload)
btn.pack(fill="x" , padx=7 , pady=7)

window.mainloop()
