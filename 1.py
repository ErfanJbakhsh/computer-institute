import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()  
        result = func(*args, **kwargs)  
        end = time.time()  
        print(f"زمان اجرا: {end - start:.6f} ثانیه")
        return result
    return wrapper
    
@time_it
def creat_list(n):
    list = []
    for i in range(1, n+1):
        if i <= n:
            list.append(i)
    return list

n = int(input())
print(creat_list(n))