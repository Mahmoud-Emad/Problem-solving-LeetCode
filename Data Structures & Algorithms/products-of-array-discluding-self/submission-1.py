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

        return zeko

    def __get_products(self,num, nums):
        
        result  = []
        for num_ in nums:
            if num_ != 0 and num_ == num:
                continue
            result.append(num_)
        return result