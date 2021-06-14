from random import choice

corner_count = 3 # must be greater than or equal to 3.
divisor = 2
SIZE = 900
radius = SIZE * .45
dot_size = 3

coords = [0, 0]
corners = []

def setup():
    size(SIZE, SIZE)
    translate(SIZE * .5, SIZE * .5)
    draw_polygon(corner_count)
    frameRate(250)
    
def draw():
    global coords, corners

    translate(SIZE * .5, SIZE * .5)
    
    # Plotting the point.
    circle(coords[0], coords[1], dot_size)
    
    # Moving the point.
    rand_corner = choice(corners)
    coords = [(rand_corner[0] + coords[0]) / divisor, (rand_corner[1] + coords[1]) / divisor]
    

def draw_polygon(n):
    global corners, coords
    stroke(250)
    background(30)
    
    corners = []
    angle = TWO_PI / n
    for i in range(n):
        # If we are connecting the last corner, than connect it to the 0th corner.
        i_two = i + 1 if i < n - 1 else 0
        line(radius * cos(angle * i), radius * sin(angle * i), 
             radius * cos(angle * i_two), radius * sin(angle * i_two)
                     )
        
        corners.append([radius * cos(angle * i), radius * sin(angle * i)])
    coords = corners[0]

def keyPressed():
    if key == CODED:
        # handling the corner_count
        global corner_count
        if keyCode == UP:
            corner_count += 1
            draw_polygon(corner_count)
        elif keyCode == DOWN:
            # Don't decrease the corner count if it is 3 so it can still be a polygon.
            if corner_count == 3:
                return
            
            corner_count -= 1
            draw_polygon(corner_count)
            
        # handling divisor 
        if keyCode == RIGHT:
            draw_polygon(corner_count)
            set_divisor(divisor + 1)
        elif keyCode == LEFT:
            draw_polygon(corner_count)
            set_divisor(divisor - 1)

def set_divisor(val):
    global divisor 
    if val == 0:
        val = 1
    divisor = val
    print("Divisor = " + str(val))
    
