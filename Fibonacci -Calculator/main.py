print('--------------------------')
print('|The Fibonacci Calculator|')
print('--------------------------')

num = int(input('How many digits of the Fibonacci Sequence do you want to compute: '))

fib = [1, 1]
for i in range(num-2):
  new_fib = fib[i] + fib[i+1]
  fib.append(new_fib)

print("\nThe first " + str(num) + " numbers of the Fibonacci Sequence are: ")
for number in fib:
  print(number)

golden = []
for i in range(len(fib)-1):
  ratio = fib[i+1]/fib[i]
  golden.append(ratio)

print("\nThe corresponding Golden Ratio values are: ")
for ration in golden:
  print(ratio)