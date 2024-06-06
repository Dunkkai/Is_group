"""+ a b c d
a   c d a b
b   d a b c
c   a b c d
d   b c d a"""
#для 5-ти букв
"""H = ["a","b","c","d",'e']
T = [
    ["a", "b", "c", "d",'e'],
    ["b", "c", "d", "e",'a'],
    ['c', 'd', 'e', 'a','b'],
    ["d", "e", "a", "b",'c'],
    ["e", "a", "b", "c",'d'],

]"""
#для 4-х букв
H = ["a","b","c","d"]
T = [
    ["c", "a", "d", "b"],
    ["a", "b", "c", "d"],
    ["d", "c", "b", "a"],
    ["b", "d", "a", "c"],
]
#для 3-х букв

"""H = ["a","b","c"]
T = [
    ["c", "a", "b"],
    ["a", "b", "c"],
    ["b", "c", "a"],
]"""

"""
нужно сделать проверку на
1) замкнутость множества отн.себя +
2) ассоциативность операции +
3) существует нейтральный элемент +
4) сущ-ет обратный элемент +
) комутативность? +

"""
#работает
def commutative (table:list[list[str]]) -> bool:
    for az in range(len(table)):
        for buki in range(len(table[az])):
            if table[az][buki] != table[buki][az]:
                return False
    return True

#работает
def is_set_closed(header: list, table:list[list[str]]) -> bool:
    all_letters = set()
    for az in range(len(table)):
        for buki in range(len(table[az])):
            all_letters.add(table[az][buki])
    if all_letters.issubset(header):
        return True
    else:
        return False

# =)
def associative (header:list[str],table:list[list[str]], dec: int) -> bool:
    d = {}
    for cifra, bukva in enumerate(header):
        d[bukva] = cifra
    counter = 0
    for az in range(len(header)):
        for buki in range(len(header)):
            for vedi in range(len(header)):
                first_part_left = d[table[az][buki]]  # Это отвечает за a*a , a*b ,a*c, a*d (в скобках)
                second_part_left = vedi  # переменная будет меняться от a до d в каждом случае для первой части
                left = table[first_part_left][second_part_left]
                first_part_right = az  # отвечает за а, б, с, д т.к оно не в скобках
                second_part_right = d[table[buki][vedi]]  # отвечает за вторую часть(в скобках)
                right = table[first_part_right][second_part_right]
                counter += 1
                if left != right:
                    print(f"2)Что-то не так:")
                    print(
                        f"({header[az]}*{header[buki]})*{header[vedi]} = {left}; {header[az]}*({header[buki]}*{header[vedi]}) = {right}")
                    return False
                if dec == 1:
                    print(f"({header[az]}*{header[buki]})*{header[vedi]} = {left}; {header[az]}*({header[buki]}*{header[vedi]}) = {right}")
    print(f"2)Проверен(-о) {counter} вариант(-а/-ов), операция ассоциативна")
    return True

#ищем нейтральный элемент
def find_neutral_element(header: list[str], table:list[list[str]]) -> str:
    d = {}
    for cifra, bukva in enumerate(header):
        d[cifra] = bukva
    for az in range(len(table)):
        if table[az] == header:
            return d[az]
#работает
def find_inverse_element(header: list[str], table: list[list[str]],neutral_element: str) -> dict[str]:
    d = {}
    for cifra, bukva in enumerate(header):
        d[cifra] = bukva
    inv_elems_dict = {}
    for az in range(len(table)):
        for buki in range(len(table[i])):
            if table[az][buki] == neutral_element:
                inv_elems_dict[header[az]] = header[buki]
    return inv_elems_dict

print(f"Наши входные данные:\nМножество: {H}\nТаблица Кэли(первая строчка и столбец - шапка):")
print("+      ","\t".join(''"{:<7}".format(item) for item in H))
for i in range(len(T)):
    print("{:<6}".format(H[i]),end='\t')
    for j in range(len(T[i])):
        print(T[i][j],end= 7*' ')
    print()

print(f"Чтобы определить является ли наша алгебраическая структура группой нам нужно проверить"
      f"\n1) Замкнута ли группа относительно себя"
      f"\n2) Ассоциативна ли операция"
      f"\n3) Существует ли нейтральный элемент"
      f"\n4) Существует ли у каждого элемент обратный к нему\n")

fst = is_set_closed(H,T)
if (fst):
    print("1)Группа замкнута.\n")
ch = int(input(f"чтобы узнать является ли операция ассоциативной нужно проверить {len(H)**3} варианта(-ов), вы хотите увидеть весь перебор?"
           f"\n0)Нет 1)Да\n"))
sec = associative(H,T,ch)

n_el = find_neutral_element(H,T)
if n_el:
    print(f"\n3)Нейтральный элемент: {n_el}")
else:
    print(f"3)Нейтрального элемента нет")

flag4 = 0
if n_el:
    flag4 = 1
    inv_el_dict = (find_inverse_element(H,T,n_el))
    print("\n4)Список обратных элементов:")
    for key,value in inv_el_dict.items():
        print(f"для {key} - {value}")
else:
    print(f"Т.к. нет нейтралього элемента, то и обратных элементов мы найти не сможем")

if fst and sec and n_el and flag4:
    print(f"\nт.к. наша алгебраическая структура - группа, то мы можем проверить является ли она Абелевой")
    if (commutative(T)):
        print(f"Операция коммутативна, является")