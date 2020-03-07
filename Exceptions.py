first_num=int(input("Enter First Number"))
second_num=int(input("Enter Second Number"))

try:
    result=first_num/second_num
except TypeError as e:
    print("Both inputs should be numbers ")
    result='undefined'
except ZeroDivisionError as e:
    print("Second number can't be 0 ")
    result = 'undefined'
except Exception as e:
    print("Some error occured. Try again!")
    result = 'undefined'

print("The result is ",result)
