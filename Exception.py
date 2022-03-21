a=int(input())
b=int(input())
try:
    print("hello")
    print(a/b)
except Exception as e:
    print("Check the values of inputs",e)
finally:
    print("Bye~")