string = input()



def turing(string):
  if len(string) == 1:
    return string
  else:
    return string[-1] + turing(string[:-1])

print(turing(string))