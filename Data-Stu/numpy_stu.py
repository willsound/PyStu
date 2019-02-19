import numpy as np

#  1D Array
a = np.array([0, 1, 2, 3, 4])
b = np.array((0, 1, 2, 3, 4))
c = np.arange(5)
d = np.linspace(0, 2*np.pi, 5)
print(a)
print(b)
print(c)
print(d)
print(a[3])

# MD Array,
md_a = np.array([[11, 12, 13, 14, 15],
                            [16, 17, 18, 19, 20],
                              [21, 22, 23, 24, 25],
                             [26, 27, 28 ,29, 30],
                            [31, 32, 33, 34, 35]])

print(md_a[2, 4])  # >>>25

# MD slicing
print(md_a[0, 1:4])  # >>>[12 13 14]
print(md_a[1:4, 0])  # >>>[16 21 26]
print(md_a[::2, ::2])  # >>>[[11 13 15]
                                #     [21 23 25]
                                 #     [31 33 35]]
print(md_a[:, 1])  # >>>[12 17 22 27 32]