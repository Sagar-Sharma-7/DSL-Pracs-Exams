def intersection(list1, list2):
    result = list()
    temp_list2 = list2[:]
    for e in list1:
        if e in temp_list2:
            result.append(e)
            temp_list2.remove(e)
    return result

def union(list1, list2):
    result = list1[:]
    for e in list2:
        if(e not in result):
            result.append(e)
    return result

def difference(list1, list2):
    result = []
    temp_list2 = list2[:]
    for e in list1:
        if e in temp_list2:
            temp_list2.remove(e)
        else:
            result.append(e)
    return result

def cricket_and_badminton(group_a, group_b):
    return(group_a, group_b)

def cricket_or_badminton(group_a, group_b):
    only_cricket = difference(group_a, group_b)
    only_badminton = difference(group_a, group_b)
    return union(only_cricket, only_badminton)

def neither_cricket_nor_badminton(all_student, group_a, group_b):
    cricket_or_badminton = union(group_a, group_b)
    return difference(all_student, cricket_or_badminton)

def cricket_and_football_not_badminton(group_a, group_b, group_c):
    cricket_and_football = intersection(group_a, group_c)
    return difference(cricket_and_football, group_b)

def no_game(all_student, group_a, group_b, group_c):
    at_least_one_game = union(group_a, union(group_b, group_c))
    return difference(all_student, at_least_one_game)

def at_least_one_game(group_a, group_b, group_c):
    return union(group_a, union(group_b, group_c))

def all_three_games(group_a, group_b, group_c):
    return intersection(group_a, intersection(group_b, group_c))

def main():
    all_students = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack"]
    group_a = ["Alice", "Bob", "Charlie", "Eve", "Bob"]  # Cricket (with duplicates)
    group_b = ["Bob", "David", "Eve", "Grace", "Bob"]    # Badminton (with duplicates)
    group_c = ["Alice", "Eve", "Frank", "Hank", "Eve"]   # Football (with duplicates)

    print("a) Students who play both cricket and badminton:", cricket_and_badminton(group_a, group_b))
    print("b) Students who play either cricket or badminton but not both:", cricket_or_badminton(group_a, group_b))
    print("c) Students who play neither cricket nor badminton:", neither_cricket_nor_badminton(all_students, group_a, group_b))
    print("d) Students who play cricket and football but not badminton:", cricket_and_football_not_badminton(group_a, group_b, group_c))
    print("e) Students who do not play any game:", no_game(all_students, group_a, group_b, group_c))
    print("f) Students who play at least one game:", at_least_one_game(group_a, group_b, group_c))
    print("g) Students who play all three games:", all_three_games(group_a, group_b, group_c))

main()