import math

def y_co_ordinate():
    y = float(input("Faka isilungelelanisi sika Y"))
    return y
def x_co_ordinates():
    x = float(input("Faka isilungelanisi sika X"))
    return x
def point_name():
    name = input("Faka igama lalendawo")
    return name
def distance(x,y):
    x_origin = 0
    y_origin = 0
    dist = math.sqrt((x-x_origin)**2+(y-y_origin)**2)
    return dist
def x_ref_x_axis(x):
    x_ref = x * -1
    return x_ref
def y_ref_y_axis(y):
    y_ref = y * -1
    return y_ref
def determine_quad(x,y):
    if y > 0 and x > 0 :
        quad = "EMntla Mpuma"
    elif y > 0 and x < 0 :
        quad = "EMntla Ntshona"
    elif y < 0 and x < 0 :
        quad = "EMzantsi Ntshona"
    elif y < 0 and x > 0 :
        quad = "Emzantsi Mpuma"
    elif y > 0 and x ==0 :
        quad ="Emntla"
    elif y == 0 and x < 0 :
        quad = "Ntshona"
    elif y < 0 and x == 0 :
        quad = "Mzantsi"
    elif y == 0 and x > 0 :
        quad = "Mpuma"
    elif y == 0 and x == 0 :
        quad = "Orijini"
    return quad
def equation_str(x,y):
    #equation of a straight line...y = mx + c
    x_ori = 0
    y_ori = 0
    m = (y-y_ori)/(x-x_ori)
    c = y - m*x
    x = x
    y = y
    y = m*x+c
    print(f'y = {m}x + {c}')

if __name__ == '__main__':
   y = y_co_ordinate()
   x = x_co_ordinates()
   name = point_name()
   print(distance(x,y))
   print(x_ref_x_axis(x))
   print(y_ref_y_axis(y))
   print(determine_quad(x,y))
   equation_str(x,y)













