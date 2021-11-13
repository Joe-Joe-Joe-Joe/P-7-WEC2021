from main import read_words_2

part_2 = ["Part2.txt"]

for f in part_2:
    print(f)
    type_times = read_words_2(f)
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