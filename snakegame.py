"""
    Snake Game Project
    เริ่ม : 27/11/2563 - 20.26
    แก้ไข : 27/11/2563 - 23.39 [Veerawat]
           05/12/2563 - 17.11 [Sirichai]
           05/12/2563 - 14.38 [Wanatchporn]
           06/12/2563 - 22.11 [Veerawat]
           12/12/2563 - 01.06 [Veerawat]
           12/12/2563 - 15.35 [Wanatchporn]
    -----------------------------------------------------
    Reference
    - Introduction To Game Building With Python's Turtle Module : https://www.edureka.co/blog/python-turtle-module/
"""

""" Import """
import turtle # นำ Module Turtle มาใช้ในการดำเนินการเกี่ยวกับตัวงู
import time # นำ Module Time มาใช้ในการสร้าง delay
import random # นำ Module Random มาใช้ในการสุ่มตำแหน่งของอาหาร
import tkinter as tk # นำ Module tkinter มาใช้ในการสร้างหน้า home

""" Home Page for Start Button """
def home_page():
    """ Use tkinter to create Home Page """
    start = tk.Tk()
    icon = tk.PhotoImage(file='pic/snakehead.png')
    start.option_add("*Font", "consolas 40"), start.title('SnakeGame Project'), start.iconphoto(0, icon)
    """ ฟังก์ชันเมื่อกดปุ่ม """
    def clicked():
        start.destroy()
        return 0
    tk.Button(start, text = "SnakeGame Project", width = 20).pack()
    tk.Button(start, text = "Start", bg = "blue", bd = 10, command=clicked).pack(fill = tk.X)
    start.mainloop()

home_page() # เริ่มหน้า Home
""" สร้างหน้าจอสำหรับการเล่นโดย Turtle Module """
win = turtle.Screen() # สร้างหน้าจอ
win.register_shape('pic/grassterrain.gif')
# Title ของหน้าจอที่สร้างขึ้น, เปลี่ยนสีพื้นหลัง, ตั้งค่าขนาดหน้าจอ, ตั้งให้หน้าจอไม่มีการปรับแต่งอะไรเพิ่ม
win.title("SnakeGame Project"), win.bgpic("pic/grassterrain.gif"), win.setup(width=600, height=600), win.tracer(0)

""" สร้างหัวงูเพื่อใช้ในการเล่น """
# import รูป สำหรับใช้เป็นหัวงู
win.register_shape('pic/snakehead.gif')
win.register_shape('pic/snakehead_down.gif')
win.register_shape('pic/snakehead_right.gif')
win.register_shape('pic/snakehead_left.gif')
head = turtle.Turtle() # สร้าง Turtle ซึ่งในที่นี้ใช้แทนหัวงู
# กำหนดความเร็วของงู, กำหนดลักษณะหัวงู โดยใช้รูปที่ import มา, ยกปากกาขึ้นทำให้ไม่มีขีดตรงจุดเริ่มต้น, ตั้งตำแหน่งของงู
head.speed(0), head.shape('pic/snakehead.gif'), head.penup(), head.goto(0, 100)
head.direction = "stop" # หยุดการเคลื่อนที่งู

""" สร้างอาหารเพื่อเก็บคะแนนเมื่อหัวงูไปกินอาหาร """
food = turtle.Turtle() # สร้างอาหารโดยใช้คำสั่งเหมือนการสร้าง Turtle
# ทำให้อาหารไม่ขยับ, ลักษณะเป็นวงกลม, สีแดง, ไม่มีการรอยบนตำแหน่งของอาหาร, ขนาดของอาหาร
food.speed(0), food.shape("circle"), food.color("red"), food.penup(), food.shapesize(0.50, 0.50)
food.goto(random.randint(-290, 290), random.randint(-290, 290)) # ตั้งตำแหน่งของอาหารให้เกิดสุ่ม

segments = [] # List เปล่าเพื่อเพิ่มความยาวของงู

""" Score """
score = 0 # ตั้งค่าคะแนนครั้งแรก
high_score = 0 # ตั้งค่าคะแนนสูงสุดครั้งแรก

""" Text บน Screen """
pen = turtle.Turtle() # เรียกใช้ Turtle เพื่อสร้าง Text บน Screen
pen.speed(0), pen.shape("square"), pen.color("white"), pen.penup()
pen.hideturtle() # ซ่อน Turtle เพื่อให้เป็น Text อย่างเดียว
pen.goto(0, 260) # ตั้งจุดที่จะเขียน
pen.write("Score: 0 High Score: {}".format(high_score), align="center", font=("Courier", 24, "normal")) # Text ที่แสดงบน Screen

""" Function """
def move(): # ฟังก์ชันเดิน
    y = head.ycor() # กำหนดให้ตัวแปร y เป็นทิศทางการเดินของงูตามแกน y
    x = head.xcor() # กำหนดให้ตัวแปร x เป็นทิศทางการเดินของงูตามแกน x
    if head.direction == "up": # ถ้าหัวของงูหันไปทางด้านบน
        head.shape('pic/snakehead.gif')
        head.sety(y + 20) # ตัวงูจะเดินไปข้างหน้าโดยแกน y + ไปทีละ 20 ต่อการเรียกฟังก์ชัน 1 ครั้ง
 
    if head.direction == "down": # ถ้าหัวของงูหันไปทางด้านล่าง
        head.shape('pic/snakehead_down.gif')
        head.sety(y - 20) # ตัวงูจะเดินไปข้างหลังโดยแกน y - ไปทีละ 20 ต่อการเรียกฟังก์ชัน 1 ครั้ง
 
    if head.direction == "right":
        head.shape('pic/snakehead_right.gif')
        head.setx(x + 20) # ตัวงูจะเดินไปข้างขวาโดยแกน x + ไปทีละ 20 ในการเรียกฟังก์ชัน 1 ครั้ง
 
    if head.direction == "left":
        head.shape('pic/snakehead_left.gif')
        head.setx(x - 20) # ตัวงูจะเดินไปข้างซ้ายโดยแกน x - ไปทีละ 20 ในการเรียกฟังก์ชัน 1 ครั้ง

# เนื่องจากงูเคลื่อนที่สวนทางในทันทีไม่ได้
def go_up():
    if head.direction != "down":
        head.direction = "up"
 
def go_down():
    if head.direction != "up":
        head.direction = "down"
 
def go_right():
    if head.direction != "left":
        head.direction = "right"
 
def go_left():
    if head.direction != "right":
        head.direction = "left"
#-------------------------------#

""" ตรวจจับการกดปุ่มของ user เพื่อนำไปแปลงเป็นการเคลื่อนที่ของงู """
win.listen() # เริ่มจับการกด
win.onkey(go_up, "w") # กด w แล้วจะสั่งเริ่มฟังก์ชัน go_up
win.onkey(go_down, "s") # กด s แล้วจะสั่งเริ่มฟังก์ชัน go_down
win.onkey(go_right, "d") # กด d แล้วจะสั่งเริ่มฟังก์ชัน go_right
win.onkey(go_left, "a") # กด a แล้วจะสั่งเริ่มฟังก์ชัน go_left

""" While Loop ทำให้เกมดำเนินอย่างต่อเนื่อง """
delay = 0.1 # ตัวแปร delay
while True:

    win.update() # ทำให้ screen อัพเดทเสมอๆ

    """ ตรวจสอบเมื่อหัวออกนอก Screen """
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        pen.clear(), pen.color('red')
        pen.write('Game Over !', align="center", font=("Courier", 24, "normal"))
        time.sleep(1) # หยุดการทำงานด้วย delay = 1
        pen.clear(), pen.color('white')
        head.goto(0, 0)
        head.direction = "stop" # หยุดเคลื่อนที่ต่อ

        # ซ่อนหาง
        for segment in segments:
           segment.goto(1000, 1000)
 
        # รีเซ็ตหาง
        segments.clear()

        # reset score
        score = 0
        delay = 0.1

        # update score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    """ เมื่อตำแหน่งของงูเข้าใกล้อาหาร """
    if head.distance(food) < 15: # เมื่องูมีระยะห่างกับอาหารน้อยกว่า 15
        # สุ่มตำแหน่งของอาหารใหม่
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y) # ตั้งตำแหน่งของอาหาร

        """ เมื่องูกินอาหารแล้วความยาวของตัวงูเพิ่มขึ้น """
        snakebody = 'pic/tiles.gif' #เพิ่มรูปหัวงู
        win.register_shape(snakebody) #import รูป สำหรับใช้เป็นหัวงู
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape(snakebody)
        new_segment.penup()
        segments.append(new_segment) # เพิ่มหางไปใน list

        score += 10 # เพิ่มคะแนน
        delay -= 0.001
 
        if score > high_score: # ถ้าคะแนนที่ได้มากกว่าคะแนนสูงสุด
            high_score = score # คะแนนสูงสุดจะกลายเป็นคะแนนที่ได้ล่าสุด
        
        # Update Score
        pen.clear() # ลบ Text อันเก่า
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) # สร้าง Text ใหม่พร้อมคะแนนล่าสุด

    """ ขยับหางไปพร้อมๆกับหัวงู """
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    """ หากหางที่เพิ่มเข้ามาอยู่บนหัวงู จะเซ็ตตำแหน่งนั้นด้วยจุดที่หัวงูอยู่ """
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move() # ทำให้งูเดินเรื่อยๆบน Loop


    """ ตรวจสอบการกินหางตัวเอง """
    for segment in segments:
        if segment.distance(head) < 20:
            pen.clear(), pen.color('red')
            pen.write('Game Over !', align="center", font=("Courier", 24, "normal"))
            time.sleep(1)
            pen.clear(), pen.color('white')
            head.goto(0, 0)
            head.direction = "stop"
 
            # ซ่อนหาง
            for segment in segments:
                segment.goto(1000, 1000)

            # รีเซ็ตหาง
            segments.clear()

            # reset score
            score = 0
            delay = 0.1

            # update score
            pen.clear() # ลบ Text อันเก่า
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) # สร้าง Text ใหม่พร้อมคะแนนล่าสุด
    
    time.sleep(delay) # ตั้งค่าความเร็วในการเคลื่อนที่ของงู