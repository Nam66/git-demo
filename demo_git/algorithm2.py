input_str = input('enter number list:')
usList = input_str.split()
a = sorted(input_str)
b = sorted(a, key=input_str.count)
print(b)

