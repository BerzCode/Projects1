# Position calculator
# begginer stage porject
# Risk Will be 200rs per trade
print("Entry Price:")
EP = input()
print("Stop loss:")
SL = input()
print("Risk:")
R = input()
print("What you want to do?"+'1,2')
T = input()
if T =='1':
   M = int(EP)-int(SL)
   print('Qty:',int(R)/M)
elif T == '2':
     M = float(EP)-float(SL)
     print('Qty:',float(R)/M)
else:
    print("Error")
#this would be my first self tought project
#i wanna thank me and my curious mind
#this is a test