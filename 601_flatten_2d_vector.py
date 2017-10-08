'''
Implement an iterator to flatten a 2d vector.

Example
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,2,3,4,5,6].
'''

class Vector2D:

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        self.x = 0
        self.y = 0
        self.vec2d = vec2d

    # @return {int} a next element
    def next(self):
        if self.hasNext():
            num = self.vec2d[self.x][self.y]
            self.y += 1

            if self.y >= len(self.vec2d[self.x]):
                self.x += 1
                self.y = 0

            return num

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        return self.x < len(self.vec2d) and self.y < len(self.vec2d[self.x])


#  not good way
# class Vector2D:
#
#     def __init__(self, vec2d):
#         self.index = 0
#         self.nums = []
#         for vector in vec2d:
#             for num in vector:
#                 self.nums.append(num)
#
#     def next(self):
#         if self.hasNext():
#             num = self.nums[self.index]
#             self.index += 1
#             return num
#
#
#     def hasNext(self):
#         return self.index < len(self.nums)



# def main():
#     vec2d = [ [1,2],
#               [3],
#               [4,5,6]]
#     i = Vector2D(vec2d)
#     print(i.next())
#     print(i.next())
#     print(i.next())
#     print(i.next())
#     print(i.next())
#     print(i.next())
#     print(i.next())
# if __name__ == '__main__':
#     main()
