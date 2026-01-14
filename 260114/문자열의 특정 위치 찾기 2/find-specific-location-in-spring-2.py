words = ["apple", "banana", "grape", "blueberry", "orange"]

ch = input().strip()

count = 0


for word in words:
    if word[2] == ch or word[3] == ch:
        print(word)
        count += 1
        
print(count)
        