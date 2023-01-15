from tkinter import *
from time import *

window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")


fnameList = ["jeju1.gif", "서울.png", "jeju3.gif", "로마.png"]
photoList = [None] * 4
num = 0

def clickNext() :
    global num
    num += 1
    if num > 3 :
        num = 0
    photo = PhotoImage(file = "gif/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image= photo

def clickPrev() :
    global num
    num -= 1
    if num < 0 :
        num = 3
    photo = PhotoImage(file = "gif/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image= photo

btnPrev = Button(window, text = "<< 이전", command = clickPrev)
btnNext = Button(window, text = "다음 >>", command = clickNext)

photo = PhotoImage(file = "gif/" + fnameList[0])
pLabel = Label(window, image = photo)

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
pLabel.place(x = 15, y = 50)

window.mainloop()