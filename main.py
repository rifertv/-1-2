def multi (number: int) -> int:
  t = 1
  for n in str(number):
    if int(n) > 0:
     t *= int(n)
  return t 

if __name__ == '__main__':
    print('Example:')
    print(multi(123405))
    
  
    assert multi(123405) == 120
    assert multi(999) == 729
    assert multi(1000) == 1
    assert multi(1111) == 1
    print("Cool!")