x=3
y=0
while x!=int(y):
   print("Devinez le nombre entre 0 et 10")
   y=input()
   if x>int(y): 
      print("Plus haut")
   if x!=int(y):
      print("Plus bas")
    
print("Bingo!")

