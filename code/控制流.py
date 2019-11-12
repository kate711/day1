x = 5
if x > 4 or x != 9:
    print('{}'.format(x))
else:
    pass

if x > 6:
    print('x is not greater than 6')
elif x > 4 and x == 5:
    print('{}'.format(x * x))
else:
    print('x is not greater than 4')

y = ['Jan', 'Feb', 'Mar', 'Jun', 'Jul', 'Aug', 'Seq']
z = ['Annie', 'Betty', 'Claire', 'Dapne', 'Ellie', 'Franchesca', 'Greta']

for month in y:
    print('{!s}'.format(month))

for i in range(len(z)):
    print('{0!s}: {1:s}'.format(i, z[i]))

for j in range(len(z)):
    if y[i].startswith('J'):
        print('{!s}'.format(y[i]))
