def count_lines(file_name):
    with open(file_name, 'r') as file:
        return sum(1 for line in file)

def merge_files(file1, file2, result_file):
    def write_file_info(file, lines):
        with open(result_file, 'a') as result:
            result.write(file + '\n')
            result.write(str(lines) + '\n')

    file1_lines = count_lines(file1)
    file2_lines = count_lines(file2)

    if file1_lines < file2_lines:
        write_file_info(file1, file1_lines)
        with open(file1, 'r') as f1, open(result_file, 'a') as result:
            result.write(f1.read() + '\n')
        write_file_info(file2, file2_lines)
        with open(file2, 'r') as f2, open(result_file, 'a') as result:
            result.write(f2.read())
    else:
        write_file_info(file2, file2_lines)
        with open(file2, 'r') as f2, open(result_file, 'a') as result:
            result.write(f2.read() + '\n')
        write_file_info(file1, file1_lines)
        with open(file1, 'r') as f1, open(result_file, 'a') as result:
            result.write(f1.read())

file1 = '1.txt'
file2 = '2.txt'
result_file = '3.txt'

merge_files(file1, file2, result_file)