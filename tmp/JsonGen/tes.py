# Giả sử rằng các biến results, skipMin, skipMax, và skipLimit đã được khởi tạo trước đó
results = []
skipMin = False
skipMax = False
skipLimit = False

min_val = None
max_val = 5
default = "test"

if min_val is not None and len(default) == min_val:
    print("First condition met")
    results.append(default)
    skipMin = True
elif max_val is not None and len(default) == max_val:
    print("Second condition met")
    results.append(default)
    skipMax = True
elif max_val is not None and len(default) < max_val:
    if min_val is None:
        print("Third condition met")
        results.append(default)
        skipLimit = True

print(results)
print(skipMin, skipMax, skipLimit)