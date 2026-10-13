pin = input()
if (len(pin) == 4 and
    len(set(pin)) == 4 and
    not(1900<= int(pin) <= 2050)):
    print("OK")
else:
    print("ERROR")