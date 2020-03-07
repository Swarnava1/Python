from tkinter import *

class Calculator:

    def __init__(self):
        self.root=Tk()

        self.result=Label(self.root)
        self.result.grid(row=0,column=0)

        Button(text="1",width=6,height=4,bg="red",command=lambda:self.get_num("1")).grid(row=1,column=0)
        Button(text="2",width=6,height=4,bg="red",command=lambda:self.get_num("2")).grid(row=1,column=1)
        Button(text="3", width=6, height=4, bg="red",command=lambda:self.get_num("3")).grid(row=1, column=2)
        Button(text="+", width=6, height=4, bg="red",command=lambda:self.get_operator("+")).grid(row=1, column=3)

        Button(text="4", width=6, height=4, bg="red",command=lambda:self.get_num("4")).grid(row=2, column=0)
        Button(text="5", width=6, height=4, bg="red",command=lambda:self.get_num("5")).grid(row=2, column=1)
        Button(text="6", width=6, height=4, bg="red",command=lambda:self.get_num("6")).grid(row=2, column=2)
        Button(text="-", width=6, height=4, bg="red",command=lambda:self.get_operator("-")).grid(row=2, column=3)

        Button(text="7", width=6, height=4, bg="red",command=lambda:self.get_num("7")).grid(row=3, column=0)
        Button(text="8", width=6, height=4, bg="red",command=lambda:self.get_num("8")).grid(row=3, column=1)
        Button(text="9", width=6, height=4, bg="red",command=lambda:self.get_num("9")).grid(row=3, column=2)
        Button(text="*", width=6, height=4, bg="red",command=lambda:self.get_operator("*")).grid(row=3, column=3)

        Button(text="0", width=6, height=4, bg="red",command=lambda:self.get_num("0")).grid(row=4, column=0)
        Button(text="/", width=6, height=4, bg="red",command=lambda:self.get_operator("/")).grid(row=4, column=1)
        Button(text="C", width=6, height=4, bg="red",command=lambda:self.clear()).grid(row=4, column=2)
        Button(text="=", width=6, height=4, bg="red",command=lambda:self.get_result()).grid(row=4, column=3)

        self.root.mainloop()

    def get_num(self,num):

        new_num=self.result['text']+num         #123+2=125
        self.result.configure(text=new_num)

    def clear(self):
        self.result.configure(text="")

    def get_operator(self,operator):
        self.first_num=float(self.result['text'])
        self.operator=operator
        self.result.configure(text="")

    def get_result(self):
        self.second_num=float(self.result['text'])

        if self.operator=="+":
            self.result.configure(text=str(self.first_num+self.second_num))
        elif self.operator=="-":
            self.result.configure(text=str(self.first_num - self.second_num))
        elif self.operator=="*":
            self.result.configure(text=str(self.first_num * self.second_num))
        else:
            if self.second_num==0:
                self.result.configure(text="Gadha")
            else:
                self.result.configure(text=str(self.first_num / self.second_num))




obj=Calculator()

