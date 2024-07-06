cringe_words = { "СКУФ": "игрок доты", "ЕЩКЕРЕ": "Рандомный набор букв", "КАПС": "сообщение написанное полонстью большими буквами"}
cringe = input("Напиши неопнятное слово слово КАПС-ом ")
if cringe in cringe_words:
    print(cringe_words[cringe])
else:
    print("Даже я такое не знаю")
