import sys

sys.stdin = open("_직사각형길이찾기.txt")

t = int(input())

for tc in range(1, t + 1) :
    data = list(map(int, input().split()))
    result = 0