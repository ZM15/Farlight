def fun(num):
    fir = num // 1000  # the first three numbers
    sec = num - fir * 1000  # the second three numbers

    sum1 = (fir // 100) + ((fir // 10) % 10) + (fir % 10)
    sum2 = (sec // 100) + ((sec // 10) % 10) + (sec % 10)

    if 99999 < num < 1000000:
        if sum1 == sum2:
            print("The entered number is a lucky number!!!")
        else:
            print("The entered number is not a happy one. You'll definitely get lucky next time!!!")

    else:
        print("You entered the wrong number.")
if __name__ == "__main__":
    a = int(input("Enter a six-digit integer: "))
    fun(a)
