#This is a program to find the square root of any number upto The
#number of decimal places user needs, the beauty of this code here is
#it can give results upto more number of decimal places then an inbuilt
#function could give
import math
number = input("Enter a number you want to find square root of: ")
isnegative = False
if float(number)< 0:
    isnegative = True
    number = number[1:]
decimal_places_required = int(input("Enter a number of decimal places required: "))
if decimal_places_required<0:
    print("Negative number of decimal places is not possible hence assigning the required number of decimal places to 0")
    decimal_places_required = 0
list_number = list(number)
try:#to find if the number is integer or floating point number
#and locate the decimal point so as to add 00 after each operation
#done after decimal
    point_indx = list_number.index(".")
#    print(point_indx)
    list_number.remove(".") #removing the decimal place as it is not required
    #during operations
except:
    point_indx = 0
if point_indx >0:
    digits_before_decimal = point_indx #getting number of digits before decimal
else:
    digits_before_decimal = len(number) #to put the decimal sign
#print(int(digits_before_decimal/2))
if digits_before_decimal%2==0:
    index_decimal_point = int(digits_before_decimal/2) #as operations are done taking two digits at a time
else:
    index_decimal_point = int(digits_before_decimal/2)+1
#print("index_decimal_point is",index_decimal_point)
#if the number is not integer
counter_digits_before_decimal = 0 #just to make sure number of digits before decimal is dealt with
list_number = list_number + [00]*2*decimal_places_required
result_list= list() #to store quotient
if (len(list_number)%2)!=0 and point_indx==0:
    list_number=['0']+list_number # if number is integer and odd number then a 0 is added at the beginning
else:
    if point_indx%2!=0:
        list_number = ['0'] + list_number # if floating number then digits before decimal is odd
        #then a 0 is added before
#print(list_number)
remainder=0 #Used for remainder after every operation
#m=0
y=0
while(len(list_number)>0):#see each digit is used in operations
    try:
        dividend = 100*remainder+10*int(list_number[0])+int(list_number[1]) #dividend
        list_number.remove(list_number[0]) #digits are removed from beginning after being used
        list_number.remove(list_number[0])
        #print("dividend is", dividend)
    except:
    #this is for case after decimal if there are odd digits then len(list_number)
    #will always be 1 if this is not done and we will go in infinite loop
        list_number.remove(list_number[0])
        #print("dividend is", dividend)
    if(dividend <= y):
        result_list.append(0)
        counter_digits_before_decimal+=1
        if(counter_digits_before_decimal == index_decimal_point):
            result_list.append(".")
        remainder = dividend
        y=10*y
    else:
        for i in range(y+1,int(dividend)+2):
        #    print("i is",i)
            if(i*(i-y)>dividend):
                x = i-1 #To find the divisor(number we generally write on left)
        #        print("x is ",x)
                z = x-y #To find the multiplier(number we write on top)
        #        print("z is ",z)
                break
            elif(i*(i-y) == dividend):
                x = i #To find the divisor(number we generally write on left)
        #        print("x is ",x)
                z = x-y #To find the multiplier(number we write on top)
        #        print("z is ",z)
                break
        y=10*(x+z) #assign the number on left(divisor) on next stage
        #print("y is ",y)
        result_list.append(x%10) # since only last digit should be added to  quotient
        #print("after an append",result_list)
        counter_digits_before_decimal+=1
        #print("counter_digits_before_decimal is",counter_digits_before_decimal)
        if(counter_digits_before_decimal==index_decimal_point):
            result_list.append(".")
        remainder = dividend - x*z
#print(result_list)
for i in range(len(result_list)):
    result_list[i]=str(result_list[i])
final_ans = ''.join(result_list)
final_ans = round(float(final_ans),decimal_places_required)
if 0 == decimal_places_required:
    if True == isnegative:
        print("The required square root of {} without any decimal place is {}i which is round off to nearest integer.".format(number, int(final_ans)))
    else:
        print("The required square root of",number,"without any decimal place is",int(final_ans),"which is round off to nearest integer.")
else:
    if True == isnegative:
        print("The required square root of {} is {}i".format(number,final_ans))
    else:
        print("The required square root of",number,"is",final_ans)
#print("The square root of",number,"using inbuilt function is",math.sqrt(float(number)))