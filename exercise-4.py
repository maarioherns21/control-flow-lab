# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
print('Enter the lengths of three side of a triangle:')
a = input('a: ')
b = input('b: ')
c = input('c: ')
# while loop 
while a != "quit":
#      equalateral - all three sides are equal in length
    if a == b and b == c:
        print(f"the sides are: {a} {b} {c} all three sides are equal in length so is a equalateral")
#      scalene - all three sides are unequal in length
    elif a != b and a != c and b != c:
        print(f"the sides are: {a} {b} {c} all three sides are unequal in length so is a scalane")
#      isosceles - two sides are the same length
    else:
        print(f"the sides are:{a} {b} {c} two sides are the same length so is a isosceles")
#    loooping    
    print('Enter the lengths of three side of a triangle:')
  


