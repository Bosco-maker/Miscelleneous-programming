from os import strerror

class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    def __init__(self, message):
        super().__init__(self, message)
        
    

class FileEmpty(StudentsDataException):
        def __init__(self, message):
            super().__init__(self, message)

file_name = input('Input file name: ')

info = []
try:
    for line in open(file_name, "rt"):
        line = line.split()
        info.append({'first name' : line[0],
                     'last name' : line[1],
                     'mark' : float(line[2])})
    
    sorted_info = []
    for line in info:
        first_name = line['first name']
        last_name = line['last name'] 

        for sorted_line in sorted_info:
            if first_name == sorted_line['first name'] and last_name == sorted_line['last name']:
                sorted_line['mark'] += line['mark']
                break
        else:
            sorted_info.append({'first name' : first_name,
                            'last name' : last_name,
                            'mark' : line['mark']})
        
    for sorted_line in sorted_info:
        print('{0}  {1}  {2}'.format(sorted_line['first name'] , sorted_line['last name'] , str(sorted_line['mark']) ) )
        

except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
except BadLine as e:
    print('badline')
except FileEmpty as e:
    print('file empty')

