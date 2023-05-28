import csv
def csv_columns(file_name):
    a = {}
    with open(file_name, "r", encoding="utf-8") as file:
        rows = csv.reader(file, delimiter=",")
        b = list(next(rows))             
        
        for i in  rows:
            for j in range(len(b)): 
                a.setdefault(b[j],[]).append(i[j])
        return a
print(csv_columns('deniro.csv'))

# import csv

# def csv_columns(filename):

#     with open(filename, encoding="utf-8") as file_in:
#         rows = list(csv.reader(file_in))
#         return {key: value for key, *value in zip(*rows)}