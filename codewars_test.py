
def dbl_linear_list(n):
    li = [1]
    for i in range(0, n):
        #print(li)
        val = li[i]

        if 2*val+1 not in li: li.append(2*val+1)
        if 3*val+1 not in li: li.append(3*val+1)
        li.sort()
        # if i == n-1:
        #     print("list", 3*val+1, 2*val+1, n)



    #print(li)
    #print(li[n])
    return li[n]


from sortedcontainers import SortedList
def dbl_linear_sorted(n):
    li = SortedList()
    li.add(1)
    for i in range(0, n):
        val = li[i]
        if 2*val+1 not in li: li.add(2*val+1)
        if 3*val+1 not in li: li.add(3*val+1)
        # if i == n-1:
        #     print("sorted", 3*val+1, 2*val+1)


    #print(li)
    # print(li[n])
    return li[n]

from queue import PriorityQueue
def dbl_linear(n):
    ret = 0
    li = PriorityQueue()
    li.put(1,1)
    s = {1}
    for i in range(0, n):
        val = li.get()
        v2 = 2*val+1
        v3 = 3*val+1
        if v2 not in s:
            li.put(2*val+1, 2*val+1)
            s.add(v2)
        if v3 not in s:
            li.put(3*val+1, 2*val+1)
            s.add(v3)

    return li.get()

# for i in range(1000, 1001):
#     print(dbl_linear_list(i), dbl_linear_sorted(i), dbl_linear(i))

print(dbl_linear_list(100000))

def test():
    assert dbl_linear(10) == 22
    assert dbl_linear(20) == 57
    assert dbl_linear(30) == 91
    assert dbl_linear(50) == 175
    #assert dbl_linear(1000) == 8590
    #assert dbl_linear(10000) == 163855
    print("Tests passed")
