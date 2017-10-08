class Result:
    def __init__(self, x, y):
        self.x = x
        self.y = y

from heapq import heappush, heappop
def main():
    heap = []
    heappush(heap, (1, 2, Result(1, 2)))
    print(heappop(heap))



if __name__ == '__main__':
    main()
