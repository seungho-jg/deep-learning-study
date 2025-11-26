# 02 퍼셉트론 25.11.26
import numpy as np

# 논리 회로 구현
def AND(x1, x2):
  w1, w2, theta = 0.5, 0.5, 0.7
  tmp = x1*w1 + x2*w2
  if tmp <= theta:
    return 0
  elif tmp > theta:
    return 1
  
# 퍼셉트론 구현하기(p.51)
def ex_2_3_1():
  print(AND(0, 0)) # 0
  print(AND(0, 1)) # 0
  print(AND(1, 0)) # 0
  print(AND(1, 1)) # 1

# 가중치와 편향 도입(p.52)
def ex_2_3_2():
  x = np.array([0, 1])       # 입력
  w = np.array([0.5, 0.5])  # 가중치
  b = -0.7                  # 편향
  print(w*x) # [0, 0.5]
  print(np.sum(w*x) + b) # -0.19999999999999996

def new_AND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.7
  tmp = np.sum(w*x) + b
  if tmp <=0:
    return 0
  else:
    return 1

def ex_2_3_3():
  print("--AND--")
  print("0 0",new_AND(0, 0)) # 0
  print("0 1",new_AND(0, 1)) # 0
  print("1 0",new_AND(1, 0)) # 0
  print("1 1",new_AND(1, 1)) # 1
  print("--NAND--")
  print("0 0",NAND(0, 0)) # 1
  print("0 1",NAND(0, 1)) # 1
  print("1 0",NAND(1, 0)) # 1
  print("1 1",NAND(1, 1)) # 0
  print("--OR--")
  print("0 0",OR(0, 0)) # 1
  print("0 1",OR(0, 1)) # 1
  print("1 0",OR(1, 0)) # 1
  print("1 1",OR(1, 1)) # 0

def OR(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.2
  tmp = np.sum(w*x) + b
  if tmp <= 0:
    return 0
  else:
    return 1

def NAND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([-0.5, -0.5])
  b = 0.7
  tmp = np.sum(w*x) + b
  if tmp <= 0:
    return 0
  else:
    return 1

if __name__ == "__main__":
    #ex_2_3_1()
    #ex_2_3_2()
    ex_2_3_3()

