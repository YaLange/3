import os

def get_txt_files(directory):
    txt_files = []
    files = os.listdir(directory)
    for file in files:
        if file.endswith(".txt"):
            txt_files.append(file)
    return txt_files

def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines), ''.join(lines)

def merge_files(directory, result_file):
    file_data = {}
    txt_files = get_txt_files(directory)

    for file in txt_files:
        path = os.path.join(directory, file)
        lines, text = read_file(path)
        file_data[file] = (lines, text)
    
    sorted_files = sorted(file_data.items(), key=lambda x: x[1][0])

    with open(result_file, 'w') as result:
        for file, (lines, text) in sorted_files:
            result.write(file + '\n')
            result.write(str(lines) + '\n')
            result.write(text + '\n')

directory = '.'  # Укажите путь к папке, содержащей файлы
result_file = '3.txt'

merge_files(directory, result_file)