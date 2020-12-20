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
import csv
import time
import pandas as pd


def printProb():
    """
    Experiment: guess 1 to 4 for 24 times, record correct times
    Print The probability that the number of guesses
    is greater than or equal to that number
    return: Probability
    """
    N = 24
    MAX_N = 10000
    cnt = np.zeros(N)
    for i in range(MAX_N):
        ans = np.random.randint(1, 5, N)
        guess = np.random.randint(1, 5, N)
        right_num = sum(ans == guess)
        cnt[right_num] += 1
    #
    # plt.bar(range(len(cnt)), cnt / MAX_N)
    # plt.show()
    prob = cnt / MAX_N
    # prob_cnt = 0
    # for i in range(1, 16):
    #     print(i, end='\t\t')
    # print()
    # for i in range(15):
    #     prob_cnt += prob[i]
    #     print("%.1f" % ((1 - prob_cnt) * 100), "%", end='\t')
    # print()
    return prob


def printProbInfo(num):
    prob = printProb()
    print("correct times = %d, prob = %.1f" % (num, prob[num] * 100),"%")
    prob_cnt=0
    for i in range(num):
        prob_cnt += prob[i]
    print("大于等于该次数的概率为：%.1f" % ((1 - prob_cnt) * 100), "%", end='\t')
    print()
def record_experiment():
    correct_num = int(input("input correct number?："))
    note = input("any note?")
    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open('records.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        # writer.writerow(['correct number','note','time'])
        writer.writerow([correct_num, note, times])
    printProbInfo(correct_num)

record_experiment()
