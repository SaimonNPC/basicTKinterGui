from tkinter import *

#สร้างหน้าต่างหน้าจอโปแกรมชื่อ root
root = Tk()           #เรียกโมดูล Tk เพื่อสร้างหน้าต่าง
root.title("My GUI")

#กำหนดขนาดหน้าต่างหน้าจอ ต้องกำหนดก่อน mainloop
root.geometry("500x200")  # +คือกำหนดพิกัดตำแหน่งแสดงหน้าต่างในหน้าจอ ในแกน X,Y


#สร้างหน้าจอ 2 หลังกดปุ่มสั่ง openWindow2
window2 = Tk()
window2.title("ทักทาย blink")
window2.geometry("500x200")
    
# ใส่ข้อความในหน้าจอ
# pack กำหนดให้ไปทำงานในหน้าต่าง จะเริ่มตรงกลางบนสุด
# # properties fg คือสีตัวหนังสือ font= คือขนาดตัวหนังสือ 
# place (x=0,y=0)เลือกตำแหน่งวางx,yของตัวหนังสือ pixel 
# grid เลือกตำแหน่งวางx,yของตัวหนังสือวางแบบตาราง 

myLabel1 = Label(root,text="BLACK PINK",fg="pink",font=60,bg="black").pack()
#myLabel2 = Label(root,text="IN YOUR AREA",fg="black",bg="pink",font=20).grid(row=1,column=2)


#สร้างกล่องข้อความ
txt=StringVar()  #ตัวแปลเก็บข้อความ
Entry(root,textvariable=txt).pack()


#สร้าง function ให้เกิดหลังจากกดปุ่ม ต้องสร้างก่อนสร้างปุ่ม
def showMessage():
    myLabel2 = Label(root,text="Hello Blink!",fg="black",bg="pink",font=20).pack()
    message = txt.get() 
    print()
    Label(root,text=message,fg="black",bg="pink",font=20).pack()

def showMessage2():
    Label(window2,text="เตรียมพร้อม",fg="black",bg="pink",font=20).pack()




#myLabel2 = Label(window2,text="Blink รายงานตัว",fg="black",bg="pink",font=20).pack()



#ใส้ปุ่ม 
btn1 = Button(text="BORN PINK",fg="pink",bg="white",command=showMessage).pack()

#btn2 = Button(root,text="เปิดรายงาน",fg="pink",bg="white",command=openWindow2).pack()

btn3 = Button(text="จำนวน Blink",fg="pink",bg="white",command=showMessage2).pack()








root.mainloop()      #สั่ง root ทำงานไปเรื่อยๆ

