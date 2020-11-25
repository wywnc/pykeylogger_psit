""" KeyLogger Project Created 19/11/2563 15:41 """
""" ลง pip และ pynput ด้วย 'pip install pynput' ก่อน """

""" Controlling the mouse """
def control_mouse_pynput():
    """ ตรวจจับ Cursor mouse และขยับไปยังตำแหน่งต่างๆ """
    """ ref: https://pypi.org/project/pynput/ -- Controlling the mouse """
    from pynput.mouse import Button, Controller

    mouse = Controller()

    # จับตำแหน่งของ Pointer
    print('The current pointer position is {0}'.format(
        mouse.position))

    # ตั้งตำแหน่งของ Pointer
    mouse.position = (10, 20)
    print('Now we have moved it to {0}'.format(
        mouse.position))

    # ขยับตำแหน่งของ Pointer
    mouse.move(5, -5)

    # ควบคุมเมาส์ให้คลิกและปล่อย
    mouse.press(Button.left)
    mouse.release(Button.left)

    # สั่งเมาส์ให้ดับเบิ้ลคลิก
    # twice on macOS
    mouse.click(Button.left, 2)

    # เลื่อนลูกกลิ้งลง
    mouse.scroll(0, 2)

""" KeyLogger """
from pynput import keyboard
""" Function ของ KeyLogger ทั้งหมด """
""" ref: https://pypi.org/project/pynput/ -- Monitoring the keyboard """
def on_press(key):
    try:
        print('Alphanumeric Key: {0} pressed'.format(
            key.char))
    except AttributeError:
        print('Special Key: {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # หยุดด้วย Key ESC
        return False

def keylog():
# ตรวจจับปุ่มกดที่กดและปล่อย
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

    # เริ่ม function
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()
"""-----------------------------------------------"""

""" Welcome Text """
def main():
    """ for show detail of project """
    print('Welcome to my KeyLogger Project')
    print('Member: -')
    print('\t-')
    print('\t-')
    print('\t-')
    print('All Project:')
    print('\t1. KeyLogger')
    print('\t2. MouseLogger [Not Available]')
    print('\t3. MouseControlling')
    num = input('Press Number: ')
    if num == '1':
        keylog()
    elif num == '2':
        pass
    elif num == '3':
        control_mouse_pynput()
main()
