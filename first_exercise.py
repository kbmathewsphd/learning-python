#first exercise
while True:
  print("\n")
  print ("select choice")
  print ("1: surface area\n2: volume\n3: exit")
  choice=int(input("enter choice: "))
  if(choice==1):
    length=int(input("enter length: "))
    print("surface area", 6*length**2)
  elif(choice==2):
    length=int(input("enter length: "))
    print("volume", length**3)
  elif(choice==3):
    print("exit")
    break