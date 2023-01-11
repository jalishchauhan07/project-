import tkinter
from tkinter import messagebox as msg
from tkinter import *

class Examination(tkinter.Tk):
    ques=["Who Developed C?",
      "Who Developed Java ?","Who Developed PHP?"]
    a="|____________________\n| Correct Answer \n|____________________|\n Dennis Ritchie\n| ____________________ |\n James Gosling\n |____________________|\n Rasmus Lerdorf \n|____________________|"

    s="|____________________|\n User Answer \n|____________________|\n"
    def __init__(self):
        super().__init__()
        self.Op1=[' Martin Richards',' Ken Thompson','Dennis Ritchie','Rasmus Lerdorf']
        self.Op2=["Dennis Ritchie",'Rasmus Lerdorf',"Martin Richards","James Gosling"]
        self.Op3=['Rasmus Lerdorf',"Martin Richards","Ken Thompson",'Dennis Ritchie']
        self.Op4=['Ken Thompson','James Gosling','Rasmus Lerdorf',"Martin Richards"]
        self.title("Examination ")
        self.no=0
        self.n=0
        self.geometry("400x200")
        self.setComponent()
        
    def radioCheck(self):
        num=self.r.get()
        self.ans=[]
        if num==1:
            self.ans.append(self.Op1[self.n])
            self.s+=self.Op1[self.n]+"\n"+"|____________________|\n"
        elif num==2:
            self.ans.append(self.Op2[self.n])
            self.s+=self.Op2[self.n]+"\n "+"|____________________|\n"
        elif num==3:
            self.ans.append(self.Op3[self.n])
            self.s+=self.Op3[self.n]+"\n"+"|____________________|\n"
        elif num==4:
            self.ans.append(self.Op4[self.n])
            self.s+=self.Op4[self.n]+"\n"+"|____________________|\n"


        
    def next_Button(self):
        try:
            self.no+=1
            self.n+=1
            self.text.configure(text=self.ques[self.no])
            self.op1.configure(text=self.Op1[self.n])
            self.op2.configure(text=self.Op2[self.n])
            self.op3.configure(text=self.Op3[self.n])
            self.op4.configure(text=self.Op4[self.n])
        except IndexError :
            msg.showwarning('Warning  ',' Finished Question')
            tk=tkinter.Tk()
            tkinter.Label(tk,text=self.s).grid(row=0,column=0)
            tkinter.Label(tk,text=self.a).grid(row=0,column=1)



    def pre_Button(self):
        try:
            if self.no<=0:
                raise IndexError()
            self.no-=1
            self.text.configure(text=self.ques[self.no])
            self.op1.configure(text=self.Op1[self.no])
            self.op2.configure(text=self.Op2[self.no])
            self.op3.configure(text=self.Op3[self.no])
            self.op4.configure(text=self.Op4[self.no])

        except IndexError :
            msg.showwarning('Warning  ',' Please click on next button')

            
    def setComponent(self):
        self.r=tkinter.IntVar(self)
        self.f1=tkinter.LabelFrame(self,width=50)
        self.f1.grid(row=0,column=0)
        self.f2=tkinter.LabelFrame(self,width=50)
        self.f2.grid(row=1)
        self.next=tkinter.Button(self.f2,text="Next",width=10,command=self.next_Button)
        self.previous=tkinter.Button(self.f2,text="Previous",width=10,command=self.pre_Button)
        self.text=tkinter.Label(self.f1,text=self.ques[self.no])
        self.text.grid(row=0,padx=50)
        self.op1=tkinter.Radiobutton(self.f2,text=self.Op1[self.n],variable=self.r,value=1,command=self.radioCheck)
        self.op1.grid(row=1,padx=50)
        self.op2=tkinter.Radiobutton(self.f2,text=self.Op2[self.n],variable=self.r,value=2,command=self.radioCheck)
        self.op2.grid(row=1,column=2)
        self.op3=tkinter.Radiobutton(self.f2,text=self.Op3[self.n],variable=self.r,value=3,command=self.radioCheck)
        self.op3.grid(row=2,padx=50)
        self.op4=tkinter.Radiobutton(self.f2,text=self.Op4[self.n],variable=self.r,value=4,command=self.radioCheck)
        self.op4.grid(row=2,column=2,padx=50,pady=40)

        self.next.grid(row=3,column=2)
        self.previous.grid(row=3)


        
        
   
e=Examination()
