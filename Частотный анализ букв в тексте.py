# TODO  Напишите функцию count_letters
def count_letters(text):
    result_dict = {}
    for i in text:
        if not i.isalpha():
            continue
        i = i.lower()
        if result_dict.get(i) == None:
            result_dict[i] = 1
        else:
            result_dict[i] += 1
    return result_dict

# TODO Напишите функцию calculate_frequency

def calculate_frequency(my_dict):
    all_frequency = 0
    dict1 = {}
    for i in my_dict.values():
        all_frequency += i
    for i in my_dict.items():
        frequency = i[1] / all_frequency
        # i[1] /= all_frequency
        dict1[i[0]] = frequency
    return dict1

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

for i in calculate_frequency(count_letters(main_str)):
    print(f"{i}: {calculate_frequency(count_letters(main_str))[i]:.2f}")
