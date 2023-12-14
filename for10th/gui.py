from tkinter import *
from tkinter import messagebox

# from tkinter import messagebox
 

# 버튼 클릭 이벤트 핸들러
def okClick():
    url = txt.get()
    
    messagebox.showinfo("이름", name)

root = Tk()
lbl = Label(root, text="이름 : ")
lbl.grid(row=0, column=0)
txt = Entry(root)
txt.grid(row=0, column=1)
# 버튼 클릭 이벤트와 핸들러 정의
btn = Button(root, text="OK", command=okClick, width=15)
btn.grid(row=1, column=1)
 
root.mainloop()

