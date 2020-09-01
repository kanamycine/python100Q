def kotoen(pln):

    enp = ['Mercury', 'Venus', 'Earth', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune']

    if pln == '수성':
        print(enp[0])
    elif pln == '금성':
        print(enp[1])
    elif pln == '지구':
        print(enp[2])
    elif pln == '화성':
        print(enp[3])
    elif pln == '목성':
        print(enp[4])
    elif pln == '토성':
        print(enp[5])
    elif pln == '천왕성':
        print(enp[6])
    elif pln == '해왕성':
        print(enp[7])


kotoen('수성')


# 모범풀이
planets = {
    '수성': 'Mercury',
}

name = input()
print(planets[name])
