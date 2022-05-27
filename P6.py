#1
def sort_prices(list_of_tuples):
    list_of_tuples
    print sorted(list_of_tuples, key = MyFn, reverse = True);

def MyFn(s):
    return s[1];
#2
def mult_tuple(tuple1,tuple2):
    tups = [tuple1, tuple2];
    return[(i,j) for x in tups for y in tups for i in x for j in y if x is not y];
#3
def sort_anagrams(list_of_strings):
    from itertools import groupby
    f = lambda w: sorted(w)
    print [list(v) for k,v in groupby(sorted(list_of_strings, key = f), f)]
#4
def ex4(dict):
    com = int(input('Enter a Command' + '\n'))
    match com:
        case 1:
            print(dict["sir_name"])
        case 2:
            print(dict["birth_date"][3:5])
        case 3:        
            print(len(dict["hobbies"]))
        case 4:
            print(dict["hobbies"][-1])
        case 5:
            dict["hobbies"].append("Cooking")
            print(dict["hobbies"][-1])
        case 6:        
            dict["birth_date"] = (dict["birth_date"][0:2], dict["birth_date"][3:5], dict["birth_date"][6:])
            print(dict["birth_date"])
        case 7:               
            dict["age"] = "52"
            print(dict["age"])
    
    
    

def main():
    #1
    list_of_tuples = [('wedges','580'),('heels','890'),('sneakers','500')];
    sort_prices(list_of_tuples);
    #2
    tup1 = (2,4);
    tup2 = (9,6,3);
    mult_tuple(tup1,tup2);
    #3
    list_of_words = ['deltas', 'retainers', 'desalt', 'pants',
    'slated', 'generating', 'ternaries', 'smelters', 'termless',
    'salted', 'staled', 'greatening', 'lasted', 'resmelts']
    sort_anagrams(list_of_words)
    #4
    dict = {'first_name':'Mariah','sir_name':'Carey','birth_date':'27.03.1970','hobbies':['Sing', 'Compose', 'Act']}
    ex4(dict)

if __name__ == '__main__':
     main()
     
