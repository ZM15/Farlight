def fun(num):
    fir = num // 1000  # первые три числа
    sec = num - fir * 1000  # вторые три числа

    sum1 = (fir // 100) + ((fir // 10) % 10) + (fir % 10)
    sum2 = (sec // 100) + ((sec // 10) % 10) + (sec % 10)

    if 99999 < num < 1000000:
        if sum1 == sum2:
            print("Введенное число - счастливое")
        
if __name__ == "__main__":
    a = int(input("Введите целое шестизначное число: "))
    fun(a)