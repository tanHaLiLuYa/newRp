import time

from controller import Controller
from maze import Maze
from nezha import Nezha

maze_list = [
  [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
  [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
  [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]
]

Maze(maze_list)
nezha = Nezha(maze_list, 0, 5, 12, 7)
# while nezha.m != nezha.end_m or nezha.n != nezha.end_n:
Controller(nezha.go_up, nezha.go_down, nezha.go_left, nezha.go_right,nezha.n,nezha.m)
# time.sleep(10)
# import turtle as f

# f.color("#FFB6C1")

# for i in range(270):
#     f.fd(i)
#     f.left(30+i)

# f.done()

# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     a= pos()
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

