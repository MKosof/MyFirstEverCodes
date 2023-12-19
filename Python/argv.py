from sys import argv,exit
# exit is the same as return in main in C, stops the program and returns a number 
if len(argv)>= 2:
    print(f"Hello,",end="")
    
    #for i in range(len(argv)-1):
    #   print(argv[i+1].lower(),end=" ")    # same as below
    for arg in argv[1:]:
        print(arg, end=" ")
    
    print()
    exit(0)

else:
    print("Hello world!")
    exit(1)