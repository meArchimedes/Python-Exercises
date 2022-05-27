import math;
#1
def shift_left(list):
    first = list[0];
    list.remove(first);
    list.append(first);
    print(list);
    return list
#2
def format_list(list):
    last = list[-1];
    list.remove(last);
    fList = ', '.join(list);
    print(fList,"and ", last);
#3
def extend_list(list_a,list_b):
    for x in list_b:
        list_a.append(x);
    print(list_a);
#4
def lists_equal(list_a, list_b):
    if(list_a==list_b):
        return true;
    return False;
#5
def longest(list):
    list.sort.__sizeof__;
    print(list[1]);
#6
def func(num1, num2):
    return math.cos(num1+num2);

def main():
    list = ["Ferari","Audi","Rolls Royce"];
    l1 = [1,2,3];
    l2 = [3,4,5];
    shift_left(list);
    format_list(list);
    extend_list(l1,l2);
    print(lists_equal(l1,l2));
    longest(list);
    help(func);
    print(func(89.765,54));
    

if __name__ == "__main__":
    main();
