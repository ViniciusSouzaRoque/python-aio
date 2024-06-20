def search_index(haystack: str, needle: str):
    if needle not in haystack:
        return -1
    else:
        return haystack.find(needle)

haystack = 'leetcode'
needle = 'eet'
print(search_index(haystack=haystack, needle=needle))

