from tkinter import*

me=Tk()
me.geometry("354x460")
me.title("python calculator")
melabel = Label(me,text="Calculator",bg='Lavender',font=("Monaco",30,'italic'))
melabel.pack(side=TOP)
me.config(background='Purple')

textin=StringVar()
operator=""


def delete():
        a = itext.get()
        itext.delete(first=len(a)-1,last="end")
def fresult():
        if itext.get() == "":
                pass
        elif itext.get()[0] == "0":
                itext.delete(0,"end")
        else:
                c_res = itext.get()
                c_res = eval(c_res)
                clearf()
                itext.insert("end",c_res)
def clearf():
        itext.delete(0,"end")



     
itext=Entry(me,font=("Courier New",12,'bold'),textvar=textin,width=27,bd=8,bg='white')
itext.pack()

B1=Button(me,padx=14,pady=10,bd=4,bg='silver',command=lambda:itext.insert("end","1"),text="1",font=("Symbol",16,'bold'))
B1.place(x=10,y=100)

B2=Button(me,padx=14,pady=10,bd=4,bg='silver',command=lambda:itext.insert("end","2"),text="2",font=("Symbol",16,'bold'))
B2.place(x=10,y=170)

B3=Button(me,padx=14,pady=10,bd=4,bg='silver',command=lambda:itext.insert("end","3"),text="3",font=("Symbol",16,'bold'))
B3.place(x=10,y=240)

B4=Button(me,padx=14,pady=10,bd=4,bg='silver',command=lambda:itext.insert("end","4"),text="4",font=("Symbol",16,'bold'))
B4.place(x=75,y=100)

B5=Button(me,padx=14,pady=10,bd=4,bg='silver',command=lambda:itext.insert("end","5"),text="5",font=("Symbol",16,'bold'))
B5.place(x=75,y=170)

B6=Button(me,padx=14,pady=10,bd=4,bg='silver',command=lambda:itext.insert("end","6"),text="6",font=("Symbol",16,'bold'))
B6.place(x=75,y=240)

B7=Button(me,padx=14,pady=10,bd=4,bg='silver',command=lambda:itext.insert("end","7"),text="7",font=("Symbol",16,'bold'))
B7.place(x=140,y=100)

B8=Button(me,padx=14,pady=10,bd=4,bg='silver',command=lambda:itext.insert("end","8"),text="8",font=("Symbol",16,'bold'))
B8.place(x=140,y=170)

B9=Button(me,padx=14,pady=10,bd=4,bg='silver',command=lambda:itext.insert("end","9"),text="9",font=("Symbol",16,'bold'))
B9.place(x=140,y=240)

B0=Button(me,padx=14,pady=10,bd=4,bg='silver',command=lambda:itext.insert("end","0"),text="0",font=("Symbol",16,'bold'))
B0.place(x=10,y=310)

B_dot=Button(me,padx=50,pady=10,bd=4,bg='silver',command=lambda:itext.insert("end","."),text=".",font=("Symbol",16,'bold'))
B_dot.place(x=75,y=310)

B_pl=Button(me,padx=14,pady=10,bd=4,bg='silver',command=lambda:itext.insert("end","+"),text="+",font=("Symbol",16,'bold'))
B_pl.place(x=205,y=100)

B_sub=Button(me,padx=14,pady=10,bd=4,bg='silver',command=lambda:itext.insert("end","-"),text="-",font=("Symbol",16,'bold'))
B_sub.place(x=205,y=170)

B_ml=Button(me,padx=14,pady=10,bd=4,bg='silver',command=lambda:itext.insert("end","*"),text="*",font=("Symbol",16,'bold'))
B_ml.place(x=205,y=240)

B_div=Button(me,padx=17,pady=10,bd=4,bg='silver',command=lambda:itext.insert("end","/"),text="/",font=("Symbol",16,'bold'))
B_div.place(x=205,y=310)

B_delete = Button(me,padx=1,pady=10,bd=4,bg='silver',command=delete,text="del",font=("Courier New",16,'bold'))
B_delete.place(x=270,y=380)

B_clear=Button(me,padx=105,pady=10,bd=4,bg='silver',command=clearf,text="CE",font=("Courier New",16,'bold'))
B_clear.place(x=10,y=380)

B_equal=Button(me,padx=14,pady=119,bd=4,bg='silver',command=fresult,text="=",font=("Courier New",16,'bold'))
B_equal.place(x=270,y=100)
me.mainloop()