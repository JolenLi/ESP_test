# !/usr/bin/env python
# encoding: utf-8
'''
@author: Jolen Li
@contact: jolen4@gmail.com
@github: https://github.com/JolenLi
@software: pycharm
@file: Gaussian_probability.py
@time: 2020/12/20 3:32 下午
@desc:
'''

import numpy as np
import matplotlib.pyplot as plt

N = 24
MAX_N = 1000000
cnt = np.zeros(N)
for i in range(MAX_N):
    ans = np.random.randint(1, 5, N)
    guess = np.random.randint(1, 5, N)
    right_num = sum(ans == guess)
    cnt[right_num] += 1

plt.bar(range(len(cnt)), cnt / MAX_N)
plt.show()
prob = cnt / MAX_N
prob_cnt = 0
for i in range(N):
    print(i, end='\t\t')
print()
for i in range(N):
    prob_cnt += prob[i]
    print("%.3f" % (1-prob_cnt), end='\t')
print()
