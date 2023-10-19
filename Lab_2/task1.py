#Напишите функцию для определения количества слов в строке и
#определения самого длинного слова
def analyze_str(string):
    if string is None:
        raise Exception("Input value is None")
    else:
        find_word = ""
        mass = string.split()
        length = 0
        for word in mass:
            if len(word) > length:
                length = len(word)
                find_word = word
        return find_word, len(mass)

user_str = input("Введите строку: ")
try:
    longest_word, count = analyze_str(user_str)
    print(f'Кол-во слов в строке: {count}')
    print(f'Самое длинное слово: {longest_word}')
except Exception as analyze_error:
    print(analyze_error)

