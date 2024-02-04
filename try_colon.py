import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5])
sub_arr = arr[2:5]  # Returns array([2, 3, 4])
arr = np.array([0, 1, 2, 3, 4, 5])
sub_arr = arr[1:6:2]  # Returns array([1, 3, 5])

import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

sub_matrix = matrix[1:, :2]  # Returns array([[4, 5],
                             #                [7, 8]])

arr = np.random.rand(3, 4, 5)
sub_arr = arr[..., 2]  # Equivalent to arr[:, :, 2], returns a 2D slice along the last axis.
