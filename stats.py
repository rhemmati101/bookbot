def wordcount(text: str) -> int:
    return len(text.split())

def charcount(text: str) -> dict[str : int]:
    char_counts: dict[str : int] = {}
    
    for char in text:
        char = char.lower()

        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1

    return char_counts

def listify_counts(counts: dict[str : int]) -> list:
    listified_counts = []

    for key in counts:
        listified_counts.append({
            "name": key,
            "count": counts[key]
            })
    
    #now, sort from greatest to smallest count
    listified_counts.sort(reverse=True, key=lambda item: item["count"])

    return listified_counts