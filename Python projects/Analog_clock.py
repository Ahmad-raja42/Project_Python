import tkinter as tk
import time
import math

Width = 400
Height = 400

root = tk.Tk()
root.title("Analog Clock")
canvas = tk.Canvas(root, width=Width, height=Height, bg="white")
canvas.pack()

def update_clock():
  canvas.delete("all")
  now = time.localtime()
  hour = now.tm_hour % 12
  minute = now.tm_min
  second = now.tm_sec
#Draw clock face
  canvas.create_oval(2,2, Width, Height, outline="black", width = 2)
#Draw hour numbers
  for i in range(12):
    angle = i * math.pi/6 - math.pi/2
    x = Width/2 + 0.7 * Width/2 * math.cos(angle)
    y = Height/2 + 0.7 * Width/2 * math.sin(angle)
    if i == 0:
      canvas.create_text(x, y-10, text=str(i+12), font=("Helvetica", 12))
    else:
      canvas.create_text(x, y, text=str(i),font=("Helvetica", 12))
# Draw min lines
    for i in range(60):
      angle = i * math.pi/30 - math.pi/2
      x1 = Width/2 + 0.8 * Width/2 * math.cos(angle)
      y1 = Height/2 + 0.8 * Height/2 * math.sin(angle)
      x2 = Width/2 + 0.9 * Width/2 * math.cos(angle)
      y2 = Height/2 + 0.9 * Height/2 * math.sin(angle)
      if i % 5 == 0:
        canvas.create_line(x1, x2,y1, y2, fill="black", width=3)
      else:
        canvas.create_line(x1, x2,y1, y2, fill="black", width=1)
#Draw hour hand
    hour_angle = (hour + minute/60) * math.pi/6 - math.pi/2
    hour_x = Width/2 + 0.5 * Width/2 * math.cos(hour_angle)
    hour_y = Height/2 + 0.5 * Height/2 * math.sin(hour_angle)
    canvas.create_line(Width/2, Height/2, hour_x, hour_y, fill="black", Width=6 )
#Draw minute hand    
    minute_angle = (second + second/60) * math.pi/30 - math.pi/2
    minute_x = Width/2 + 0.7 * Width/2 * math.cos(minute_angle)
    minute_y = Height/2 + 0.7 * Height/2 * math.sin(minute_angle)
    canvas.create_line(Width/2, Height/2, minute_x, minute_y, fill="black", Width=4 )
#Draw minute hand    
    second_angle = second * math.pi/30 - math.pi/2
    second_x = Width/2 + 0.6 * Width/2 * math.cos(second_angle)
    second_y = Height/2 + 0.6 * Height/2 * math.sin(second_angle)
    canvas.create_line(Width/2, Height/2, second_x, second_y, fill="red", Width=2 )
    canvas.after(1000, update_clock)
    update_clock()
    root.mainloop()