# 方法 1
def power2na(n):
    return 2**n

# 方法 2a：用遞迴
def power2nb(n):
    if n == 0:
        return 1
    return power2nb(n-1) + power2nb(n-1)

# 方法2b：用遞迴
def power2nc(n):
    if n == 0:
        return 1
    return 2 * power2nc(n-1)
    # 2*power2n(n-1)

cache = [1]  # cache[0]=1

# 方法 3：用遞迴+查表
def power2ne(n):
    #print(len(cache),n,cache[0])
    if n <= len(cache)-1:
        return cache[n]
    cache.append(power2ne(n-1)+power2ne(n-1))
    return cache[n]
    # if ....
    # power2n(n-1)+power2n(n-1) 


print("power2ne(5)=", power2ne(100))