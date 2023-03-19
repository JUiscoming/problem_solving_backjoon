### 최소, 최대값 탐색
```python
nums: List[int]

# 1. 정렬 후 찾기: O(N * logN)
nums.sort()
m, M = nums[0], nums[-1]

# 2. 선형 탐색: O(N)
min(nums), max(nums)
```
- 1회성 탐색인 경우, 정렬은 비효율적.