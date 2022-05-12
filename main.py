import turtle
from abc import ABCMeta, abstractmethod
from types import NoneType
from math import atan,degrees
import tic_tac_toe as tt

screen = turtle.Screen()
class Drawable(metaclass = ABCMeta):
    """Абстрактний клас для зображення точок та кіл заданих розмірів та
    кольору
    """
    @property
    @abstractmethod
    def color(self):
        """Властивість, що повертає/встановлює колір переднього плану."""
        pass
    
    @color.setter
    @abstractmethod
    def color(self, cl):
        pass
    
    @property
    @abstractmethod
    def bgcolor(self):
        """Властивість, що повертає/встановлює колір фону."""
        pass
    
    @bgcolor.setter
    @abstractmethod
    def bgcolor(self, cl):
        pass
    
    @abstractmethod
    def draw_point(self, x, y, cl):
        """Зобразити точку з координатами x, y кольором cl."""
        pass
    
    @abstractmethod
    def draw_circle(self, x, y, r, cl):
        """Зобразити коло з координатами цнтру x, y радіусом r кольором
        cl."""
        pass
    
    @abstractmethod
    def draw_rectangle(self, a, b, c, d,cl):
        """Зобразити прямокутник з вершинами в точках a,b,c,d кольором
        cl."""
        pass
    
    @abstractmethod
    def draw_crisscross(self, a, b, l ,cl):
        """Зобразити хрестик з вершинами в точках a,b, довжиною l кольором
        cl."""
        pass
    
    
 
class TurtleDraw(Drawable):
    """Клас для зображення точок та кіл заданих розмірів та кольору.
    TurtleDraw є нащадком абстрактного класу Drawable та використовує засоби
    роботи з графікою з модуля turtle.
    """

    def __init__(self):
        pause = 0
        turtle.up()
        # turtle.home()
        turtle.delay(pause)
 
    @property
    def color(self):
        """Властивість, що повертає/встановлює колір переднього плану."""
        return turtle.pencolor()
    
    @color.setter
    def color(self, cl):
        turtle.pencolor(cl)
   
    @property
    def bgcolor(self):
        """Властивість, що повертає/встановлює колір фону."""
        return turtle.bgcolor()

    @bgcolor.setter
    def bgcolor(self, cl):
        turtle.bgcolor(cl)
    
    def draw_point(self, x, y, cl):
        """Зобразити точку з координатами x, y кольором cl."""
        turtle.up()
        turtle.setpos(x, y)
        turtle.down()
        turtle.dot(cl)

    def draw_circle(self, x, y, r, cl):
        """Зобразити коло з координатами цнтру x, y радіусом r кольором
        cl."""
        c = self.color
        self.color = cl
        turtle.up()
        turtle.setpos(x, y-r) #малює починаючи знизу кола
        turtle.down()
        turtle.circle(r)
        turtle.up()
        self.color = c

    def draw_rectangle(self, a, b, c, d,cl):
        prev_color = self.color
        self.color = cl
        turtle.up()
        turtle.setpos(a)
        turtle.down()
        for i in (b,c,d,a):
            turtle.setpos(i)
        self.color = prev_color
    
    def draw_crisscross(self, a, b, l,angle,cl):
        prev_color = self.color
        self.color = cl
        turtle.up()
        turtle.setpos(a)
        turtle.down()
        turtle.right(angle)
        turtle.forward(l)
        turtle.left(angle)
        turtle.up()
        turtle.setpos(b)
        turtle.down()
        turtle.right(180-angle)
        turtle.forward(l)
        turtle.left(180-angle)
        self.color = prev_color

x = -120
y = 200
width = 75
height = 100
angle = degrees(atan(4/3))

def draw_folder(a,b,c,d):
    TurtleDraw().draw_rectangle(a,b,c,d,'black')

    
def main():
    k = 1
    pen = turtle.Turtle().getpen()

    def click(i,j):
        nonlocal k
        pos = (int((i-x)//width),int((y-j)//height))
        if 0<=pos[0]<=2 and 0<=pos[1]<=2 and not tt.check_status():
            if tt.player_move(*pos[::-1]):
                tt.see_the_field()
                k += 1
                TurtleDraw().draw_crisscross((x+pos[0]*width + 7.5,y-pos[1]*height - 10),(x+(pos[0]+1)*width - 7.5,y - pos[1]*height - 10),100,angle,'red')
                if not tt.check_status():
                    pen.clear()
                    comp_move()
                    tt.see_the_field()
                    k += 1

    def pl_move():
        pen.hideturtle()
        pen.up()
        pen.setpos(-150,-150)
        pen.write('Хід гравця, виберіть поле:',font=['Courier',16,'italic'])
        screen.listen()
        screen.onclick(click)
        
    def comp_move():
        pos = tt.computer_move()
        TurtleDraw().draw_circle(x+(pos[0]+0.5)*width,y - (pos[1]+0.5)*height,30,'blue')

    for i in range(3):
        for j in range(3):
            x_ = x+j*width
            y_ = y - i*height
            draw_folder((x_,y_), (x_+width, y_),(x_+width, y_-height), (x_, y_ - height))
    
    tt.see_the_field()
    while not(tt.check_status()):
        pl_move()
    print('Гру завершено!')
    
    res = 'перемога'
    if tt.check_status() == 'deadlock':
        res = 'нічия!'
    else:
        winner = ' гравця!' if k%2 == 0 else " комп'ютера :("
        res += winner
    print(res)
    pen.clear()
    pen.goto(-160,220)
    pen.write(f'Гру закінчено, {res}',font=["Lucida Sans Unicode", 16, "normal"])
        
main()
turtle.done()
