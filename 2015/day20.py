import numpy as np


def calculate_presents(n):
    return 10*(n+1 + sum(factors(n)))

def factors(n):
    return (i for i in range(2, n//2+1) if n%i == 0)

for i in range(17):
    print(i, calculate_presents(i))

a = np.zeros(1081080, np.int32)
# a = np.zeros(100, np.int32)

for i in range(2, len(a//2)):
    for j in range(i, min((len(a),50*i+1)), i):
        if a[j] == 0:
            a[j] = 11
        a[j] += 11*i
        if a[j] >= 36000000:
            print(j, a[j])
            exit()

print(a[:30])



#between 720720 and 1081080

# for i in range(720720, 1081081):
#     if calculate_presents(i)>= 36000000:
#         print(i)
