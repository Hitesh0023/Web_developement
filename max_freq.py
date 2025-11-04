nums = input("Enter the numbers separated by commas : ").split(",")
nums = [int(x) for x in nums]
unique_nums = set(nums)

freq = {}
for num in unique_nums:
    freq[num] = nums.count(num)

max_freq = max(freq, key=freq.get)
min_freq = min(freq, key=freq.get)

print(f"Number appearing most times {max_freq} = {freq[max_freq]} times")
print(f"Number appearing least times {min_freq} = {freq[min_freq]} times")