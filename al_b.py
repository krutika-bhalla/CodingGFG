def can_win(nums):
    n = len(nums)

    # Try every possible pair for removal
    for i in range(n - 1):
        if nums[i] == nums[i + 1]:
            # Simulate removal of the pair
            new_nums = nums[:i] + nums[i + 2:]
            # If the next player can't win after this move, then the current player can win
            if not can_win(new_nums):
                return True

    # If no winning move was found, return False
    return False

def game_winner(nums):
    if can_win(nums):
        return "Alice"
    return "Bob"

# Test the function
arr = [1,3,3,1,6]
print(game_winner(arr))  # Expected: Bob

arr = [1,4,5,5,6]
print(game_winner(arr))  # Expected: Alice

arr = [1,4,4,5,5,6]
print(game_winner(arr))  # Expected: Bob

arr = [1,2,1,2,1,1,1,1]
print(game_winner(arr))