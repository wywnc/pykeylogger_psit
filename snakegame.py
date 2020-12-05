
"""
    Snake Game Project
    เริ่ม : 27/11/2563 - 20:26
    แก้ไข : 27/11/2563 - 23:39 [Veerawat]
           05/12/2563 - 14.38 [Wanatchporn]
    -----------------------------------------------------
    Reference
    - Introduction To Game Building With Python's Turtle Module : https://www.edureka.co/blog/python-turtle-module/
"""

""" Import """
import turtle # นำ Module Turtle มาใช้ในการดำเนินการเกี่ยวกับตัวงู
import time # นำ Module Time มาใช้ในการสร้าง delay
import random # นำ Module Random มาใช้ในการสุ่มตำแหน่งของอาหาร



""" สร้างหน้าจอสำหรับการเล่นโดย Turtle Module """
win = turtle.Screen() # สร้างหน้าจอ
win.title("Snake Game Project") # Title ของหน้าจอที่สร้างขึ้น
win.bgcolor("green") # เปลี่ยนสีพื้นหลัง
win.setup(width=600,height=600) # ตั้งค่าขนาดหน้าจอ
win.tracer(0) # ตั้งให้หน้าจอไม่มีการปรับแต่งอะไรเพิ่ม

""" สร้างหัวงูเพื่อใช้ในการเล่น """
turtle.register_shape('snakehead.gif') #import รูป สำหรับใช้เป็นหัวงู
turtle.register_shape('snakehead_down.gif')
turtle.register_shape('snakehead_right.gif')
turtle.register_shape('snakehead_left.gif')
head = turtle.Turtle() # สร้าง Turtle ซึ่งในที่นี้ใช้แทนหัวงู
head.speed(0) # กำหนดความเร็วของงู
head.shape('snakehead.gif') # กำหนดลักษณะหัวงู โดยใช้รูปที่ import มา
head.penup() # ยกปากกาขึ้นทำให้ไม่มีขีดตรงจุดเริ่มต้น
head.goto(0, 100) # ตั้งตำแหน่งของงู
head.direction = "stop" # หยุดการเคลื่อนที่งู

""" สร้างอาหารเพื่อเก็บคะแนนเมื่อหัวงูไปกินอาหาร """
food = turtle.Turtle() # สร้างอาหารโดยใช้คำสั่งเหมือนการสร้าง Turtle
food.speed(0) # ทำให้อาหารให้ขยับ
food.shape("circle") # ทำให้ลักษณะเป็นวงกลม
food.color("red") # สีของอาหารเป็นสีแดง
food.penup() # ทำให้ไม่มีการขีดเขียนบนตำแหน่งของอาหาร
food.shapesize(0.50, 0.50) # ขนาดของวงกลม
food.goto(0, 0) # ตั้งตำแหน่งของอาหาร

segments = [] # List เปล่าเพื่อเพิ่มความยาวของงู

""" Score """
score = 0 # ตั้งค่าคะแนนครั้งแรก
high_score = 0 # ตั้งค่าคะแนนสูงสุดครั้งแรก

""" Text บน Screen """
pen = turtle.Turtle() # เรียกใช้ Turtle
pen.speed(0)
pen.shape("square")
pen.color("white") # สี Text
pen.penup()
pen.hideturtle() # ซ่อนหัวเพื่อให้เป็น Text อย่างเดียว
pen.goto(0, 260) # ตั้งจุดที่จะเขียน
pen.write("Score: 0 High Score: {}".format(high_score), align="center", font=("Courier", 24, "normal")) # Text ที่แสดงบน Screen

""" Function """
def move(): # ฟังก์ชันเดิน
    if head.direction == "up": # ถ้าหัวของงูหันไปทางด้านบน
        y = head.ycor() # กำหนดให้ตัวแปร y เป็นทิศทางการเดินของงูตามแกน y
        head.shape('snakehead.gif')
        head.sety(y + 20) # ตัวงูจะเดินไปข้างหน้าโดยแกน y + ไปทีละ 20 ต่อการเรียกฟังก์ชัน 1 ครั้ง
 
    if head.direction == "down": # ถ้าหัวของงูหันไปทางด้านล่าง
        y = head.ycor() # กำหนดให้ตัวแปร y เป็นทิศทางการเดินของงูตามแกน y
        head.shape('snakehead_down.gif')
        head.sety(y - 20) # ตัวงูจะเดินไปข้างหลังโดยแกน y - ไปทีละ 20 ต่อการเรียกฟังก์ชัน 1 ครั้ง
 
    if head.direction == "right":
        x = head.xcor() # กำหนดให้ตัวแปร x เป็นทิศทางการเดินของงูตามแกน x
        head.shape('snakehead_right.gif')
        head.setx(x + 20) # ตัวงูจะเดินไปข้างขวาโดยแกน x + ไปทีละ 20 ในการเรียกฟังก์ชัน 1 ครั้ง
 
    if head.direction == "left":
        x = head.xcor() # กำหนดให้ตัวแปร x เป็นทิศทางการเดินของงูตามแกน x
        head.shape('snakehead_left.gif')
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
        time.sleep(1) # หยุดการทำงานด้วย delay = 1
        head.goto(0, 0)
        head.direction = "stop" # หยุดเคลื่อนที่ต่อ

        # ซ่อนหาง
        for segment in segments:
           segment.goto(1000, 1000)
 
        # รีเซ็ตหาง
        segments = []

        # reset score
        score = 0

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
        snakebody = 'snakebody.gif' #เพิ่มรูปหัวงู
        turtle.register_shape(snakebody) #import รูป สำหรับใช้เป็นหัวงู
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape(snakebody)
        new_segment.penup()
        segments.append(new_segment) # เพิ่มหางไปใน list

        score += 10 # เพิ่มคะแนน
 
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
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
 
            # ซ่อนหาง
            for segment in segments:
                segment.goto(1000, 1000)

            # รีเซ็ตหาง
            segment.clear()

            # reset score
            score = 0

            # update score
            pen.clear() # ลบ Text อันเก่า
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) # สร้าง Text ใหม่พร้อมคะแนนล่าสุด
    
    time.sleep(delay) # ตั้งค่าความเร็วในการเคลื่อนที่ของงู