sh = input("Enter hours: ")
sr = input("Enter rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except: 
    print("Error plz enter numeric input")
    quit()

print(fr, fh)
if fh > 40 :
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print("Pay:",xp)