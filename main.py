
button_times = {
    "a": 0.25,
    "b": 0.5,
    "c": 0.75,
    "d": 0.25,
    "e": 0.5,
    "f": 0.75,
    "g": 0.25,
    "h": 0.5,
    "i": 0.75,
    "j": 0.25,
    "k": 0.5,
    "l": 0.75,
    "m": 0.25,
    "n": 0.5,
    "o": 0.75,
    "p": 0.25,
    "q": 0.5,
    "r": 0.75,
    "s": 1,
    "t": 0.25,
    "u": 0.5,
    "v": 0.75,
    "w": 0.25,
    "x": 0.5,
    "y": 0.75,
    "z": 1,
    "*": 0.25,
    "#": 0.25
}
char_key_map = {
    "a": "2",
    "b": "2",
    "c": "2",
    "d": "3",
    "e": "3",
    "f": "3",
    "g": "4",
    "h": "4",
    "i": "4",
    "j": "5",
    "k": "5",
    "l": "5",
    "m": "6",
    "n": "6",
    "o": "6",
    "p": "7",
    "q": "7",
    "r": "7",
    "s": "7",
    "t": "8",
    "u": "8",
    "v": "8",
    "w": "9",
    "x": "9",
    "y": "9",
    "z": "9",
    "*": "*",
    "#": "#"
}
cap_time = 2

files_in = ["Test1.txt",
            "Test2.txt",
            "Test3.txt",
            "Test4.txt"]


def time_words(infile):
    times = []
    with open(infile, 'r') as f:
        words_lines = f.readlines()
        words_lines = [word.strip() for word in words_lines]
    for word in words_lines:
        time_to_type = -0.25
        last_char = None
        for ch in word:
            if 97 <= ord(ch) <= 122 or ord(ch) == 35 or ord(ch) == 42:
                time_to_type += button_times[ch]
            else:
                ch = ch.lower()
                time_to_type += cap_time
                time_to_type += button_times[ch]
            if last_char is not None:
                if char_key_map[last_char] == char_key_map[ch]:
                    time_to_type += 0.25
            last_char = ch
        times.append([time_to_type, word])
    return times


for f in files_in:
    print(f)
    type_times = time_words(f)
    min_time = 1000
    min_time_ind = []
    for i in range(len(type_times)):
        if type_times[i][0] < min_time:
            min_time_ind = [i]
            min_time = type_times[i][0]
        elif type_times[i][0] == min_time:
            min_time_ind.append(i)
    for index in min_time_ind:
        print(type_times[index][1], type_times[index][0])
    print()



