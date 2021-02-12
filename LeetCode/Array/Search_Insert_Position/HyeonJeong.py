class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums):
            if n == target:
                return i
            elif n > target: # 크기순으로 정리된 리스트에 target이 들어가게 되는 인덱스 위치
                return i
        return len(nums)
    # target이 nums에 존재하지 않고, nums에서 가장 큰 수가 되는 경우에는 인덱스+1인 위치에 target이 들어가게 됨
