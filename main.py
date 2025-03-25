import tkinter as tk
from PIL import Image, ImageTk
import tkinter as tk
import tkinter.font as font
from tkinter import PhotoImage
from in_out import in_out
import os
from motion import noise
from rect_noise import rect_noise 
from record import record
from find_motion import find_motion
from Face_recognition import maincall


window = tk.Tk()
window.title("Smart cctv")
window.config(bg="#1A3259")
window.geometry('1280x720+0+0')

frame1 = tk.Frame(window, bg="#1A3259", width=1280, height=720,borderwidth=0)  # Set background color and size of the frame
frame1.pack_propagate(False)  # Prevent frame from resizing to its contents
frame1.pack()

icon = Image.open('icons/bg.png')
icon = icon.resize((550, 550), Image.LANCZOS)# type: ignore
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon, borderwidth=0, highlightthickness=0, bg="#1A3259")# type: ignore
label_icon.place(x=365, y=40)  # Place the label at coordinates (100, 100) within the frame

btn1_image = Image.open('icons/monitor.png')
btn1_image = btn1_image.resize((150,150), Image.LANCZOS) # type: ignore
btn1_image = ImageTk.PhotoImage(btn1_image)
btn1 = tk.Button(frame1, height=150, width=150, command=find_motion, image=btn1_image, compound='left',  borderwidth=0, highlightthickness=0, bg="#1A3259") # type: ignore
btn1.place(x=100, y=50)  # Place the button at coordinates (300, 400) within the frame

btn2_image = Image.open('icons/identify.png')
btn2_image = btn2_image.resize((150,150), Image.LANCZOS)# type: ignore
btn2_image = ImageTk.PhotoImage(btn2_image)
btn2 = tk.Button(frame1, height=150, width=150, command=maincall, image=btn2_image, compound='left',  borderwidth=0, highlightthickness=0, bg="#1A3259")# type: ignore
btn2.place(x=100, y=225)  # Place the button at coordinates (300, 400) within the frame

def open_database():
    folder_path = os.path.join(os.getcwd(), "database")
    os.system(f'explorer "{folder_path}"')

btn3_image = Image.open('icons/database.png')
btn3_image = btn3_image.resize((300,80), Image.LANCZOS)# type: ignore
btn3_image = ImageTk.PhotoImage(btn3_image)
btn3 = tk.Button(frame1, height=80, width=300, command=open_database, image=btn3_image, compound='left',  borderwidth=0, highlightthickness=0, bg="#1A3259")# type: ignore
btn3.place(x=300, y=570)  # Place the button at coordinates (300, 400) within the frame

btn4_image = Image.open('icons/exit1.png')
btn4_image = btn4_image.resize((300,80), Image.LANCZOS)# type: ignore
btn4_image = ImageTk.PhotoImage(btn4_image)
btn4 = tk.Button(frame1, height=80, width=300, command=window.quit, image=btn4_image, compound='left',  borderwidth=0, highlightthickness=0, highlightbackground="#1A3259",bg="#1A3259")# type: ignore
btn4.place(x=700, y=570)  # Place the button at coordinates (300, 400) within the frame

btn5_image = Image.open('icons/record.png')
btn5_image = btn5_image.resize((150,150), Image.LANCZOS)# type: ignore
btn5_image = ImageTk.PhotoImage(btn5_image)
btn5 = tk.Button(frame1, height=150, width=150, command=record, image=btn5_image, compound='left',  borderwidth=0, highlightthickness=0, bg="#1A3259")# type: ignore
btn5.place(x=100, y=400)  # Place the button at coordinates (300, 400) within the frame

btn6_image = Image.open('icons/in-out.png')
btn6_image = btn6_image.resize((150,150), Image.LANCZOS)# type: ignore
btn6_image = ImageTk.PhotoImage(btn6_image)
btn6 = tk.Button(frame1, height=150, width=150, command=in_out, image=btn6_image, compound='left',  borderwidth=0, highlightthickness=0, bg="#1A3259")# type: ignore
btn6.place(x=1015, y=50)  # Place the button at coordinates (300, 400) within the frame

btn7_image = Image.open('icons/Noise.png')
btn7_image = btn7_image.resize((150,150), Image.LANCZOS)# type: ignore
btn7_image = ImageTk.PhotoImage(btn7_image)
btn7 = tk.Button(frame1, height=150, width=150, command=noise, image=btn7_image, compound='left',  borderwidth=0, highlightthickness=0, bg="#1A3259")# type: ignore
btn7.place(x=1015, y=225)  # Place the button at coordinates (300, 400) within the frame

btn8_image = Image.open('icons/rectangle.png')
btn8_image = btn8_image.resize((150,150), Image.LANCZOS)# type: ignore
btn8_image = ImageTk.PhotoImage(btn8_image)
btn8 = tk.Button(frame1, height=150, width=150, command=rect_noise, image=btn8_image, compound='left',  borderwidth=0, highlightthickness=0, bg="#1A3259")# type: ignore
btn8.place(x=1015, y=400)  # Place the button at coordinates (300, 400) within the frame

window.mainloop()
