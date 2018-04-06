import math

nbr_of_tests = 0
test_cases = []
results = []

with open("B-tests.in", 'r') as file:
    nbr_of_tests = int(file.readline())
    for i in range(nbr_of_tests):
        test_cases.append((file.readline().split(), file.readline().split()))

for test in test_cases:
    (l1, l2) = test
    l1 = list(map(int, l1))
    l2 = list(map(int, l2))
    n = l1[0]
    k = l1[1]
    if n == 1:
        results.append(l2[0])
        continue
    if k == 0:
        results.append(sum(l2) / n)
        continue
    if sum(l2) / n == l2[0]:
        results.append(l2[0])
        continue
    p = 1 - math.pow(1 / n, k + 1)
    m = max(l2)
    l2.remove(m)
    e = p * m + (1 - p) * sum(l2) / (n - 1)
    results.append(e)

for i in range(len(results)):
    print("Case #", i + 1, ": ", '{0:.6f}'.format(results[i]), sep='')
    