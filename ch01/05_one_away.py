def one_away(str1, str2):
    longer = len(str2) - len(str1)
    if abs(longer) > 1: return False

    long_str, short_str = (str1, str2) if longer == -1 else (str2, str1)
    i, j, diff_count = 0, 0, 0

    while (i < len(long_str)):

        if j >= len(str2) or str1[i] != str2[j]:
            diff_count += 1
            if diff_count > 1: return False

            if longer == 0:
                i += 1
                j += 1
            elif longer == -1:
                i += 1
            else:
                j += 1
        else:
            i += 1
            j += 1

    return (diff_count == 1)

print(one_away("pales", "pale"))
print(one_away("bales", "pales"))
print(one_away("bale", "pales"))
