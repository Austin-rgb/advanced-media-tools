#!amt/Scripts/python
from tkinter import Tk, Button, Label, Entry, filedialog, Frame
from lib.mp42mp3 import mp42mp3
from lib.cropmp3 import crop_mp3
from lib.xformat import change_format

root = Tk()
def get_file():
    diag=filedialog.FileDialog(root,'Choose file')
    file = diag.go('E:/')
    print(f'got file: {file}')
    return file

def _mp42mp3():
    mp42mp3(get_file())

class NewLabel(Frame):
        def __init__(self,root,*args,name='new label',**kwargs,):
            name_label = Label(self,text=name)
            name_label.pack()
            entry = Entry(self,name=name)
            entry.pack()
            
class Form(Frame):
    def __init__(self,params:tuple,binding,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.params = params
        self.binding = binding
    
        for arg in params:
            row = NewLabel(self,name=arg)
            row.pack()

        finish_button = Button(self,text='OK',command=self.close)
        finish_button.pack()

    def close(self):
        self.finish()
        self.binding(*self.params)

    def finish(self):
        for i in range(len(self.params)):
            self.params[i]=self.children.get(self.params[i]).children.get(self.params[i]).get()
    

class CropMp3(Frame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        btn_choose_file = Button(self,text='Choose File', command=None)

def _change_format():
    change_format(get_file(),'mp3')
def _crop_mp3():
    form = Form(('start', 'end'),crop_mp3)
    form.pack()
    

btn_mp42mp3 = Button(root,text='Mp3 from Mp4', command=_mp42mp3)
btn_mp42mp3.pack()
btn_cropmp3 = Button(root,text='Crop mp3',command=_crop_mp3)
btn_cropmp3.pack()
root.mainloop()
