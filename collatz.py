def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

def main():
    try:
        number = int(input(("Enter number: ")))
        while number != 1 :
            number = collatz(number)
            print(number, end=' ')
    except(ValueError):
        print("Invalid input")

main()