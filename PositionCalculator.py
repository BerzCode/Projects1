# Position calculator
# begginer stage porject
# Risk Will be 200rs per trade
print("Entry Price:")
EP = input()
print("Stop loss:")
SL = input()
print("Risk:")
R = input()
m = int(EP)-int(SL)
print("Position Size =",int(R)/m )


