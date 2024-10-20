# TODO Найдите количество книг, которое можно разместить на дискете

disketa_size_in_bytes = 1.44 * 1024 * 1024
total_characters_in_one_book = 25 * 50 * 100
memory_for_one_book = total_characters_in_one_book * 4
answer = disketa_size_in_bytes // memory_for_one_book

print("Количество книг, помещающихся на дискету:", int(answer))

