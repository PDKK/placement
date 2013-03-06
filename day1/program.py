def count(number):
 i = 0
 while(i < number):
  i = i + 1
  print i

def f(z):
 return z+z
def main():
 insertnumber = input("Enter the number you would like to count to")
 count(insertnumber)
 count(f(5))

main()
