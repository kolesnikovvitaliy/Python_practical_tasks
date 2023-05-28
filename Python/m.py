from zipfile import ZipFile
with ZipFile('workbook.zip') as zip_file:
    a = {}
    info = zip_file.infolist()
    for i in info:
        if i.file_size > i.compress_size:
            a.setdefault(((i.compress_size / i.file_size) * 100),i.filename)          
    print(a[min(a)].split('/')[1])


    # a = sum([i.file_size for i in info])
    # b = sum([i.compress_size for i in info])
    # print(f'Объем исходных файлов: {a} байт(а)',f'Объем сжатых файлов: {b} байт(а)',sep="\n")
    # for i in info:
    #     print(i.file_size)
#     file_size
# compress_size
# Объем исходных файлов: 7810260 байт(а)
# Объем сжатых файлов: 7798267 байт(а)







#     info = zip_file.infolist()
# print(len(info) - sum([1 for i in info if i.is_dir()]))