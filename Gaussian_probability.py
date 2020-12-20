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


def printProbInfo():
    prob = printProb()
    for i in range(1, 15):
        print("correct times = %d, prob = %.1f" % (i, prob[i] * 100))


printProbInfo()


def record_experiment():
    str = input("请输入：");
    correct = 1
    note = "none"
    timeNow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    dataframe = pd.DataFrame({'correct number': correct, 'note': note, "time": timeNow})
    dataframe.to_csv("records.csv", mode='a', header=False, index=False, sep=',')
record_experiment()