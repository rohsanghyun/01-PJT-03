import sys

sys.stdin = open("_소득불균형.txt")

t = int(input())

for num in range(t):
    n = int(input())
    s = list(map(int,input().split()))