def fizzbuzz(x, y):
  for i in range(1, 101):
    output = ''
    if i % x == 0:
      output += 'Fizz'
    if i % y == 0:
      output += 'Buzz'
    if output == '':
      output = i
    print(output)
