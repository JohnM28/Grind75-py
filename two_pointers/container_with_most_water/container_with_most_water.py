def container_with_most_water(height: list) -> int:
    """
    Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
    """
    left = 0
    right = len(height) - 1
    max_area = 0
    while left <= right:
        area = min(height[left], height[right]) * abs(left - right)
        if area > max_area:
            max_area = area
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return max_area
