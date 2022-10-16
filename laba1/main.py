from numgen_1 import Generator1
from numgen_2 import Generator2
from numgen_3 import Generator3

num_of_values = 10000
bins = 20
num_of_test = 3
list_of_lambda = [1, 0.5, 10]

for lambda_val in list_of_lambda:
    print(f'\t###__Lambda = {lambda_val}__###')
    generator_1 = Generator1(lambda_val, num_of_values)
    generator_1.analyze(bins)
    print()

list_of_alpha = [1, 0.3, 11]
list_of_sigma = [2, 0.8, 15]

for i in range(0, num_of_test):
    print(f'\t###__Alpha = {list_of_alpha[i]}; Sigma = {list_of_sigma[i]}__###')
    generator_2 = Generator2(list_of_alpha[i], list_of_sigma[i], num_of_values)
    generator_2.analyze(bins)
    print()

list_of_a = [pow(5, 13), pow(5, 3), pow(5, 2)]
list_of_c = [pow(2, 31), pow(2, 7), pow(2, 5)]


for i in range(0, num_of_test):
    print(f'\t###__A = {list_of_a[i]}; C = {list_of_c[i]}__###')
    generator_3 = Generator3(num_of_values, list_of_a[i], list_of_c[i])
    generator_3.analyze(bins)
    print()
