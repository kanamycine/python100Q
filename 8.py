#딕셔너리를 만들 때 키 이름이 중복되면 어떻게 될까요? (파이썬 3.6 기준)

lux = {'health': 490, 'health': 800, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux['health'])    # 키가 중복되면 가장 뒤에 있는 값만 사용함
print(lux)    # 중복되는 키는 저장되지 않음
