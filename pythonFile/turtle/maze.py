from turtle import Turtle

class Maze(Turtle):
    size = 20
  
    def __init__(self, maze_list):
        # 需要先调用父类的初始化方法才能在初始化方法中调用父类的方法
        Turtle.__init__(self)
        self.maze_list = maze_list
        # 为了加快绘图速度隐藏海龟，速度设为最快
        self.hideturtle()
        self.speed(0)
        self.draw_walls()

    def draw_wall(self):
        self.pendown()
        self.begin_fill()
        self.fillcolor('#7392f6')
        for i in range(4):
            self.forward(self.size)
            self.right(90)
        self.end_fill()
        self.penup()

    def draw_walls(self):
        self.penup()
        # 从 (-130, 130) 开始
        self.goto(-130, 130)

        for row in range(13):
            for col in range(13):
                if self.maze_list[row][col] == 1:
                     self.draw_wall()
        # 右移一列
                self.goto(self.size * (col + 1) - 130, 130 - self.size * row)
      # 下移一行
            self.goto(-130, 130 - self.size * (row + 1))