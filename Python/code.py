

def main():
    x = int(input("x= "))
    y = int(input("y= "))
    swap (x,y)
    print(f"x= {x} || y= {y}")



def swap(x,y):
    temp = x
    x = y
    y = temp
    print(f"x= {x} || y= {y} --swap")
main()