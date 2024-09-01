import tkinter as tk
import math

def rotate_point(x, y, angle_degrees, cx, cy):
  
    angle_radians = math.radians(angle_degrees)
    # Translate point back to origin
    temp_x = x - cx
    temp_y = y - cy
    # Rotate point
    rotated_x = temp_x * math.cos(angle_radians) - temp_y * math.sin(angle_radians)
    rotated_y = temp_x * math.sin(angle_radians) + temp_y * math.cos(angle_radians)
    # Translate point back to its original position
    final_x = rotated_x + cx
    final_y = rotated_y + cy
    return final_x, final_y

def draw_rotated_square(angle):
    """
    Draws a square rotated by a specific angle on the canvas.
    
    Parameters:
    angle - angle in degrees to rotate the square.
    """
    # Clear the canvas
    canvas.delete("all")
    
    # Center and size of the square
    cx, cy = 200, 200
    side = 100
    
    # Original coordinates of the square's corners
    points = [
        (cx - side // 2, cy - side // 2),
        (cx + side // 2, cy - side // 2),
        (cx + side // 2, cy + side // 2),
        (cx - side // 2, cy + side // 2)
    ]
    
    # Rotate each corner
    rotated_points = [rotate_point(x, y, angle, cx, cy) for x, y in points]
    
    # Draw the rotated square
    canvas.create_polygon(rotated_points, outline="black", fill="lightblue", width=2)

def on_slider_change(value):
    """
    Callback function for the slider to update the rotation angle.
    
    Parameters:
    value - current value of the slider (angle in degrees).
    """
    angle = float(value)
    draw_rotated_square(angle)

# Set up the main application window
root = tk.Tk()
root.title("Rotate Square GUI")

# Set up the canvas to draw the square
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Set up the slider to control the rotation angle
angle_slider = tk.Scale(root, from_=0, to=360, orient=tk.HORIZONTAL, length=300, label="Rotation Angle", command=on_slider_change)
angle_slider.pack()

# Initial drawing of the square
draw_rotated_square(0)

# Start the main event loop
root.mainloop()
