#!usr/bin/env python
#coding:utf-8

# def concatenetedString(s1, s2):
#     A,B='',''
#     for i in s1:
#         if i not in s2:
#             A += i
#     for j in s2:
#         if j not in s1:
#             B += j
#     return A+B
# if __name__ == '__main__':
#     s1='aacdb'
#     s2='gafd'
#     print concatenetedString(s1,s2)

def kClosest(points,k):
    num_dict = {}
    sum_list = []
    index_list = []
    for each_list in points:
        sum_list.append(sum(each_list))

    for i,num in enumerate(sum_list):
        sum_list_sorted=sum_list.sort()
        num_dict[num] = i
    for key in range(k):
        index_list.append(num_dict[sum_list_sorted[key]])

    return [points[x] for x in range(index_list)]

if __name__ == '__main__':

    points = [[4,6],[4,7],[4,4],[2,5],[1,1]]
    # origin = [0, 0]
    k = 3
    print kClosest(points,k)