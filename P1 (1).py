import math
r = 42
theta_deg = 60
theta = math.radians(theta_deg)
arc_length = r * theta
side = arc_length / 4
area = side ** 2
print("Area of the square =", area)