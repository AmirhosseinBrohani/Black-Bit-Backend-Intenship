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
    if ex - 1 >= 0 and mmap[ex - 1][ey] != "*":  # top
        mmap[ex - 1][ey] += 1

        if ey - 1 >= 0 and mmap[ex - 1][ey - 1] != "*":  # top-left-corner
            mmap[ex - 1][ey - 1] += 1

        if ey + 1 <= m - 1 and mmap[ex - 1][ey + 1] != "*":  # top-right-corner
            mmap[ex - 1][ey + 1] += 1
    if ex + 1 <= n - 1 and mmap[ex + 1][ey] != "*":  # down
        mmap[ex + 1][ey] += 1

        if ey - 1 >= 0 and mmap[ex + 1][ey - 1] != "*":  # down-left-corner
            mmap[ex + 1][ey - 1] += 1
        if ey + 1 <= m - 1 and mmap[ex + 1][ey + 1] != "*":  # down-right-corner
            mmap[ex + 1][ey + 1] += 1
    if ey - 1 >= 0 and mmap[ex][ey - 1] != "*":  # left
        mmap[ex][ey - 1] += 1
    if ey + 1 <= m - 1 and mmap[ex][ey + 1] != "*":  # right
        mmap[ex][ey + 1] += 1


for i in range(n):
    for j in range(m):
        print(mmap[i][j], end=" ")
    print(end="\n")
