"""Function 2

# Function 2: Metric Dictionary
Write a function which takes in a list of integers and returns a dictionary of the [five number summary.](https://www.statisticshowto.datasciencecentral.com/how-to-find-a-five-number-summary-in-statistics/) 
Answers should be rounded to the nearest second decimal.
"""
import function_1
import numpy as np

def five_num_summ(gauteng):
    maximum = function_1.get_max(gauteng)
    median = function_1.get_median(gauteng)
    minimum = function_1.get_min(gauteng)

    #code for q1
    q1 = 0
    #code for q3
    q3 = 0

    #create dictionary
    dct = {}
    dct['maximum'] = maximum
    dct['median'] = median
    dct['minimum'] = minimum
    dct['q1'] = q1
    dct['q3'] = q3

    return dct

if __name__ == '__main__':
    gauteng = [39660.0,36024.0,32127.0,39488.0,18422.0,23532.0,8842.0,37416.0,16156.0,18730.0,19261.0,25275.0]
    # print('max = ', five_num_summ(gauteng)==39660.0)
    # print('median = ', five_num_summ(gauteng)==24403.5)
    # print('min = ', five_num_summ(gauteng)==8842.0)
    # print('q3 = ', five_num_summ(gauteng)==36024.5)
