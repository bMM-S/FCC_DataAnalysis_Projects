import numpy as np

def calculate(lst):

    if len(lst)!=9:
        raise ValueError("List must contain nine numbers.")

    matrix = [lst[i*3:(i+1)*3] for i in range(3)]
    
    mean_values = [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(lst)]
    var_values = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(lst)]
    std_values = [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(lst)]
    max_values = [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(lst)]
    min_values = [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(lst)]
    sum_values = [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(lst)]

    calculations = {'mean' : mean_values,
                    'variance' : var_values,
                    'standard deviation' : std_values,
                    'max' : max_values,
                    'min' : min_values,
                    'sum' : sum_values}

    return calculations
