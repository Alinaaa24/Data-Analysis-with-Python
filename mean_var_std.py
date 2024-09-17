import numpy as np

def calculate(list):
    size = len(list)
    if (size == 9):
        array_p = np.array(list)
        array = array_p.reshape(3, 3)
        print(array)
        calculations = {
            'mean': [np.mean(array, axis=0).tolist(),
                     np.mean(array, axis=1).tolist(),
                     np.mean(array.flatten())],

            'variance': [np.var(array, axis=0).tolist(),
                         np.var(array, axis=1).tolist(),
                         np.var(array.flatten().tolist())],

            'standard deviation':[np.std(array, axis=0).tolist(),
                                  np.std(array, axis=1).tolist(),
                                  np.std(array.flatten().tolist())],

            'max':[np.max(array, axis=0).tolist(),
                   np.max(array, axis=1).tolist(),
                   np.max(array.flatten().tolist())],

            'min':[np.min(array, axis=0).tolist(),
                   np.min(array, axis=1).tolist(),
                   np.min(array.flatten().tolist())],

            'sum':[np.sum(array, axis=0).tolist(),
                   np.sum(array, axis=1).tolist(),
                   np.sum(array.flatten().tolist())]
        }
    else:
        raise ValueError("List must contain nine numbers.")
    
    return calculations



