
str = input("Enter the string : ")
vowels = 0
consonants = 0
characterstics = 0
str = str.lower()
for i in range(0, len(str)):
    if (str[i] == "a" or str[i] == 'e' or str[i] == 'i'
    or str[i] == 'o' or str[i] == 'u'):
        vowels = vowels + 1
    elif ((str[i] >= 'a' and str[i] <= 'z')):
        consonants = consonants + 1
    elif (str[i] ==" " or str[i]=="!" or str[i]=="@" or str[i]=="$"):
        characterstics = characterstics + 1
print("Vowels :", vowels);
print('Consonants: ', consonants)
print("characterstics: ",characterstics)