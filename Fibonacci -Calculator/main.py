print('--------------------------')
print('|The Fibonacci Calculator|')
print('--------------------------')

num = int(input('How many digits of the Fibonacci Sequence do you want to compute: '))
print   ('--------------------------------------------------------------------')

fib = [1, 1]
for i in range(num-2):
  new_fib = fib[i] + fib[i+1]
  fib.append(new_fib)

print("The first " + str(num) + " numbers of the Fibonacci Sequence are: ")
for number in fib:
  print(number)
print   ('--------------------------------------------------')

