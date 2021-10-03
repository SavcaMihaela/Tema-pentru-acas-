X=[[2,4,6,8,10],
   [1,3,5,7,9],
   [1,2,3,4,5],
   [6,7,8,9,1],
   [3,4,5,1,2]]
print('Suma primului rand', sum(X[0]))
print('Suma randului doi', sum([1]))
print('Suma randului trei', sum([2]))
print('Suma randului patru', sum([3]))
print('Suma randului cinci', sum([4]))
coloana1=0
coloana2=0
coloana3=0
coloana4=0
coloana5=0
for i in X:
    coloana1+=i[0]
    coloana2+=i[1]
    coloana3+=i[2]
    coloana4+=i[3]
    coloana5+=i[4]
print('Suma primei coloane', coloana1)
print('Suma a doua coloana', coloana2)
print('Suma a treia coloana', coloana3)
print ('Suma a patra coloana', coloana4)
print('Suma a cincea coloana', coloana5)
a=X[0][0]+X[1][1]+X[2][2]+X[3][3]+X[4][4]
b=X[0][4]+X[1][3]+X[2][2]+X[3][1]+X[4][0]
print('Suma diagonalei principale',a, 'Suma diagonalei secundare',b)
