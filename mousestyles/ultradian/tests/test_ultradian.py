#Test
import pytest
import pandas as pd

#Check the outcome data type of function aggregate_interval()
def aggregate_interval_test(strain, mouse, feature, bin_width):
    result = aggregate_interval(strain, mouse, feature, bin_width)
        assert type(result) is pd.tseries.index.DatetimeIndex

#Check the outcome data type of function aggregate_movement()
def aggregate_movement_test(strain, mouse, bin_width):
    result = aggregate_movement(strain,mouse, bin_width)
        assert type(result) is pd.tseries.index.DatetimeIndex

#Check the outcome data type of function aggregate_data()

#First to check to data type
def aggregate_data_test(feature, bin_width):
    result = aggregate_data(feature, binwith)
        assert type(result) is pd.core.frame.DataFrame
#Then to check the number of columns
def aggregate_data_test_columns(feature, binwith):
    result = aggregate_data(feature, binwith)
        n = len(result.columns)
        assert n == 4

#Check the data type of seasonal decomposition
def seasonal_decomposition_test(strain, mouse, feature, bin_width, period_length):
    resul = seasonal_decomposition(strain, mouse, feature, bin_width, period_length)
        assert tyep(result) = statsmodels.tsa.seasonal.DecomposeResult

#strain_seasonal is to produce a plot, so I think we can check the plot directly istead of writing a test function

#check the outcome range of mix_strain
def mix_strain_test(data, feature):
    result = mix_strain(data, feature)
        assert  0 < result < 1