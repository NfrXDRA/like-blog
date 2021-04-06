import amino,os,getpass
clint=amino.Client()
password=getpass.getpass('\033[1;32mpassword  :  ')
u=input('\033[1;35mblog url : ')
co=input('\033[1;35mcomment : ')
blogId=clint.get_from_code(u).objectId
comI=clint.get_from_code(u)
comId=comI.path[1:comI.path.index('/')]
try:
	x=open('email.txt').read()
except FileNotFoundError:
	print('\033[1;31mcreate file email.txt')
pv=x.split('\n')
clb=str(pv)
how=clb.count(',')+1
start=0
for i in range(how):
	try:
		clint.login(email=pv[start],password=password)
	except:
		print('\033[1;31merror')
		exit()
	try:
		clint.join_community(comId=comId)
	except:
		print('\033[1;31merror')
		exit()
	try:
		subclint=amino.SubClient(comId=comId,profile=clint.profile)
		subclint.comment(blogId=blogId,message=co)
		start+=1
		os.system('clear')
		print('\033[1;36mdone'+pv[start])
	except:
		print('\033[1;31merror')
		exit()
