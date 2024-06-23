def single_root_words(root_word, *other_words):
    same_words = []  # Создаем пустой список для пополнения
    for i in other_words: # цикл будет перебирать подходящие слова
        if root_word.lower() in i.lower() or root_word.upper() in i.upper(): # условие поиска
            same_words.append(i)
        if i.lower() in root_word.lower() or i.upper() in root_word.upper(): # второе условие поиска
            same_words.append(i) # пополняем созданный список
    return same_words # возвращаем наш созданный список


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)


