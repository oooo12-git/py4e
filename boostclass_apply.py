
# 1-1

# sum = 0

# for i in range(1,10):
#     if i % 2 == 0:
#         sum += i
# print(sum)


# 1-2

# sum = 0

# for i in range(1,10):
#     if i % 3 == 1:
#         sum += i
# print(sum)

# 1-3

# sum = 0

# for i in range(1,10):
#     if i % 4 == 0:
#         sum += i
# print(sum)

# 1-4

# sum = 0

# for i in range(1,10):
#     if i % 6 == 3:
#         sum += i
# print(sum)

import numpy as np

m = np.array([[2],[4],[6]])
n = np.array([[1],[3],[5]])

print(m.T @ n)

