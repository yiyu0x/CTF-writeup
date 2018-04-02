from pwn import *
r = remote('140.110.112.29',5119)
r.recvline() #Can you help us?
r.recvline()


print(r.recvline())

for i in range(100):
	print(r.recvline())

	s = r.recvline()

	one = s.split('?')
	print(one)
	two = one[1].split('=')
	print(two)

	if(int(one[0]) + int(two[0]) == int(two[1])):
		print('+')
		r.sendline('+')
	elif(int(one[0]) - int(two[0]) == int(two[1])):
		print('-')
		r.sendline('-')
	elif(int(one[0]) * int(two[0]) == int(two[1])):
		print('*')
		r.sendline('*')

print(r.recvline())

# print(r.recvline())


# print(r.recvline())
