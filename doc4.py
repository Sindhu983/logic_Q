import itertools
def test(my_dict):
    result = list(map(dict, itertools.combinations(my_dict.items(), 2)))
    return result    

students = {'V' : [1, 4, 6, 10], 'VI' : [1, 4, 12], 'VII' : [1, 3, 8]} 
# print("Original Dictionary:" students)
print("Combinations of key-value pairs of the said dictionary:")
print(test(students))

