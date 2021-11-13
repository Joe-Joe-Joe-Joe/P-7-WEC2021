from main import read_words_1

part_1 = ["Test1.txt",
          "Test2.txt",
          "Test3.txt",
          "Test4.txt"]

for f in part_1:
    print(f)
    type_times = read_words_1(f)
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



