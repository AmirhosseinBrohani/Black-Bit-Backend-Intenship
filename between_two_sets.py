def getTotalX(a, b):
    # Write your code here
    mark = 0

    a_lcm = a[0]
    for i in range(1, len(a)):
        a_lcm = math.lcm(a_lcm, a[i])
    b_gcd = b[0]
    for j in range(1, len(b)):
        b_gcd = math.gcd(b_gcd, b[j])
    if b_gcd % a_lcm != 0:
        return 0
    itter = int(b_gcd / a_lcm)
    for i in range(1, itter + 1):
        if b_gcd % (i * a_lcm) == 0:
            mark += 1
    return mark
