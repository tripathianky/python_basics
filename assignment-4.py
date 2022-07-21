phrase = input("Type in: ")
phrase = list(phrase)
letters, digits = 0, 0
for i in phrase:
    if i.isalpha():
        letters = letters + 1
    if i.isdigit():
        digits = digits + 1
    else:
        pass
print("Letters:", letters)
print("Digits:", digits)
