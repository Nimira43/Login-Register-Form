print('The Fibonacci Calculator')

num = int(input('How many digits of the Fibonacci Sequence do you want to compute: '))

fib = [1, 1]
for i in range(num-2):
  new_fib = fib[i] + fib[i+1]
  fib.append(new_fib)
print(fib)

