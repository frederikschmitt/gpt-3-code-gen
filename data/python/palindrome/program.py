input_str = input("Enter a string: ")
reversed_str = reversed(input_str)
if list(input_str) == list(reversed_str):
    print(f"String {input_str} is a palindrome.")
else:
    print(f"String {input_str} is not a palindrome.")