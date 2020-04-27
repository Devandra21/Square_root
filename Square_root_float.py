#This is a program to find the square root of any number upto The
#number of decimal places user needs, the beauty of this code here is
#it can give results upto more number of decimal places then an inbuilt
#function could give
# Here it is number of digits/2
import math
a = input("Enter a number you want to find square root of: ")
decimalno = int(input("Enter a number of decimal places required: "))
b = list(a)
try:#to find is the number is integer or floating point NUMBER
#and locate the decimal point so as to add 00 after each operation
#done after decimal
    point_indx = b.index(".")
#    print(point_indx)
    b.remove(".")
except:
    point_indx = 0
if point_indx >0:
    qwe = point_indx #getting number of digits before decimal
else:
    qwe = len(a) #to put the decimal sign
#print(int(qwe/2))
if qwe%2==0:
    it = int(qwe/2)
else:
    it = int(qwe/2)+1
#print("it is",it)
ij = 0 #just to make sure number of digits before decimal is dealt with
b = b + [00]*2*decimalno
q= list()
c=['0']
if (len(b)%2)!=0 and point_indx==0:
    b=c+b
else:
    if point_indx%2!=0:
        b = c + b
#print(b)
r=0
m=0
y=0
while(len(b)>0):
    try:
        d=100*r+10*int(b[0])+int(b[1])
        b.remove(b[0])
        b.remove(b[0])
#        print(d)
    except:
        b.remove(b[0])
#        print(d)
    if(d<=y):
        q.append(0)
        ij+=1
        if(ij==it):
            q.append(".")
        r=d
        y=10*y
    else:
        for i in range(y+1,int(d)+2):
#            print(i)
            if(i*(i-y)>d):
                x = i-1 # to find the number we write on left
#                print("x is ",x)
                z = x-y # TO FIND THE NUMBER WE WRITE ON TOP
#                print("z is ",z)
                break
            elif(i*(i-y)==d):
                x=i
#                print("x is ",x)
                z=x-y
#                print("z is ",z)
                break
        y=10*(x+z)
#        print("y is ",y)
        q.append(x%10)
#        print("after an append",q)
        ij+=1
#        print("ij is",ij)
        if(ij==it):
            q.append(".")
        r=d - x*z
#print(q)
for pmn in range(len(q)):
    q[pmn]=str(q[pmn])
lmt = ''.join(q)
#while(len(q)>0):
#    m=10*m+q[0]
#    q.remove(q[0])
print("The required square root of",a,"is",lmt)
#print("The square root of",a,"using inbuilt function is",math.sqrt(float(a)))
