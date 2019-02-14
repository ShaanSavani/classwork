import arcade


WIDTH = 640
HEIGHT = 480

x = int(input("Please enter the x value of the shape: "))
y = int(input("Please enter the y value of the shape: "))
radius = int(input("Please enter the radius: "))

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

# Begin drawing

arcade.draw_circle_filled(x, y, radius, arcade.color.COCOA_BROWN)

# End drawing
arcade.finish_render()
arcade.run()