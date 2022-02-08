n, m = map(int, input().split())


mmap = []
for x in range(n):
    mmap.append([])
    for y in range(m):
        mmap[x].append(0)


k = int(input())
for i in range(k):
    x, y = map(int, input().split())
    ex = x - 1
    ey = y - 1
    mmap[ex][ey] = "*"
    if ex - 1 >= 0 and mmap[ex - 1][ey] != "*":  # bala
        mmap[ex - 1][ey] += 1

        if ey - 1 >= 0 and mmap[ex - 1][ey - 1] != "*":  # chapbala
            mmap[ex - 1][ey - 1] += 1

        if ey + 1 <= m - 1 and mmap[ex - 1][ey + 1] != "*":  # rastbala
            mmap[ex - 1][ey + 1] += 1
    if ex + 1 <= n - 1 and mmap[ex + 1][ey] != "*":  # paeen
        mmap[ex + 1][ey] += 1

        if ey - 1 >= 0 and mmap[ex + 1][ey - 1] != "*":  # chappaeen
            mmap[ex + 1][ey - 1] += 1
        if ey + 1 <= m - 1 and mmap[ex + 1][ey + 1] != "*":  # rastpaeen
            mmap[ex + 1][ey + 1] += 1
    if ey - 1 >= 0 and mmap[ex][ey - 1] != "*":  # chap
        mmap[ex][ey - 1] += 1
    if ey + 1 <= m - 1 and mmap[ex][ey + 1] != "*":  # rast
        mmap[ex][ey + 1] += 1


for i in range(n):
    for j in range(m):
        print(mmap[i][j], end=" ")
    print(end="\n")
