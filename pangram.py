
def pangram(str):
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   for char in alphabet:
      if char not in str.lower():
         return False
   return True

string = 'The five boxing wizards jump quickly.'
if(pangram(string) == True):
   print("pangram")
else:
   print("not pangram")