numbers = '123456789'
spaces = 8
arr = ['']*spaces
def check(arr):
	s = ''
	for i in range(8):
		s += numbers[i] + arr[i]
	s += '9'
	if(eval(s) == 100):
		print(s, eval(s))
	return
def checkSum(spaces, arr, i): 
	if i == spaces: 
		check(arr)
		return
	arr[i] = '+'
	checkSum(spaces, arr, i + 1) 

	arr[i] = '-'
	checkSum(spaces, arr, i + 1) 
    
	arr[i] = ''
	checkSum(spaces, arr, i + 1) 

# Driver Code 
checkSum(spaces, arr, 0) 
