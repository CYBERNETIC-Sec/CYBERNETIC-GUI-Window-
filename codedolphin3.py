from tkinter import*
from tkinter import scrolledtext
import threading,time

def table1():
    for i in range(100):
        line=txt1.get()+"\n"
        content1.insert(END,line)
        time.sleep(1)
def table2():
    line2=txt2.get()+"\n"
    content2.insert(END,line2)
    time.sleep(1)
def clicked():
    thread1=threading.Thread(target=table1)
    thread2=threading.Thread(target=table2)
    thread1.start()
    thread2.start()
# GUI PROGRAMMIMNG
window=Tk()
window.title("tables")
window.geometry("1000x700")
lbleading=Label(window,text="enter msg",font=("arial bold",18))
txt1=Entry(window,width=20,font=("arial bold",18))
txt2=Entry(window,width=20,font=("arial bold",18))
btn=Button(window,text="start",command=clicked,width=15,height=2,font=("arial bold",18))
content1=scrolledtext.ScrolledText(window,width=20,height=10,font=("arial bold",18))
content2=scrolledtext.ScrolledText(window,width=20,height=10,font=("arial bold",18))
# gui tables positions
lbleading.place(x=70,y=100)
txt1.place(x=200,y=100)
txt2.place(x=550,y=100)
btn.place(x=400,y=150)
content1.place(x=200,y=250)
content2.place(x=550,y=250)
window.mainloop()


