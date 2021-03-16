#Fizzbuzz

def fizzbuzz(num):
    for i in range(num+1):
        if (i % 15 == 0):  
            print('Fizzbuzz')
        elif (i % 3 == 0):
            print('Fizz')
        elif (i % 5 == 0):
            print('Buzz')
        else:
            print(i)

fizzbuzz (20)

#apakah bisa (i % 3 and 5 == 0)

#apakah elif kedua bisa dijadikan sebagai else?