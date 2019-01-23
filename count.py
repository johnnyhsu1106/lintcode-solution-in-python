import os

def count_files():
    execute_fname = 'run_files.py'
    dirs = os.listdir(os.getcwd())
    py_files = [ py_file for py_file in dirs \
                if py_file[-3:]=='.py' \
                and py_file[0:3].isdigit()]

    print(len(py_files))


# def main():
#     count_files()
# 
#
# if __name__ == '__main__':
#     main()
