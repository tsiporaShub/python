
def find_primes(num):
    myList = []
    for num in range(num):
        if num > 1:
            flag = True
            for i in range(2, num):
                if num % i == 0:
                    flag = False
            if flag == True:
                myList.append(num)
    return myList


def sort_list(list1):
    return sorted(list1)

