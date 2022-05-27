import math;
#1
def squared_numbers(start, stop):
    list = [math.pow(start,2)];
    i=start+1;
    while i<stop+1:
        list.append(math.pow(i,2))
        i+=1
    return list;

#2
def fibonacci():
    i=1;
    fnc=0;
    while fnc<23333:
        fnc=0;
        for num in range(1,i):
            fnc+=fnc+num;
        print(fnc);
        i+=1

#3
def is_greater(list, n):
    for num in list:
        if n > num:
            list.remove(num);
    return list;
def main():
    print(squared_numbers(2,5));
    fibonacci();
    l= [3,5,65,45,2,4];
    print(is_greater(l,19));
    
if __name__ == "__main__":
    main();
