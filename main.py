import random

# Question 1
"""Write a program that randomly generates an integer number from
O to 1000,if 0 is generated, calculate and display the average
of all generated numbers."""
def main():
    total = 0
    numbers = []

    while True:
        num = random.randint(0, 1000)
        if num == 0:
            numbers.append(num)
            print("Generated 0 at after ", len(numbers), "random numbers.")
            print("Total generated numbers: ", len(numbers))
            print("The generated numbers are: \n")
            print("Average of all generated numbers:", total / len(numbers))
            break
        numbers.append(num)
        total += num
        print(num)
main()

# Question 2
"""Write a program that inputs an integer number from the keyboard,
randomly generates integer numbers for input number times from -50 to 50,
calculate the average of all generated numbers."""
def main1():
    n = int(input("Enter the number of times to generate random numbers: \n"))
    total_sum = 0
    print("Generated numbers:")
    for _ in range(n):
        numb = random.randint(-50, 50)
        total_sum += numb
        print(numb)
    average = total_sum / n
    print("Average of all generated numbers:", average)

main1()
