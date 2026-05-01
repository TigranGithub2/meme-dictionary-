meme_dict = {
            "кринж": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное"
            }

word = input("введите непонятное слово: ").lower()

if word in meme_dict.keys():
    print("значение слова:", meme_dict[word])
else:
    print('такого слово нет')
