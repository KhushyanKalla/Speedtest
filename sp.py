from tkinter import *
import speedtest

def st():
    test=speedtest.Speedtest()
    test.get_best_server()
    check_1=str(round(test.download()/(10**6),3))+" Mbps "
    check_2=str(round(test.upload()/(10**6),3))+" Mbps "
    lab_check_1.config(text=check_1)
    lab_check_2.config(text=check_2)

test=Tk()
test.title("Speed Test")
test.geometry("500x300")
test.config(bg="black")

lab = Label(test,text="Speed Test By Python",font=("Time New Roman",30,"bold"),fg="grey",bg="black")
lab.place(x=60,y=10)

lab = Label(test,text="Download Speed:",font=("Time New Roman",20,"bold"),fg="grey",bg="black")
lab.place(x=40,y=100)

lab_check_1 = Label(test,text="00",font=("Time New Roman",15,"bold"),fg="green",bg="black")
lab_check_1.place(x=275,y=105)

lab = Label(test,text="Upload Speed:",font=("Time New Roman",20,"bold"),fg="grey",bg="black")
lab.place(x=40,y=200)

lab_check_2 = Label(test,text="00",font=("Time New Roman",15,"bold"),fg="green",bg="black")
lab_check_2.place(x=235,y=205)

but=Button(test,text="Tap For Speed Test",font=("Time New Roman",10,"bold"),fg="white",bg="navy",command=st)
but.place(x=190,y=245)
test.mainloop()