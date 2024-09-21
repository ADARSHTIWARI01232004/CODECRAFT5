def three_sum(nums):
    nums.sort()  # Sort the array to make it easier to avoid duplicates and use two-pointer technique
    result = []
    
    for i in range(len(nums) - 2):
        # Skip the duplicate elements to avoid repeating triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Move the left pointer to the right, skipping over duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Move the right pointer to the left, skipping over duplicates
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1  # We need a larger sum, move the left pointer to the right
            else:
                right -= 1  # We need a smaller sum, move the right pointer to the left
    
    return result

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
triplets = three_sum(nums)
print(triplets)  # Output should be [[-1, -1, 2], [-1, 0, 1]]
