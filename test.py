import os
import sys

# def file_list(filename, py_files):
#     file = open(filename, 'w')
#     output = ''
#     for py_file in py_files:
#         output += py_file[:-3] + '\n'
#     file.write(output)
#     file.close()


def run_all_files():
    execute_fname = 'run_files.py'
    dirs = os.listdir(os.getcwd())
    py_files = [py_file for py_file in dirs if py_file.find('_') > -1 and py_file[-3:]=='.py' and py_file != execute_fname]
    count = 0

    # file_list('lintcode_problem_list.txt', py_files)

    for py_file in sorted(py_files):
        print(py_file)
        count += 1
        os.system( "python " + py_file)

    print('All ' + str(count)  + ' files can be executed successfully.')

def main():
    run_all_files()


if __name__ == '__main__':
    main()
