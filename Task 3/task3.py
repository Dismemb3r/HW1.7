import os

lst_files = ['1.txt', '2.txt', '3.txt']
dict_files = {}

for i in lst_files:
    file_p = os.path.join(os.getcwd(), i)
    with open(file_p, "r") as f:
        dict_files[i] = len(f.readlines())


def count_rows(txt):
    file_path = os.path.join(os.getcwd(), txt)
    with open(file_path, "r") as f_p:
        return str(len(f_p.readlines()))


sorted_key = sorted(dict_files, key=dict_files.get)


def merge_files(sorted_key):
    for j in sorted_key:
        file_path = os.path.join(os.getcwd(), j)
        with open(file_path, "r") as f_:
            with open(os.path.join(os.getcwd(), 'save.txt'), "a") as f_1:
                f_1.write(j + '\n')
                f_1.write(count_rows(j) + '\n')
                while True:
                    line = f_.readline()
                    f_1.write(line)
                    if not line:
                        f_1.write('\n')
                        break


merge_files(sorted_key)
