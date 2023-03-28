from tkinter import *

#สร้างหน้าต่างชื่อ root
root = Tk()
root.title("My GUI Natdanai")
#home =Tk()
#home.title("My home page")

#ใส่จ้อความ
myLabel = Label(root,text="Hello World",fg="red",font= 100,bg="red").pack()
myLabel2 = Label(text="Natdanai Chaiyachat",fg="yellow",bg="brown",font=200).pack()
myLabel1 = Label(root,text="BLACK PINK",bg="pink",font=60,fg="black").pack()

#สร้างกล่องข้อความ
txt1=StringVar()  #ตัวแปลเก็บข้อความ
Entry(root,textvariable=txt1).pack()

#ใ่ส่ฟังก์ชั่นให้ปุ่มหลังการกดต้องสร้างก่อนสร้างปุ่ม
def showMessage():
    myLabel3 = Label(text="Hello !!!",fg="yellow",bg="black",font=200).pack()
    message = txt1.get()
    Label(root,text=message,fg ="black",bg="pink",font=20).pack()
    
def openPageReport():
    page2 = Tk()
    page2.title("page report")
    page2.geometry("800x450+500+230")

#ใส่ปุ่ม widget button
btn1 = Button(root,text = "เพิ่มสมาชิก",bg = "pink",font = 60,fg = "black",command=showMessage).pack()
btn2 = Button(root,text = "รายชื่อสมาชิก",bg = "pink",font = 60,fg = "black",command=openPageReport).pack()



#กำหนดขนาดและตำแหน่งหน้าจอด้วย geometry
root.geometry("800x450+500+200")

root.mainloop()  #ต้องอยู่ล่างสุด
