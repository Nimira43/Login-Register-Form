print('--------------------------')
print('|The Fibonacci Calculator|')
print('--------------------------')

try:
  num = int(input('How many digits of the Fibonacci Sequence do you want to compute: '))
  if num < 2: 
    raise ValueError("Number must be at least 2")
  
  fib = [1, 1]
  for i in range(num-2):
    new_fib = fib[i] + fib[i+1]
    fib.append(new_fib)

  print(f"\nThe first {num} numbers of the Fibonacci Sequence are: ")
  for number in fib:
    print(number)

  golden = []
  for i in range(len(fib)-1):
    ratio = fib[i+1]/fib[i]
    golden.append(ratio)

  print("\nThe corresponding Golden Ratio values are: ")
  for ratio in golden:
    print(f"{ratio}")

  print("\nThe ratio of consecutive Fibonacci terms approaches Phi - 1.618033988749895 - with the more values computed.")

except ValueError as e: 
  print(f"Invalid input: {e}")