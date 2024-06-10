my_dist = {'Ирина':2001, 'Влад':2005, 'Кристина':1995, 'Тмофей':2006}
print(my_dist)
print('Год рождения Влада: ', my_dist['Влад'])
print('Год рождения Олеси: ', my_dist.get('Олеся', 'не известен'))
my_dist.update({'Илья':2000, 'Слава':2008})
print('Удаляю из списка Кристину', my_dist.pop('Кристина'), 'года рождения')
print(my_dist)
my_set = {10, 3.14, 'August', 400, 3.14, 'March', 'August'}
print(my_set)
my_set.add('April')
my_set.add(9.8)
my_set.discard(3.14)
print(my_set)




