#Mostre o aumento de um salário dependendo do seu cargo
#Junior: 10%
#Pleno: 20% 
#Sênior: 30% 
# Valores: 
#Junior: 2000
#Pleno: 5000
#Sênior:10000
print('Descubra quanto será seu aumento de salário')
nivel = str(input("Qual o seu nivel? "))
junior = 2000
pleno = 5000
senior = 10000


if nivel == 'junior': 
    aumento = junior + (junior * 10/100)
    print(aumento)
if nivel == 'pleno':
    aumento = pleno + (pleno * 20/100)
    print(aumento)
if nivel == 'senior':
    aumento = senior + (senior * 30/100)
    print(aumento)