def power_recursive(a, k, i=0):
    if i > k:
        return
    print(f"{a}^{i} = {a ** i}")
    power_recursive(a, k, i + 1)
power_recursive(2, 100)
