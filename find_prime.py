number = int(input("Enter any Number: "))
i = 2
if (number <= 1):
    print("Not Prime")
elif (number == 2):
    print("Prime")
else:
    while (i <= number//2):
        mod = number % i
        if mod == 0:
            print('Not Prime')
            break
        i = i+1
    else:
        print('Prime')
