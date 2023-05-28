import csv
import time
aaaa = time.monotonic()
a = dict()
with open('student_counts.csv', 'r' ,encoding="utf-8") as file_in, \
    open('sorted_student_counts.csv', 'w' ,encoding="utf-8", newline='') as file_onn:
    rows = list(csv.reader(file_in, delimiter=","))        
    [a.setdefault(rows[0][y],[]).append(rows[1:][i][y]) for i in range(len(rows[1:])) for y in range(len(rows[1:][i]))]
    b = sorted([sorted(a, key=lambda x: x)][0][:-1], key=lambda y: (len(y), int(y[:1]) if len(y) < 2 else int(y[0])))
    c = [sorted(a, key=lambda x: x)][0][-1]
    b.insert(0, c)
    d = [[a[i][y] for i in b] for y in range(len(rows[1:]))]
  
    writer = csv.writer(file_onn)
    writer.writerow(b)
    writer.writerows(d)

# def key_func(grade):
#     number, letter = grade.split('-')
#     return int(number), letter

# with open('student_counts.csv', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     columns = ['year'] + sorted(reader.fieldnames[1:], key=key_func)
#     rows = list(reader)

# with open('sorted_student_counts.csv', 'w', encoding='utf-8') as file:
#     writer = csv.DictWriter(file, fieldnames=columns)
#     writer.writeheader()
#     writer.writerows(rows)
    
bbbb = time.monotonic()
print(bbbb-aaaa)