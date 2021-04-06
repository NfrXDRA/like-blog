import random,amino,os
clint=amino.Client()
def pasek(dau):
	m=10
	pas=''
	while len(pas)!=m:
		v=random.choice(dau)
		pas+=v
	return pas
dau='1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIPOASDFGHJKLZXCVMBN'
url=input('enter blog url   ')
blogId=clint.get_from_code(url).objectId
comI=clint.get_from_code(url)
comId=comI.path[1:comI.path.index('/')]
while True:
	dev=input('deviceId')
	em=pasek(dau)+'@bot.com'
	clint.register(nickname='bot',email=em,password='botpassword87658',deviceId=dev)
	clint.logout
	clint.login(email=em,password='botpassword87658')
	subclint=amino.SubClient(comId=comId,profile=clint.profile)
	clint.join_community(comId=comId)
	subclint.like_blog(blogId=blogId)
	os.system('clear')