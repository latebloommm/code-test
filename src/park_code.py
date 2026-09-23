import random
def lotto(a):

	win_num = random.randint(1,10)
	user_num = a

	if user_num == win_num:
		print("당첨")
	else:
		print("꽝 당첨번호는%d입니다." % win_num)
