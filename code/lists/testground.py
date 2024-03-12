def perm(list1, list2):
    if len(list1) != len(list2):
        return False

    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    else:
        return False


print(perm([1, 2, 3], [3, 2, 1, ]))
print(perm([1, 5, 1, 6], [6, 1, 5, 1]))
print(perm([1, 2, 3], [1, 2, 1]))


def permString(list1, list2):
    if len(list1) != len(list2):
        return False

    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    else:
        return False


print(permString(["c", "a", "t"], ["a", "c", "t"]))
print(permString(["c", "a", "t"], ["a", "c", "t", "s"]))
print(permString(["hello"], ["olleh"]))
