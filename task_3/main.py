# Class that stores information about the file
class FileInfo:
    files = dict()

    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.count_line = len(text)
        self.files[len(text)] = self


# Function that writes information to a file in the correct order
def write_file(result, file):
    result.write(f"{file.name}\n{file.count_line}\n{"".join(file.text)}\n")


# Creating objects of class FileInfo
file_1 = FileInfo("text_1.txt", open("text_1.txt", encoding='utf-8').readlines())
file_2 = FileInfo("text_2.txt", open("text_2.txt", encoding='utf-8').readlines())
file_3 = FileInfo("text_3.txt", open("text_3.txt", encoding='utf-8').readlines())

# Sorting by the number of lines in the file
files_sort = dict(sorted(FileInfo.files.items()))

# Creating an output file
file_result = open("result.txt", 'a', encoding='utf-8')

# Sequential writing of text to a file
for item in files_sort.values():
    write_file(file_result, item)
