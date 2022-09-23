from matplotlib import pyplot as plt
from supervenn import supervenn
a = {1, 2, 3, 4, 5, 6, 7, 8} ## 1- общий для всех, 2- a и b, 3 - a, b, c, 4- a, b, d, 5 - a, c, 6- a,c, d 7- a, d, 8 - a,
b = {1, 2, 3, 4, 9, 10, 11, 12} ## 9 - b, 10 - b, d, 11 - b, d, c, 12 --b, c
c = {1, 3, 5, 6, 11, 12, 13, 14} ## 13 - c, 14 - c d
d = {1, 4, 6, 7, 10, 11, 14, 15}## 15 - d
not_a = {9, 10, 11, 12, 13, 14, 15, 16}
not_d = {2, 3, 5, 8, 9, 12, 13, 16}
not_b = {5, 6, 7, 8, 13, 14, 15, 16}
not_c = {2, 4, 7, 8, 9, 10, 15, 16}
q = (((a | b) & c) | b) & d
p = ((((a | b) & not_c) | b) & d)
supervenn([a, b, c, d, q, p], ['A', 'B', 'C', 'D', 'Q', 'P8'])
plt.savefig('p8.png')
