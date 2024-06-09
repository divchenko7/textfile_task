import random
#читаємо весь файл з текстом та робимо нижній регістр, щоб всі слова зчитувались однаково
with open('/Users/dianaivchenko/Documents/GitHub/textfile_task1/book.txt', 'r') as text_file:
    text = text_file.read().lower()

#Проходячи через кожен символ тексту, розділові знаки замінюються пробілом,
# а інші символи залишаються без змін.

punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
cleaned_text = ""
for el in text:
    if el not in punctuation:
        cleaned_text += el
    else:
        cleaned_text += " "
#очищений текст розбиваємо на слова
list_of_words = cleaned_text.split()


#словник, де кожне слово з тексту є ключем, а значенням є список слів,
# які йдуть за цим словом у тексті
new_dict = {}
for i in range(len(list_of_words) - 1):
    key = list_of_words[i]
    value = list_of_words[i + 1]
    if key in new_dict:
        new_dict[key].append(value)
    else:
        new_dict[key] = [value]

current_word = random.choice(list(new_dict.keys()))
sequence = [current_word] #в цьому листі вже буде міститись нова послідовність слів
# згенерована випадковм чином

sequence_length = 200

#Згенерована послідовність слів об'єднується в один рядок з пробілами між словами
# та виводиться на екран.

for s in range(sequence_length + 1):
    if current_word in new_dict:
        value = random.choice(new_dict[current_word])
        sequence.append(value)
        current_word = value

print(' '.join(sequence))
