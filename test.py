from typing import List, Counter

'''
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        l1 = []
        l2 = []
        for i in range(len(nums) -1):
            if nums[i] in l1 :
                l2.append(nums[i])
            else :
                l1.append(nums[i])
        return l2
'''


'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num = set(nums)
        heads = ListNode(0)
        heads.next = head

        while heads.next:
            if heads.next.val in num:
                head.next = head.next.next
            else:
                heads = heads.next
        return heads.next
'''

'''
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        res=0
        for i in range(n):
            if nums[i] == 0:
                for y in[-1,1]:
                    temp = nums[:]
                    x = i
                    z = y

                    while 0 <= i < n :
                        if temp[i] == 0:
                            i+=z
                        else:
                            temp[i] -=1
                            z*=-1
                            i +=z
                    if all(x==0 for x in temp):
                        res+=1
        return res
'''
'''
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guard = [[0]*n for _ in range(m)]
        for x, y in guards:
            guard[x][y] = 1
        for x, y in walls:
            guard[x][y] = 2

        di = [(-1,0), (1,0), (0,-1), (0,1)]

        for x,y in guards:
            for r,c in di:
                dr, dc = r+x, c+y
                while 0 <= dr < m and 0<= dc < n and guard[dr][dc] != 1 and guard[dr][dc] != 2:
                    if guard[dr][dc] == 0:
                        guard[dr][dc] = 3
                    dr += r
                    dc += c

        return sum(cell == 0 for cell in guard for row in cell)
'''
'''
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res =0
        arr = []
        n = len(bank)
        for i in range(n):
            a = bank[i].count('1')
            if a > 0:
                arr.append(a)
        for i in range(len(arr)-1):
            res += arr[i]*arr[i+1]

        return res
'''
'''
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res=0
        n = len(colors)
        
        for i in rangen(1,n):
            if colors[i] == colors[i-1]:
                res += min(neededTime[i], neededTime[i-1])
                neededTime[i] = max(neededTime[i], neededTime[i-1])
        
        return res
'''
'''
class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        a = n//7
        b=n%7
        if a>=1:
            for i in range (0,a):
                res +=(28+7*i)
            for i in range (0,b):
                res += i+1+a
        else:
            for i in range (b):
                res += i+1

        return res
'''
'''
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        a = []
        for i in range(n-k+1):
            res=0
            num = nums[i:i+k]
            sub = Counter(num)
            subs = sorted(sub.items(), key=lambda item: (-item[1],-item[0]))
            top_x = subs[:x]
            for num,count in top_x:
                res+=num*count
            a.append(res)
        return a
'''

'''
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            t = ""
            for i in range(len(s)-1):
                val = (int(s[i])+int(s[i+1]))%10
                t +=str(val)
            s=t
        return s[0]==s[1]
'''

'''
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        a = self.binary(n)
        res= 0
        for i in range(len(a)):



    def binary(self, n: int) -> str:
        if n==0:
            return "0"
        a=""
        while n>0:
            a = str(n%2)+a
            a//=2
        return a
'''
'''
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        res=0
        while num1!=0 amd num2!=0:
            if(num1 > num2):
                num1-=num2
            else:
                num2-=num1
            res+1
        return res
'''

'''
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        left = 0
        res= 1
        for right in range(len(nums)):
            while nums[right]-nums[left]>2*k:
                left+=1
            size=right-left+1
            res = max(res,min(size,numOperations+1))

            if(res>numOperations):
                break
        return res
'''

'''
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 in nums:
            return n-nums.count(1)

        min_len = float('inf')
        for i in range(n):
            g=nums[i]
            for j in range(i,n):
                g = self.UCLN(g, nums[j])
                if g==1:
                    min_len=min(min_len,j-i+1)
                    break
        if min_len == float('inf'):
            return -1
        return n + min_len-2

    def UCLN(self, a: int, b:int)->int:
        while b!=a:
            if a>b:
                a-=b
            else:
                b-=a
        return a
'''

'''
class Solution:
    def maxOperations(self, s: str) -> int:
        zeros=0
        res=0

        for c in reversed(s):
            if c=='0':
                zeros+=1
            else:
                res+=zeros

        return res
'''

'''
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        for i in range (len(nums)):
            if nums[i]==original:
                original*=2
        return original
'''


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums.sort()
        res=1
        for i in range(len(nums)-1):
            if 2*nums[i] > nums[len(nums)-1]:
                res=-1
        return res
nums = [1,2,3,4]
print(Solution().dominantIndex(nums))
