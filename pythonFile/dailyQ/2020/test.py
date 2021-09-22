
class solution:
    def __init__(self,nums,target):
        self.nums =nums
        self.target =target
    def twoSum(self) :
        hashmap = {}
        for index,num in enumerate(self.nums):
            anothernum=self.target - num
            if anothernum in hashmap:
                return [hashmap[anothernum],index]
            hashmap[num] = index
        return None
    def twoSum_(self,numsIn,targetIn):
        for num in numsIn:
            anothernum=targetIn - num
            if anothernum in numsIn:
                return anothernum,num,targetIn
        return None




# twoSum([23,4,22,5,7,6,1,3,9],30)