"""
Há uma matriz de strings. Todas as strings contêm letras semelhantes, exceto uma. Tente encontrá-la!

Strings podem conter espaços. Espaços não são significativos, apenas símbolos sem espaços são importantes.
Por exemplo, string que contém apenas espaços é como string vazia.

É garantido que a matriz contém mais de 2 strings.
"""

from collections import Counter

def find_uniq(arr):
    def normalize(s):
        return "".join(sorted(set(s.replace(" ", "").lower())))

    normalized_counts = Counter(normalize(s) for s in arr)

    unique_pattern = min(normalized_counts, key=normalized_counts.get)

    return next(s for s in arr if normalize(s) == unique_pattern)

