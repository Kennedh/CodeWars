def filter_list(l):
    filterr = []
    for item in l:
        if isinstance(item, int):
            filterr.append(item)
    return filterr

# Teste

print(filter_list([1, 2, "a", "b"]))