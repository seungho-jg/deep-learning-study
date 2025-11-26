# 02 퍼셉트론 25.11.26

# p.51 퍼셉트론 구현하기

# 논리 회로 구현

def AND(x1, x2):
  w1, w2, theta = 0.5, 0.5, 0.7
  tmp = x1*w1 + x2*w2
  if tmp <= theta:
    return 0
  elif tmp > theta:
    return 1
  
AND(0, 0)
AND(1, 0)
AND(0, 1)
AND(1, 1)

