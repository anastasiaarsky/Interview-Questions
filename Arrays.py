from typing import List


### 1. Remove Duplicates from Sorted Array

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that
# each unique element appears only once. The relative order of the elements should be kept the same.
#
# Since it is impossible to change the length of the array in some languages, you must instead have the
# result be placed in the first part of the array nums. More formally, if there are k elements after removing
# the duplicates, then the first k elements of nums should hold the final result. It does not matter what
# you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with
# O(1) extra memory.

def removeDuplicates(nums: List[int]) -> int:
    for i, num in reversed(list(enumerate(nums[:-1]))):
        if num == nums[i + 1]:
            del nums[i]
    return len(nums)


### 2. Rotate Array

# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

def rotate(nums: List[int], k: int) -> None:
    while k != 0:
        nums.insert(0, nums.pop())  # or nums = nums[-1:] + nums[:-1]
        k -= 1


# for some reason, leetcode doesn't like this answer even though when I print nums it returns the correct answer:
def rotate2(nums: List[int], k: int) -> None:
    nums = nums[len(nums) - k:len(nums)] + nums[0:len(nums) - k]
    print(nums)


# doesn't work when nums = [1,2] and k = 5 --> returns [1,2] instead of [2,1]
def rotate3(nums: List[int], k: int) -> None:
    shifted = nums[len(nums) - k:len(nums)]
    notshifted = nums[0:len(nums) - k]
    nums.clear()
    nums.extend(shifted + notshifted)


### 3. Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if
# every element is distinct.

def containsDuplicate(nums: List[int]) -> bool:
    nums_set = set(nums)
    if len(nums) != len(nums_set):
        return True
    return False


### 4. Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.

def singleNumber(nums: List[int]) -> int:
    for num in nums:
        if nums.count(num) == 1:
            return num

# without using count:
def singleNumber(nums: List[int]) -> int:
    found = set()
    repeated = set()
    for num in nums:
        if num in repeated:
            continue
        if num in found:
            found.remove(num)
            repeated.add(num)
        else:
            found.add(num)
    return found.pop()


### 5. Intersection of Two Arrays II

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the
# result must appear as many times as it shows in both arrays and you may return the result in any order.

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    intersection = []
    for num in nums1:
        if num in nums2:
            intersection.append(num)
            nums2.remove(num)
    return intersection


### 6. Plus One

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith
# digit of the integer. The digits are ordered from most significant to least significant in left-to-right
# order. The large integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of digits.

# Example 1:
#
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 2:
#
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

def plusOne(digits: List[int]) -> List[int]:
    strings = [str(i) for i in digits]
    resdigit = int("".join(strings)) + 1
    return [int(x) for x in str(resdigit)]


### 7. Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the
# non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.

def moveZeroes(nums: List[int]) -> None:
    noZeroes = [num for num in nums if num != 0]
    zeroes = [0] * (len(nums) - len(noZeroes))
    nums.clear()                      # for some reason nums = noZeroes + zeroes does not work
    nums.extend(noZeroes + zeroes)


### 8. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they
# add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

def twoSum(nums: List[int], target: int) -> List[int]:
    num_diff = [(num, target - num) for num in nums]
    for i, (num, diff) in enumerate(num_diff):
        if diff in nums:
            if diff == num and nums.count(diff) == 1 or i == nums.index(diff):   # clunky but needed for duplicates
                continue
            return [i, nums.index(diff)]

# using a dictionary:
def twoSum2(nums: List[int], target: int) -> List[int]:
    numdiff = {}
    for i, num in enumerate(nums):
        diff = target-num
        if diff in numdiff:
            return numdiff[diff], i
        numdiff[num] = i


### 9. Valid Sudoku

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the
# following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
#
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Example 1:
#
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:
#
# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there
# are two 8's in the top left 3x3 sub-box, it is invalid.

def isValidSudoku(board: List[List[str]]) -> bool:
    # check validity of digits
    validdigits = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "."}
    flattened_board = [digit for row in board for digit in row]
    for digit in flattened_board:
        if digit not in validdigits:
            return False
    # check row
    for row in board:
        rowNoPeriods = [i for i in row if i != '.']
        if len(rowNoPeriods) != len(set(rowNoPeriods)):
            print("Row Error")
            return False
    # check column
    for i in range(0, 9):
        colNoPeriods = [row[i] for row in board if row[i] != '.']
        if len(colNoPeriods) != len(set(colNoPeriods)):
            print("Column Error")
            return False
    # check subbox
    for k in range(0, 9, 3):
        for l in range(0, 9, 3):
            subbox = []
            for i in range(k, k+3):
                for j in range(l, l+3):
                    subbox.append(board[i][j])
            subboxNoPeriods = [i for i in subbox if i != '.']
            if len(subboxNoPeriods) != len(set(subboxNoPeriods)):
                print("Subbox Error")
                return False
    return True


### 10. Rotate Image

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.

