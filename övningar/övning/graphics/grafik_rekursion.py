from graphics import *

def circle_rek(win, radie, centrum_point):
    circle = Circle(centrum_point, radie)
    circle.draw(win)
    if radie >= 1: 
        cir_r = circle_rek(win, radie / 2, centrum_point = Point(centrum_point.getX() + radie, centrum_point.getY()))
        cir_l = circle_rek(win, radie / 2, centrum_point = Point(centrum_point.getX() - radie, centrum_point.getY()))
        cir_hd =circle_rek(win, radie / 2, centrum_point = Point(centrum_point.getX(), centrum_point.getY() + radie))
        cir_xy = [cir_r, cir_l, cir_hd]
        return cir_xy

    else:
        return 0

win1 = GraphWin("triangel" , 1600, 1000)
win1_h = win1.getHeight() / 2
win1_w = win1.getWidth() / 2
circle_center = Point(win1_w, win1_h)
radius = win1_w / 4

circle_rek(win1, radius, circle_center)
win1.getMouse()
