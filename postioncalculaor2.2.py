# Position calculator
# begginer stage porject
# Risk Will be 200rs per trade
print("Entry Price:")
EP = input()
print("Stop loss:")
SL = input()
print("Risk:")
R = input()
if EP is float and SL is float and R is int:
   M = float(EP)-float(SL)
   print('Qty:',float(R)/M)
elif EP is int and SL is int and R is int:
     M = int(EP)-int(SL)
     print('Qty:',int(R)/M)
else:
    print("Error")
#this would be my first self tought project
