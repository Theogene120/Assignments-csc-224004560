#Python program to put in upper case all vowel of entered string
my_str=input('Enter a text:')
new_str=" "
for m in my_str:
    if m.lower()=="a" or m.lower()=="e" or m.lower()=="i" or m.lower()=="o" or m.lower()=="u":
        new_str+=m.upper()
    else:
        new_str+=m
print(new_str)