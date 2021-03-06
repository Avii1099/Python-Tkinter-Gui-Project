from tkinter import *


root= Tk()
canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root, width= canvas_width, height= canvas_height)
can_widget.pack()

# The line goes from point x1, y1 to x2, y2
can_widget.create_line(0 , 200, 800, 200 )
root.mainloop()