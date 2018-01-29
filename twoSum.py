class Solution:
    def twoSum(self, nums, target):
        nums_len = len(nums)
        for i in range(0,nums_len):
            for j in range(i+1, nums_len):
                if nums[i] + nums[j] == target:
                    result = []
                    result.append(nums[i])
                    result.append(nums[j])
                    return result

def main():
    import sys

    while True:
        try:

            ret = Solution().twoSum([1,3,4,5], 9)

            
            print(ret)
        except StopIteration:
            break

if __name__ == '__main__':
    main()