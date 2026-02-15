#simple interst = P*R*T/100
PRINCIPLE= float(input("enter your principle amount: "))
RATE = float(input("enter your rate of interst:" ))
TIME =float(input("enter your time interval: "))
 
simple_interest= (PRINCIPLE*RATE*TIME/100)
print("simple interest: ", simple_interest)
print("total amount : ", simple_interest + PRINCIPLE)
