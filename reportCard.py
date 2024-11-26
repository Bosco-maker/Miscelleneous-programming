from os import strerror

class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    print("cannot read lines in file")

class FileEmpty(StudentsDataException):
    print("file empty")

file_name = input('Input file name: ')

info = []
try:
    for line in open(file_name, "rt"):
        line = line.split()
        info.append({'first name' : line[0],
                     'last name' : line[1],
                     'mark' : line[2]})
    
    sorted_info = []
    for line in info:
        first_name = line['first name']
        last_name = line['last name'] 

        for sorted_line in sorted_info:
            if first_name == sorted_info [sorted_line]['first name'] and last_name == sorted_info [sorted_line]['last_name']:
                sorted_info [line]['mark'] += info[line]['mark']
                break
        sorted_info.append({'first name' : first_name,
                            'last name' : last_name,
                            'mark' : line['mark']})
        
    print(sorted_info)
        

except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

