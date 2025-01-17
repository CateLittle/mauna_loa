##Contains Python functions for HW08, BDS 311
##These functions will be generated collaboratively and called in each user's separate Jupyter notebook

#import standard packages here
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


def make_standard_units(input_array):
    mn_subtracted_array = input_array-np.mean(input_array)
    normalized_array = mn_subtracted_array/np.std(input_array)
    return normalized_array
    '''Converts input_array to standard_units, where data has mean 0 and standard deviation of 1
        INPUT: data array
        OUTPUT: array in standard units'''

    
def calc_corrcoef_from_standardized_input(array1, array2):
    correlation_coefficient = np.mean(array1 * array2)
    return correlation_coefficient
    '''Calculates Pearson correlation coefficient from two arrays in standard units
    INPUT: array1, array2: In standard units
    OUTPUT: Pearson correlation coefficient'''

def get_regression_parameters(array3, array4):
    ratio_of_sds = np.std(C02)/np.std(decimal_date)
    slope = corr_coef * ratio_of_sds
    intercept = np.mean(C02) - slope*np.mean(decimal_date)
    regression_array = [slope,intercept]
    return regression_array
    '''Calculates regression parameters from two input arrays
    INPUT: array1, array2: two data arrays
    OUTPUT: regression_array, length 2: regression_array[0] is slope and regression_array[1] is intercept'''



