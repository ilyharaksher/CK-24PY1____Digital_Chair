# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, separator=','):
    all_participants = []
    common_members = []
    member = ''
    for i in group1:
        if i == separator:
            all_participants.append(member)
            member = ''
        else:
            member += i
    all_participants.append(member)
    member = ''
    for i in group2:
        if i == separator:
            all_participants.append(member)
            member = ''
        else:
            member += i
    all_participants.append(member)

    for i in all_participants:
        if all_participants.count(i) > 1 and common_members.count(i) < 1:
            common_members.append(i)

    return common_members
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, separator=','))
