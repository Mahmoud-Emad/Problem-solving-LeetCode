from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            product = self.__get_products(num, nums)
            result.append(product)

        ress = None
        zeko = []
        for arr in result:
            for num in arr:
                if ress is None:
                    ress = num
                else:
                    ress = ress * num
            zeko.append(ress)
            ress = None
        print(zeko)
        return zeko
    def __get_products(self,num, nums):
        result  = []
        for num_ in nums:
            if num_ == num:
                continue
            result.append(num_)
        return result
            
            
        
s = Solution()

s.productExceptSelf([1,2,4,6]) # [48, 24, 12, 8]
s.productExceptSelf([-1,0,1,2,3]) # [0, -6, 0, 0, 0]
 
 
# Conclusion
# 1. Time Complexity: O(n)
# 2. Take each index except self then multiply them
# 2.1 For each index, get the product of all elements except self, Keep in mind that if the index is zero then the result will be 0 because the product of 0 and anything is 0.
# 3. Append the response of the setp 2 to the result
# 4. Return the result