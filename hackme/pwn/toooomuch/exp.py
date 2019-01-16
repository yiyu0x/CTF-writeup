from pwn import *

r = remote('hackme.inndy.tw', 7702)

print r.recvuntil('Give me your passcode:')

r.sendline(str(43210))

x = r.recvuntil('Guess a number from 0 to 100:')[:-1]
x = x.split()

up, down = int(x[4]), int(x[6])
guess = (up + down)/2

r.sendline(str(guess))

while True:
	try:
		x = r.recvuntil(':')[:-1]
	except:
		print r.recvuntil('}')
		break
	x = x.split('\n')[1].split()
	up, down = int(x[4]), int(x[6])
	print up, down
	guess = (up + down)/2
	r.sendline(str(guess))