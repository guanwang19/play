import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5])
sub_arr = arr[2:5]  # Returns array([2, 3, 4])
arr = np.array([0, 1, 2, 3, 4, 5])
sub_arr = arr[1:6:2]  # Returns array([1, 3, 5])
print("arr[0:6:2]:  "+ str(arr[0:6:2]))
print(arr[::2])
print(f"arr[::-2]: {arr[::-2]}")
print(f"arr[::-1]: {arr[::-1]}")
# from chatgpt:
# The first colon (:) before the first empty position indicates the starting point of the slice. When omitted, it defaults to the beginning of the array.
# The second colon (:) after the first empty position indicates the ending point of the slice. When omitted, it defaults to the end of the array.
# The -1 after the second colon indicates the step size. A step of -1 means that the slicing will move through the array in reverse order.
# So, arr[::-1] means "start from the end, move towards the beginning, and take every element in reverse order."

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

sub_matrix = matrix[1:, :2]  # Returns array([[4, 5],
                             #                [7, 8]])

arr = np.random.rand(3, 4, 5)
sub_arr = arr[..., 2]  # Equivalent to arr[:, :, 2], returns a 2D slice along the last axis.
