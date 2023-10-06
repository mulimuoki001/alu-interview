#!/usr/bin/python3

def rain(walls):
    if len(walls) == 0:
        return 0
    left = 0
    right = len(walls) - 1
    left_highest = 0
    right_highest = 0
    total_water = 0

    while left < right:
        if walls[left] < walls[right]:
            if walls[left] >= left_highest:
                left_highest = walls[left]
            else:
                total_water += left_highest - walls[left]
            left += 1
        else:
            if walls[right] >= right_highest:
                right_highest = walls[right]
            else:
                total_water += right_highest - walls[right]
            right -= 1
    return total_water
