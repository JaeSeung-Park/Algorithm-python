# 행의 개수n, 열의 개수m
n, m = map(int, input().split())
result = 0
for i in range(n):
    a = list(map(int, input().split()))
    a.sort()
    if a[0] >= result:
        result = a[0]
        
print(result)

# min() 함수 사용
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
    
print(result)