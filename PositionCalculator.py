# Position calculator
# begginer stage porject
# Risk Will be 200rs per trade
print("Entry Price:")
EP = input()
print("Stop loss:")
SL = input()
print("Risk:")
R = input()
print("Position Size =",int(R)/int(EP)-int(SL))
