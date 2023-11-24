def exactly_two_positive(a, b, c):
    positive_count = 0
    
    #Check if each number is positive 
    #Then increment the count if so
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    
    #Return true if exactly two numbers are positive, otherwise false
    return positive_count == 2

