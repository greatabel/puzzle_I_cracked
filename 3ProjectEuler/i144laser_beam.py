'''

In laser physics, a "white cell" is a mirror system that acts as a delay line for the laser beam. 

The beam enters the cell, bounces around on the mirrors, and eventually works its way back out.

The specific white cell we will be considering is an ellipse with the equation 4x2 + y2 = 100

The section corresponding to −0.01 ≤ x ≤ +0.01 at the top is missing, 

allowing the light to enter and exit through the hole.


The light beam in this problem starts at the point (0.0,10.1) just outside the white cell, 

and the beam first impacts the mirror at (1.4,-9.6).

Each time the laser beam hits the surface of the ellipse, it follows the usual law of reflection 

"angle of incidence equals angle of reflection." That is, both the incident and reflected 

beams make the same angle with the normal line at the point of incidence.

In the figure on the left, the red line shows the first two points of contact between the laser beam 

and the wall of the white cell; the blue line shows the line tangent to the ellipse at the point of 

incidence of the first bounce.

The slope m of the tangent line at any point (x,y) of the given ellipse is: m = −4x/y

The normal line is perpendicular to this tangent line at the point of incidence.

The animation on the right shows the first 10 reflections of the beam.

How many times does the beam hit the internal surface of the white cell before exiting?

#----------------------------#

对这道题不感兴趣，直接使用 https://github.com/Meng-Gen/ProjectEuler 的方案

'''




import time
from termcolor import colored
import math


def normalize(v):
    length = math.sqrt(v[0] * v[0] + v[1] * v[1])
    return (v[0] / length, v[1] / length)

def dot(u, v):    
    return u[0] * v[0] + u[1] * v[1]
    
def direction_vector(p, q):
    return (q[0] - p[0], q[1] - p[1])

def normal_vector(p):
    return normalize((4 * p[0], p[1]))

def reflect(v, n):
    return (2 * dot(v, n) * n[0] - v[0], 2 * dot(v, n) * n[1] - v[1])

def solve(v, p):
    t = (-8 * v[0] * p[0] - 2 * v[1] * p[1])/(4 * v[0] * v[0] + v[1] * v[1])
    return (v[0] * t + p[0], v[1] * t + p[1])


def main_process():
    p = (0.0, 10.1)
    q = (1.4, -9.6)
    v = direction_vector(q, p)
    for i in range(1, 1000):
        n = normal_vector(q)
        r = reflect(v, n)
        s = solve(r, q)
        v = direction_vector(s, q)
        q = s
        print(s)
        if s[0] >= -0.01 and s[0] <= 0.01 and s[1] > 0:
            print(colored('mycount=', 'red'), i)
            break 
        # mycount= 354

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)
