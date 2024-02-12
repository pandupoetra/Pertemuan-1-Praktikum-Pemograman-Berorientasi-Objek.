def prima(x):
    if x <= 1:
        return False  
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

a = int(input("Masukkan bilangan yang akan dicek: "))
if prima(a):
    print(f"{a} adalah bilangan prima")
else:
    print(f"{a} bukan bilangan prima")