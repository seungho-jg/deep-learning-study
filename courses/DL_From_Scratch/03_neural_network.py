# 03 신경망 25.12.02
import numpy as np
import matplotlib.pylab as plt

def main():
    print('ji')

def ex_3_1():
    """ 퍼셉트론에서 신경망으로 """
    print('y = h(b + w1*x1 + w2*x2)')

def ex_3_2():
    """ 계단 함수 구현하기 """
    def step_function(x):
        if x > 0:
            return 1
        else:
            return 0
        
    def step_function_np(x):
        y = x > 0
        return y.astype(np.int64)
    
    print("1: ", step_function(1))
    print("2: ", step_function_np(np.array([0, 2, 3, 4])))

    def step_function_np2(x):
        return np.array(x > 0, dtype=np.int64)
    
    x = np.arange(-5.0, 5.0, 0.1)
    y = step_function_np2(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1) # y축의 범위 지정
    plt.show()

def ex_3_2_4():
    """ 시그모이드 함수 """
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))
    x = np.arange(-5.0, 5.0, 0.1)
    y = sigmoid(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()

def ex_3_2_7():
    """ ReLU 함수 """
    def relu(x):
        return np.maximum(0, x)
    x = np.arange(-5.0, 5.0, 0.1)
    y = relu(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 5)
    plt.show()

# 3.3 다차원 배열의 연산


if __name__ == "__main__":
    ex_3_2_7()
    pass