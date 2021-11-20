password = 'a123456'
i = 3
while True:
	pws = input ("please enter password:")
	if pws == password:
		print('Sucess')
		break # Break Loop
	else:
		i = i - 1
	print('Password incorrect, you can try',i)
	if i == 0:
		break
