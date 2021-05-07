try:
    n = list(map(int, input().split()))
except:
    ValueError
    print("valueeror")

print(sum(n))
