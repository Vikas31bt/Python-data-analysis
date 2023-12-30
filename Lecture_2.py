Name = 'Human Genome Project (HGP)'
Start_HGP = 1990
End_HGP = 2003
Field = 'Genomics'
print(Name, 'began in', Start_HGP, 'and was completed in', End_HGP, Field)
print(Name + '\n' + 'started in ' +str(Start_HGP) + ' and was completed in ' + str(End_HGP) + '\n' + Field)

print(type(Start_HGP))
Start_HGP = str(Start_HGP)
print(type(Start_HGP))
End_HGP = int(input('Human Genome Project was completed in which year: '))
print(type(End_HGP))

g = '9.8'
print(g, type(g))
g = float(g)
print(g, type(g))

num = 5
num = float(num)
print(num, type(num))

number = '100'
number = int(number)
print(number, type(number))

print(2)
print(7)
print(2+7)

num1 = 5
num2 = 10
print(num1*num2)

result1 = 2+7*3-3
print(result1)

result2 = 3+10*2%2
print(result2)
