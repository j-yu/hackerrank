'''
Problem Statement

There is an array of n integers. There are also two disjoint sets, A and B, each containing m integers.
You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0.
For each i integer in the array, if i is an element of set A, you add 1 to your happiness.
If i is an element of B, you add -1 to your happiness. Otherwise, your happiness does not change.
Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

Input Format

The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

'''

n, m = map(int, input().split())
n_elements = map(int, input().split())
a_elements = set(map(int, input().split()))
b_elements = set(map(int, input().split()))

happiness = 0
for i in n_elements:
    if i in a_elements:
        happiness += 1
    elif i in b_elements:
        happiness -= 1

print(happiness)
