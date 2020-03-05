# @File  : TwoStack.py
# @Author: Magic Huang
# @GitHub: github.com/MH-Blog
# @Date  : 2020/3/5


"""
 用一个数组实现两个栈，只需处理整型，实现l_pop/l_push/r_pop/r_push，需要UT。
"""


class TwoStack:
    def __init__(self, size):
        """
        :param size: 数组的初始长度
        """
        self.stack = [None for _ in range(size)]
        self.size1 = 0
        self.size2 = size - 1

    # 栈1的个数
    def l_num(self):
        return self.size1

    # 栈2的个数
    def r_num(self):
        return self.capacity() - self.size2 - 1

    # 栈1是否为空
    def isEmpty1(self):
        return self.size1 == 0

    # 栈2是否为空
    def isEmpty2(self):
        return self.size2 == self.capacity() - 1

    # 数组的大小
    def capacity(self):
        return len(self.stack)

    # 数组自动扩展大小
    def ensureCapacity(self):
        if self.l_num() + self.r_num() >= self.capacity():

            tempSize = self.capacity() * 2
            newStack = [None for _ in range(tempSize)]
            k = tempSize - 1
            for i in range(self.l_num()):
                newStack[i] = self.stack[i]
            for j in range(self.capacity() - 1, self.size2, -1):
                newStack[k] = self.stack[j]
                k -= 1
            self.size2 = tempSize - (self.capacity() - self.size2)
            self.stack = newStack

    # 栈1入栈
    def l_push(self, val):
        self.ensureCapacity()
        self.stack[self.size1] = val
        self.size1 += 1

    # 栈2入栈
    def r_push(self, val):
        self.ensureCapacity()
        self.stack[self.size2] = val
        self.size2 -= 1

    # 栈1出栈
    def l_pop(self):
        if (self.isEmpty1()):
            raise Exception("栈1不能为空")
        self.size1 -= 1
        val = self.stack[self.size1]
        self.stack[self.size1] = None
        return val

    # 栈2出栈
    def r_pop(self):
        if (self.isEmpty2()):
            raise Exception("栈2不能为空")
        self.size2 += 1
        val = self.stack[self.size2]
        self.stack[self.size2] = None
        return val


if __name__ == '__main__':
    stack = TwoStack(5)
    print(stack.isEmpty1())  # 判断栈1是否为空
    print(stack.isEmpty2())  # 判断栈2是否为空

    stack.l_push(1)  # 栈1添加一个元素
    stack.l_push(2)  # 栈1添加一个元素
    stack.r_push(10)  # 栈2添加一个元素
    print(stack.stack)

    print(stack.l_pop())  # 栈1取出一个元素
    print(stack.stack)

    for i in range(2, 6):  # 栈1添加4个元素
        stack.l_push(i)
    print(stack.stack)

    for i in range(9, 6, -1):  # 栈2添加3个元素
        stack.r_push(i)
    print(stack.stack)

    print(stack.r_pop())  # 栈2取出一个元素
    print(stack.stack)

"""
True
True
[1, 2, None, None, 10]
2
[1, None, None, None, 10]
[1, 2, 3, 4, 5, None, None, None, None, 10]
[1, 2, 3, 4, 5, None, 7, 8, 9, 10]
7
[1, 2, 3, 4, 5, None, None, 8, 9, 10]
"""
