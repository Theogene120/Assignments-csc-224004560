#python program to change camel case to snake case
CamelCase=input('Enter variable in camel case:')
snake_case=""
for i in CamelCase:
    if i.isupper():
        snake_case+="_"+i.lower()
    else:
        snake_case+=i
print(f'Entered variable in snake case is:\t{snake_case}')