text = input("Enter a string: ")
print("Original:", text)
print("Reverse:", text[::-1])
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")