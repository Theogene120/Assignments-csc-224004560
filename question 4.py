#Python program to check prefect number from 1 to 1M

print('Perfect number between 1 and 1,000,000 are:')
for number in range(1,10000001):
    sum=0
    for i in range(1,number):
        if number%i==0:
            sum=sum+i
    if sum==number:
        print(number)