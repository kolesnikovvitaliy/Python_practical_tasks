import csv
import time
aaaa = time.monotonic()
def condense_csv(filename, id_name):
    import csv
    a = dict()
    with open(filename, 'r' ,encoding="utf-8") as file_in, \
        open('condensed.csv', 'w' ,encoding="utf-8", newline='') as file_onn:
        rows = list(csv.reader(file_in, delimiter=","))    
        [a.setdefault(i[0], []).append([i[1], i[2]]) for i in rows]
        b = [rows[i][1] for i in range(len(a[rows[0][0]]))]
        b.insert(0, id_name)
        c = sorted(list(map(lambda x: [x, *map(lambda y: y[1], a[x])], a)))
        writer = csv.writer(file_onn)
        writer.writerow(b)
        writer.writerows(c)


condense_csv('data_test.csv', id_name='ID')







# condensed.csv
#condense_csv('data.csv', id_name='ID')

# ball,color,purple
# ball,size,4
# ball,notes,it's round
# cup,color,blue
# cup,size,1
# cup,notes,none

# object,color,size,notes
# ball,purple,4,it's round
# cup,blue,1,none
#GROUP BY 1

bbbb = time.monotonic()
print(bbbb-aaaa)