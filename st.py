import tkinter as tk

def scale_point(x, y, scale_factor, cx, cy):
    """
    Scales a point (x, y) relative to a center point (cx, cy) by a scale factor.
    
    Parameters:
    x, y - coordinates of the point to scale.
    scale_factor - factor by which to scale the point.
    cx, cy - center of scaling.
    
    Returns:
    (x', y') - new coordinates after scaling.
    """
    # Translate point to origin, scale, then translate back
    scaled_x = cx + (x - cx) * scale_factor
    scaled_y = cy + (y - cy) * scale_factor
    return scaled_x, scaled_y

def draw_scaled_rectangle(scale_factor):
    """
    Draws a rectangle scaled by a specific factor on the canvas.
    
    Parameters:
    scale_factor - scaling factor to apply to the rectangle.
    """
    # Clear the canvas
    canvas.delete("all")
    
    # Center and size of the rectangle
    cx, cy = 200, 200
    rect_width, rect_height = 100, 50
    
    # Original coordinates of the rectangle's corners
    points = [
        (cx - rect_width // 2, cy - rect_height // 2),
        (cx + rect_width // 2, cy - rect_height // 2),
        (cx + rect_width // 2, cy + rect_height // 2),
        (cx - rect_width // 2, cy + rect_height // 2)
    ]
    
    # Scale each corner
    scaled_points = [scale_point(x, y, scale_factor, cx, cy) for x, y in points]
    
    # Draw the scaled rectangle
    canvas.create_polygon(scaled_points, outline="black", fill="lightgreen", width=2)

def on_slider_change(value):
    """
    Callback function for the slider to update the scaling factor.
    
    Parameters:
    value - current value of the slider (scaling factor).
    """
    scale_factor = float(value)
    draw_scaled_rectangle(scale_factor)

# Set up the main application window
root = tk.Tk()
root.title("Scale Rectangle GUI")

# Set up the canvas to draw the rectangle
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Set up the slider to control the scaling factor
scale_slider = tk.Scale(root, from_=0.1, to=3.0, resolution=0.1, orient=tk.HORIZONTAL, length=300, label="Scaling Factor", command=on_slider_change)
scale_slider.set(1.0)  # Initial scale factor
scale_slider.pack()

# Initial drawing of the rectangle
draw_scaled_rectangle(1.0)

# Start the main event loop
root.mainloop()
