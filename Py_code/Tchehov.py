for ch in 'Чехов':
    print(ch)
    
st= 'олдос Хаксли родился в 1894 году'
st=st[0].upper()+st[1:]
print(st)
st1 = 'Где это? Кто это? Когда это?'.replace('? ','?? ').split('? ')
print(st1)
st2=' '.join(["Рыжая", "лиса", "перепрыгнуля", "через",
"низкий", "забор", "."])
st2=st2.replace(' .','.')
print(st2)
print('Хемингуэй'.index('н'))
st3='И не зачем так орать! Я и в первый раз прекрасно слыщал.'
st3 = st3[:st3.index('!')]
print(st3)
n1 = input('Напишите существительное: ')
n2 = input('Напишите еще одно: ')
print('Вчера я написал {}. Вчера я ходил в {}!'.format(n1,n2))
