#HW 1-1
list1 = [10, 15, 21, 28, 33, 40]
def Oddremoval(list1): 
    total = len(list1)     
    while total != 0:
       for i in list1:
           if i%2 != 0:
               list1.remove(i)
       total /= 2
Oddremoval(list1)
print(list1)

#HW 1-2
list2 = [10, 40, 30, 20, 50]
def SortSecond(list2):
    target = len(list2) - 2
    list2.sort()
    print(list2[target])
SortSecond(list2)
#HW 2
scores = [
['Justin', 89, 90, 100],
['Tom', 92, 87, 100],
['Jane', 90, 90, 100],
['Philip', 89, 95, 100]
]

score_tuples = [(item[0], tuple(item[1:])) for item in scores]

def CalculateAverage(score_tuple):
    return sum(score_tuple[1]) / len(score_tuple[1])

def FindHighestAverage(scores):
    highest_average = 0

    for student in scores:
        average_score = CalculateAverage(student)
        if average_score > highest_average:
            highest_average = average_score

    return highest_average
highest_avg = FindHighestAverage(score_tuples)
print(f"AVG:{highest_avg}")
#HW 3-1
dict1 = {'a': 5, 'b': 1, 'c': 3, 'd': 4, 'e': 2}
def FindTopThree(dict1):
    return sorted(dict1, key=dict1.get, reverse=True)[:3]
print(FindTopThree(dict1))
#HW 3-2
dict2 = {1: 'Apple', 2: 'Orange', 3: 'Pineapple', 4: 'watermelon'}
def DeleteShort(dict2):
    to_delete = [key for key, value in dict2.items() if len(value) < 6]
    for key in to_delete:
        del dict2[key]
    print(dict2)
DeleteShort(dict2)

    