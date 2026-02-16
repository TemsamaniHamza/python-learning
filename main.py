


# nums1 = ["aaaa", "bbbb", "ccc", "eeee", "dddd", "5"]


# nums2 = [121, 232]


# for n1, n2 in zip(nums1, nums2):
#     print(n1, n2)
# nums1.reverse()
# print(nums1)
# nums1.sort(key=lambda x: len(x), reverse=True)
# print(nums1)
# for n in nums:
#     print(n)


# for i, n in enumerate(nums):
#     print(i,n)





# arr = [[0]* 4 for i in range(4)]

# print(arr)

# strings = ["ab", "cd", "ef"]
# s = "".join(strings)
# print(s)

# from collections import deque

# queue = deque()

# for i in range(3):
#     queue.append(i)
# print(queue)

# queue.popleft()

# queue.appendleft(-1)
# queue.pop()
# queue.pop()
# queue.pop()
# print(queue)

# myset = set()

# myset.add(1)
# myset.add(2)
# print(myset)
# print(len(myset))
# print(1 in myset)
# print(2 in myset)
# print(3 in myset)

# myset.remove(2)
# print(1 in myset)


# print (set([1,2,3]))

# myset = {i for i in range(5)}
# print(myset)




# myMap = {}
# myMap["alice"] = 99
# myMap["bob"] = 88
# print(myMap)
# print(len(myMap))

# myMap["alice"] = 80
# print(myMap["alice"])

# print("alice" in myMap)
# myMap.pop("alice")
# print("alice" in myMap)

# myMap = {"alice": 90, "bob":70}
# for key in myMap:
#     print(key, myMap[key])

# for key, val in myMap.items():
#     print(key, val)
# print("-------------")

# for val in myMap.values():
#     print(val)
# print(myMap)



# myMap = {i: i*i for i in range(6) if i % 2 == 0}
# print(myMap)

# tup = (1,2,3)

# print(tup[1])


# myMap = { (1,2): 3}
# # print(myMap[(1,2)])
# # print(myMap.items())
# mySet = set()
# mySet.add((1, 2))
# print((1,2) in mySet)

import heapq



# minHeap = []
# heapq.heappush(minHeap, -3)
# heapq.heappush(minHeap, -2)
# heapq.heappush(minHeap, -4)


# while len(minHeap):
#     print(-1 * heapq.heappop(minHeap))


def double(arr,val):
    def helper():
        for i, n in enumerate(arr):
            arr[i] *= 2

        nonlocal val
        val *= 2
    helper()
    print(arr, val)

nums = [1, 2]
val = 3

double(nums, val)