total_time = 300 * 60
number_of_problems = None
times = None
with open('win.in') as f:
    number_of_problems = int(f.readline().strip())
    times = sorted(map(int, f.readline().strip().split(' ')))
    print(number_of_problems, times)

time = 0
result = number_of_problems
for i in range(0, number_of_problems):
    time = time + times[i]
    if time > total_time:
        result = i
        break
print(result)
with open('win.out', 'w') as f:
    f.write(str(result))

            


