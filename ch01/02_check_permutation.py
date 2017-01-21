def check_perm(str1, str2):
    if len(str1) != len(str2): return False

    char_count_1 = {}
    for c in list(str1):
        char_count_1[c] = (char_count_1[c] + 1) if char_count_1.get(c) else 1

    for c2 in list(str2):
        if char_count_1.get(c2) != None:
            char_count_1[c2] -= 1
        else:
            return False

    return all(v == 0 for v in char_count_1.values())

print(check_perm("abcdefabc", "abcabcdef"))
