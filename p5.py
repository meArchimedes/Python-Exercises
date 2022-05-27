import math;

def squared_numbers(start, stop):
    list;
    i=start;
    j=0;
    while i<stop+1:
        list[j] = math.pow(i,2);
        i+=1
        j+=1
    return list;

def main():
    print(squared_numbers(2,5));
    
if __name__ == "__main__":
    main();
