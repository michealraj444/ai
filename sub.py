r = set()  # To store unique subsets

def sub(i, current, k):
    if sum(current) == k:
        r.add(tuple(sorted(current)))  # Add the subset as a tuple to the set
    if i == len(nums):  # Base case: reached the end of the list
        return
    # Exclude the current element and move to the next
    sub(i + 1, current, k)
    # Include the current element and move to the next
    current.append(nums[i])
    sub(i + 1, current, k)
    current.pop()  # Backtrack

nums = list(map(int, input("Enter list: ").split()))
k = int(input("Target sum (k): "))
sub(0, [], k)
print(r)
