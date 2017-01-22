def zero_matrix(arr):
    zero_rows, zero_cols = {}, {}
    n = len(arr[0])
    m = len(arr)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                zero_rows[i] = True
                zero_cols[j] = True
    result = [[]]
    for i in range(n):
        for j in range(m):
            if zero_rows.get(i) or zero_cols.get(j):
                arr[i][j] = 0

test = [[1,2,3,0], [1,0,2,3], [1,3,2,3], [1,3,2,3]]
for row in test:
    print(row)

zero_matrix(test)

for row in test:
    print(row)
