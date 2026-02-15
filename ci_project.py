#compound interest 
p = float(input("enter your principle amount: "))
r = float(input("enter your rate of interest : "))
t = float(input("enter your time interval : "))

amount= p*(1 + r/100)**t
ci = amount - p 
print("your compound interest: ", ci)
print("total amount:", p+ci )

