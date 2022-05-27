import math
#1
def are_files_equal(file1, file2):
    one = open(file1, 'r')
    two = open(file2, 'r')
    if(one.read()==two.read()):
        return true
    return False

#2
def sort(file):
    f = open(file, 'r').read()
    print(sorted(set(f)))

    for line in open(file, 'r').readlines():
      line = line.strip()
      age = line[0:3] #This will get the first 3 characters of the line
      age = int(age)

  thisLine = {"age":age, "line":line}
  result.append(thisLine)

sortedList = sorted(result, key=lambda k: k["age"]) 

def rev(file):
   with open(file, 'r') as f:
       for row in f:
           print row[::-1]

def last(file):
    n = input(print('Enter number'))
    a_file = open(file, "r")
    lines = a_file. readlines()
    last_lines = lines[-n:]
    print(last_lines)
    a_file.close() 

#3
def copy_file_content(source, destination):
    src = open(source,'r')
    s = src.read()
    src.close()
    dest = open(destination,'w')
    dest = s
    dest.close()

#4
def who_is_missing(file):
    nums = ''
    with open(file) as f:
        lines = f.readLines()
        x = [t.strip(' ') for t in lines]
        for i in range(1,10):
            if str(i) not in x:
                print(x)
                missing_num = open('missingNum.txt','w')
                missing_num = x

def main():
    open('H:\Python\ex1.txt', 'w')
    open('H:\Python\ex2.txt', 'w')

    print(are_files_equal('H:\Python\ex1.txt', 'H:\Python\ex2.txt'))
    copy_file_content('H:\Python\ex1.txt', 'H:\Python\ex2.txt')
    who_is_missing('H:\Python\ex1.txt')
    route = input(print('Enter file route'))
    action = input(print('Enter desired action'))
    match action:
        case 'sort':
            sort(route)
        case 'rev':
            rev(route)
        case last:
            last(route)



if __name__ == "__main__":
    main();
    
           
           
           
    
    
    
