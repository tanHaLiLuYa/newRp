from turtle import Turtle
import os
import time
# os.chdir(r"D:\github\pythonFile\testpy")


class Nezha(Turtle):
    def __init__(self, maze_list, start_m, start_n, end_m, end_n):
    # 父类初始化
        Turtle.__init__(self)
        self.m = start_m
        self.n = start_n
        self.end_m = end_m
        self.end_n = end_n
        self.maze_list = maze_list
        self.hideturtle()
        self.speed(0)
        self.penup()
        # 移到对应的位置
        self.goto(self.n * 20 - 120, 120 - self.m * 20)
        # 变成海龟
        self.shape('turtle')
        self.color('#28bea0')
        self.setheading(270)
        self.showturtle()
        # time.sleep(10)
        # 添加哪吒图片作为形状
        screen = self.getscreen()
        screen.addshape('nezha.gif')
    # def game_over(self):
    #     while self.m != self.end_m or self.n != self.end_n:


    def reach_exit(self, m, n):
        if m == self.end_m and n == self.end_n:
      # 变成哪吒
            self.shape('nezha.gif')

    def canmove(self, m, n):
        return self.maze_list[m][n] == 0

    def move(self, m, n):
        self.m = m
        self.n = n
        self.goto(self.n * 20 - 120, 120 - self.m * 20)
        self.reach_exit(m, n)

    def go_up(self):
        if self.canmove(self.m - 1, self.n):
            self.setheading(90)
            self.move(self.m - 1, self.n)
  
    def go_down(self):
        if self.canmove(self.m + 1, self.n):
            self.setheading(270)
            self.move(self.m + 1, self.n)

    def go_left(self):
        if self.canmove(self.m, self.n - 1):
            self.setheading(180)
            self.move(self.m, self.n - 1)

    def go_right(self):
        if self.canmove(self.m, self.n + 1):
            self.setheading(0)
            self.move(self.m, self.n + 1)
