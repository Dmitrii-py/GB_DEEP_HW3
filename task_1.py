# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# Пример:
# [1, 2, 3, 1, 2, 4, 5, 7 ,7] -> [1, 2]

input_list = [1, 2, 3, 1, 2, 4, 5, 7, 7]
repeat_list = []
NOT_REPEAT = 1
for num in input_list:
    if num not in repeat_list and input_list.count(num) > NOT_REPEAT:
        repeat_list.append(num)
print(repeat_list)
