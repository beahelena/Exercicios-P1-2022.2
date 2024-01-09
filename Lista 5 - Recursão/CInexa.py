numbers = input()
n = int(input())
number1, number2, number3 = numbers.split()
difference = int(number2) - int(number1)

def pa(n, number1, difference):
  if n == 1:
    return int(number1)
  else:
    return pa(n-1, number1, difference) + difference

result = pa(n, number1, difference)

print(f"Na progressão aritmética cujos três primeiros números são {number1}, {number2} e {number3}, o {n}º elemento é {result} e a razão da progressão é {difference}.")