v=int(input("wind speed in m/s:"))
t=int(input("temperature in degree celsius"))
z=13.12+0.6215*t-11.37*v**0.16+0.3965*t*v**0.16
print(z)