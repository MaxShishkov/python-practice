def digit_sum(n):
    numbers = []
    while n > 0:
        #get the rightmost digit of the number 1234%10 = 4
        numbers.append(n % 10)
        #remove the rightmost digit using floor division
        n = n // 10
    
    total = 0
    for number in numbers:
        total += number
    
    return total
    
print digit_sum(1234)