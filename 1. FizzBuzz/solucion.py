#Escribe un programa que imprima los números del 1 al 100, 
#pero aplicando las siguientes reglas:
#Si el número es divisible entre 3, imprime Fizz
#Si el número es divisible entre 5, imprime Buzz
#Si el número es divisible entre 3 y 5, impriþme FizzBuzz

for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
