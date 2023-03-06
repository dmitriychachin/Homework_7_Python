"""
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке
"""
verse = input()

def rhythm_count(verse):
    list_count = []
    rhythm:bool
    word = ""
    for i in range(len(verse)):
        if (verse[i] != " " and i < len(verse) - 1):
            word = word + verse[i]
        else:
            count = verbs_in_word(word)
            list_count.append(count)
            word = ""
        
    rhythm = all(x == list_count[0] for x in list_count)
    return rhythm

def verbs_in_word(word):
    count = 0
    word = word.upper()
    for char in word:
        if char in list:
            count = count + 1
    
    return count

list = {"А","О","Э","Е","И","Ы","У","Ё","Ю","Я"}

if rhythm_count(verse) == True:
    print("Парам пам-пам")
else:
    print("Пам парам")
