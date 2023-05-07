from operator import itemgetter
if __name__ == '__main__':
    x = int(input())
    list1 = [] 
    for _ in range(x):
        name = input()
        score = float(input())
        sublist = []
        sublist.append(name)
        sublist.append(score)
        list1.append(sublist)
        sublist = []
    def sort(list1):
        l = len(list1)
        for i in range(0, l):
            for j in range(0, l-i-1):
                if (list1[j][1] > list1[j + 1][1]):
                    tempo = list1[j]
                    list1[j]= list1[j + 1]
                    list1[j + 1]= tempo
        return list1
    sortedArr = sort(list1)
    alphaSort = []
    for i in range(1,len(sortedArr)):
        if sortedArr[1][1] == sortedArr[i][1]:
            alphaSort.append(sortedArr[i][0])
    alphaSort.sort()
    for k in alphaSort:
        print(k)

            