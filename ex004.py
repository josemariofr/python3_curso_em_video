a = input('Digite alguma coisa: ')  
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços? ', a.isspace()) 
print('Só tem números? ', a.isnumeric())
print('É alfabético? ', a.isalpha()) 
print('É alfanumérico? ', a.isalnum())
print('É maiúcula? ', a.isupper())                 
print('É minúscula? ', a.islower())