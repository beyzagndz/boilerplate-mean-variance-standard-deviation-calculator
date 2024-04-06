import numpy as np

def calculate(list):
    #using raise ValueError when the passed in parameter of the function-list- does not contain 9 digit as wanted
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    #converting list to an array -by default a 1D array)
    list_to_array = np.array(list)
    #converting 1D array to 3x3 matrix
    array_to_3x3 = list_to_array.reshape(3,3)
    #converting 3x3 matrix to flattened back to 1D
    fl_array = array_to_3x3.flatten()
    #using mean function to calculate the mean of axis 0, axis 1, flattened
    axis_zero_mean = array_to_3x3.mean(axis = 0)
    axis_one_mean = array_to_3x3.mean(axis = 1)
    fl_mean = fl_array.mean()
    #using var function to calculate variance of axis 0, axis 1, flattened
    axis_zero_var = array_to_3x3.var(axis = 0)
    axis_one_var = array_to_3x3.var(axis = 1)
    fl_var = fl_array.var()
    #using std function to calculate standard deviation for axis 0, axis 1, flattened
    axis_zero_std = array_to_3x3.std(axis = 0)
    axis_one_std = array_to_3x3.std(axis = 1)
    fl_std = fl_array.std()
    #using max function to calculate max of axis 0, axis 1, flattened
    axis_zero_max = array_to_3x3.max(axis = 0)
    axis_one_max = array_to_3x3.max(axis = 1)
    fl_max = fl_array.max()
    #using min function to finde the smallest value of arrays along axis 0, axis 1, flattened
    axis_zero_min = array_to_3x3.min(axis = 0)
    axis_one_min = array_to_3x3.min(axis = 1)
    fl_min = fl_array.min()
    #using sum function to find the sum of each axis 0, axis 1, flattened
    axis_zero_sum = array_to_3x3.sum(axis = 0)
    axis_one_sum = array_to_3x3.sum(axis = 1)
    fl_sum = fl_array.sum()




    return calculations
