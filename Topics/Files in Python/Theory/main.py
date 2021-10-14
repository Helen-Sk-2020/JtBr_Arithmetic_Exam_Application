#  You can experiment here, it won’t be checked
def check():
    x = int(input())
    min_border = 25
    max_border = 38
    try:
        if x in range(min_border, max_border):
            print(x)
        else:
            print("Correct the error!")
    except ValueError:
        print("Correct the error!")



