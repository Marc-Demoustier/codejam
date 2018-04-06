nbr_of_tests = int(input())
test_cases = []
for i in range(nbr_of_tests):
    test_cases.append(input())


def is_even(s):
    for c in s:
        if int(c) % 2 != 0:
            return False
    return True


def solve(input):
    m = 0
    a = input
    while not is_even(a):
        m += 1
        a = str(int(a) - 1)

    p = 0
    b = input
    while not is_even(b):
        p += 1
        b = str(int(b) + 1)

    return min(m, p)


results = []


for i in range(nbr_of_tests):
    results.append(solve(test_cases[i]))

for i in range(len(results)):
    print("Case #", i + 1, ": ", results[i], sep='')
