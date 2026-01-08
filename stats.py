def get_word_count(file_text):
    words = file_text.split()
    words = len(words)
    print (f"Found {words} total words")


def get_character_count(file_text):
    characters = file_text.lower()
    count = {}
    for char in characters:
        if char.isalpha():
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    for char, num in sorted(count.items()):
        count[char] = num
    return count

def sorted_report(count_dict):
    report = []
    for char, num in sorted(count_dict.items(), key=lambda item: item[1], reverse=True):
        report.append(f"{char}: {num}")
    for i in len(report):
        print(report,sep="\n")