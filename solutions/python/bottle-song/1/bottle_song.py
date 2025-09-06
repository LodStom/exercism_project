def recite(start, take=1):
    num_dict = {
        10: "Ten", 9: "Nine", 8: "Eight", 7: "Seven", 6: "Six",
        5: "Five", 4: "Four", 3: "Three", 2: "Two", 1: "One"
    }
    verses = []
    verse_3 = "And if one green bottle should accidentally fall,"

    for _ in range(take):
        if start == 1:
            verses.append(f"{num_dict[start]} green bottle hanging on the wall,")
            verses.append(f"{num_dict[start]} green bottle hanging on the wall,")
            verses.append(verse_3)
            verses.append("There'll be no green bottles hanging on the wall.")
        elif start == 2:
            verses.append(f"{num_dict[start]} green bottles hanging on the wall,")
            verses.append(f"{num_dict[start]} green bottles hanging on the wall,")
            verses.append(verse_3)
            verses.append("There'll be one green bottle hanging on the wall.")
        else:
            verses.append(f"{num_dict[start]} green bottles hanging on the wall,")
            verses.append(f"{num_dict[start]} green bottles hanging on the wall,")
            verses.append(verse_3)
            verses.append(f"There'll be {num_dict[start - 1].lower()} green bottles hanging on the wall.")

        start -= 1
        if _ < take - 1:  # blank line between verses
            verses.append("")

    return verses
