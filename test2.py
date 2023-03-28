from tkinter import *

#สร้างหน้าต่างหน้าจอโปแกรมชื่อ root
root = Tk()           #เรียกโมดูล Tk เพื่อสร้างหน้าต่าง
root.title("My GUI")

#กำหนดขนาดหน้าต่างหน้าจอ ต้องกำหนดก่อน mainloop
root.geometry("500x200")  # +คือกำหนดพิกัดตำแหน่งแสดงหน้าต่างในหน้าจอ ในแกน X,Y

#สร้างกล่องข้อความ
txt=StringVar()  #ตัวแปลเก็บข้อความ
Entry(root,textvariable=txt).pack()


root.mainloop()