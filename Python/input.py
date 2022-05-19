usrtext = input('Text: ')

print(usrtext.upper())

##### Guy in the tutorial mentions providing a colon. Fails to mention that Boris is one.

usrnum = input('What number am I thinking of? ')

print(int(usrnum)*69)

##### First asn for some text, and then prompt "Enter 1 for uppercase; 2 for lowercase:" and then do the thing

upper_or_lower = input('Enter 1 for uppercase; 2 for lowercase: ')

if upper_or_lower == "1":
    print(usrtext.upper())
else:
    print(usrtext.lower())
