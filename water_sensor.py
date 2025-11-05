"""
HW05 — Water Sensor: Streaming Median

Implement streaming_median(nums) -> list
"""

import heapq

def streaming_median(nums):
    if not nums:
        return []

    low = []   # max-heap (store negative values)
    high = []  # min-heap
    result = []

    for num in nums:
        # Step 1: Insert into max-heap (low)
        heapq.heappush(low, -num)

        # Step 2: Balance so that every element in low <= every element in high
        if low and high and (-low[0]) > high[0]:
            val = -heapq.heappop(low)
            heapq.heappush(high, val)

        # Step 3: Rebalance sizes so that len(low) >= len(high) and diff ≤ 1
        if len(low) > len(high) + 1:
            heapq.heappush(high, -heapq.heappop(low))
        elif len(high) > len(low):
            heapq.heappush(low, -heapq.heappop(high))

        # Step 4: Compute median
        if len(low) == len(high):
            median = (-low[0] + high[0]) / 2.0
        else:
            median = float(-low[0])

        result.append(median)

    return result


# Example manual test
if __name__ == "__main__":
    print(streaming_median([1, 2, 3]))        # [1, 1.5, 2]
    print(streaming_median([5, 15, 1, 3]))    # [5, 10.0, 5, 4.0]
    print(streaming_median([2, 4, 6, 8, 10])) # [2, 3.0, 4, 5.0, 6]
    print(streaming_median([]))               # []
