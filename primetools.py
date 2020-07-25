def is_prime(a):
  if a == 2 or a == 3:
      return "prime"
  elif a== 1:
      return "don't know"
  elif a == 0:
      return "zero"
  elif a%2 == 0:
    return "even"


  else:
    t = (a//2)
    for i in range(2,t+1):
        if a%i == 0:
            return f"not prime and dividable by {i}"
            break
        elif i >= t:
            return "prime"

