import sys
def calculate_sum():
    total_sum = 0
    while True:
        try:
            num = int(input("Enter a number to add or (non-integer to exit): "))#sys.stdin is used when you call the input() function
            total_sum += float(num)
        except ValueError:
            break
    print("Total sum is: ",total_sum)
calculate_sum()