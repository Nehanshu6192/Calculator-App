from tkinter import *
#from tkinter import ttk
root=Tk()
root.title("CALCULATOR APP #(By Nehanshu)")
root.resizable(False,False)
#########Entry Box######################
enrty_box= Entry(font= "times 14 bold", width=32, bd=10, justify= RIGHT, bg= "#e6e6fa")
enrty_box.insert(0,"0")
enrty_box.place(x=20, y=10)
#################Functions###########################
def enterNumber(x):
    if enrty_box.get()=="0":
        enrty_box.delete(0, 'end')
        enrty_box.insert(0, str(x)) 
    else: 
        length= len(enrty_box.get())
        enrty_box.insert(length, str (x))

def enterOperator(x):
    if enrty_box.get() !="0":
        length= len(enrty_box.get())
        enrty_box.insert(length, btn_operator[x]["text"])
        
def funcClear():
    enrty_box.delete(0, END)
    enrty_box.insert(0, "0")     

result= 0
result_list= []
def isEqaulto():
    content = enrty_box.get()
    print(content)
    result = eval(content)
    print(result)
    enrty_box.delete(0, END)
    enrty_box.insert(0,str(result))

    result_list.append(content)
    result_list.reverse()
    statusBar.configure(text= 'History:'+'|'.join(result_list[:5]))
def funcDelete():
    length= len(enrty_box.get())
    enrty_box.delete(length-1, 'end')
    if length==1:
        enrty_box.insert(0,"0")


def funcPercentage():
    number= enrty_box.get()
    

def funcBracket():
    enrty_box.insert(0, "( )")

#################buttons################
btn_numbers= []

for i in range(10,0,-1):
    btn_numbers.append(Button(width=4, text=str(i), font="times 15 bold", bd=5, command= lambda x=i: enterNumber(x)))

btn_text=1
for i in range(0,3):
    for j in range(0,3):
        btn_numbers[btn_text].place(x=25+j*90, y=140+i*70)
        btn_text+=1

##################Operator Button##########################
btn_operator= []
for i in range(4):
    btn_operator.append(Button(width= 4, font= 'times 15 bold', bd= 5, command= lambda x=i: enterOperator(x)))

btn_operator[0]['text']= "/"
btn_operator[1]['text']= "*"
btn_operator[2]['text']= "-"
btn_operator[3]['text']= "+"

for i in range(4):
    btn_operator[i].place(x=290, y=70+i*70)
#######################Other_buttons#########################
btn_zero= Button(width=4, text= '0', font= 'times 15 bold', bd=5, command= lambda x=0: enterNumber(x))
btn_zero.place(x= 115, y= 350)
btn_dot= Button(width=4, text= '.', font= 'times 15 bold', bd=5, command= lambda x=".":enterNumber(x))
btn_dot.place(x= 25, y= 350)
btn_equal= Button(width=4, text= '=', font= 'times 15 bold', bd=5, command= isEqaulto)
btn_equal.place(x=295, y=350)
btn_clear= Button(width=4, text= 'AC', font= 'times 15 bold', bd=5, command=funcClear )
btn_clear.place(x= 25, y= 70)
btn_Delete= Button(width=4, text="D", font= 'times 15 bold', bd=5, command= funcDelete)
btn_Delete.place(x= 115, y= 70)
btn_percentage= Button(width=4, text="%", font= 'times 15 bold', bd=5, command= funcPercentage)
btn_percentage.place(x= 205, y= 70)
btn_brackets= Button(width=4, text="( )", font= 'times 15 bold', bd=5, command= funcBracket)
btn_brackets.place(x= 205, y= 350)

statusBar=Label(root,text='History : ',relief=SUNKEN,height=3,anchor=W,font='verdana 11 bold')
statusBar.pack(side=BOTTOM,fill=X)

root.geometry("380x480+850+200")
root.mainloop()