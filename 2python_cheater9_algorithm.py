"""
@author:sqx0612@gmail.com
@software:PyCharm
@file:2python_cheater9_algorithm.py
@time:2022/7/11/011 23:47
"""

#复杂度的定义
#线性搜索
def Search(L,x):
    for i in L:
        if i==x:
            return True
    return False
#为了匹配x，将L中的每一个元素挨个拿出来匹配
#最佳情况就是1次，最坏情况len(L)次


#常数对复杂度的影响，最简单情况
def fact(n):
   #阶乘函数
    answer=1
    while n>1:
        answer*=n
        n-=1
    return answer

#answer=1和return answer，执行两次
#while n>1  n*n  answer=    n-1     n=  每轮循环总计五次
#所以复杂度为5n+2，与5n近似


#近似平方根

