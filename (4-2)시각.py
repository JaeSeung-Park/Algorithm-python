n = int(input())
h, m, s = n, 59, 59
c = 0
for i in range(h + 1):
    if h == 3 or h == 13 or h == 23:
        c += 60 * 60
        h -= 1
        continue
    else:
        h -= 1
    m = 59
    for j in range(60):
        if m == 3 or m == 13 or m == 23 or (30<= m and m<=39) or m == 43 or m == 53:
            c += 60
            m -= 1
            continue
        else:
            m -= 1
        s = 59
        for k in range(60):
            if s == 3 or s == 13 or s == 23 or (30<= s and s<=39) or s == 43 or s == 53:
                c += 1
                s -= 1
                continue
            else:
                s -= 1
print(c)

#=======================================================
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)