def func1():
    try:
        l = [1,5,6,7]
        i = int(input("Enter any index: "))
        print(l[i])
        return 0
    except:
        print("Some error occurred")
        return 1
    finally:
        print("I'm always executed")
    # print("I'm always executed")

x = func1()
print(x)