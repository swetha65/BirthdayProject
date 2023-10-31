# import required packages
import datetime
import pandas as pd
import os

template = '''
Wishing you a very Happy Birthday {{name}}! May you be gifted with life's biggest joys and never-ending bliss.

Regards,
CP Team
'''

def fillTemplate():
	birthdayList = checkBirthday()
	if birthdayList[0] == 0:
		return ""
	elif birthdayList[0] == 1:
		name = birthdayList[1][0]
	else:
		name = ""
		for i in range(0,len(birthdayList[1])):
			if i == (len(birthdayList[1]) - 2):
				name += birthdayList[1][i] + " "
			elif i == (len(birthdayList[1]) - 1):
				name += "and " + birthdayList[1][i]
			else:
				name += birthdayList[1][i] + ", "
	message = f"Wishing you a very Happy Birthday {name}! May you be gifted with the biggest joys and never-ending bliss of life."
	print(message)


        

def checkBirthday():
	cur_path = os.path.dirname(__file__)
	pathlist = os.path.split(cur_path)
	new_path = os.path.join(pathlist[0], "data")
	new_path = os.path.join(new_path,"Birthdays.xlsx")
	df = pd.read_excel(new_path)
	df = df.dropna()
	birthday_dict = df.set_index("Name").T.to_dict("list")
	today = datetime.datetime.now().strftime("%d/%m") # today date in format : DD-MM
	numOfBirthdays = 0
	birthdayList = []
	for name in birthday_dict.keys():
		if today == birthday_dict[name][0]:
			numOfBirthdays += 1
			birthdayList.append(name)

	return [numOfBirthdays, birthdayList]

fillTemplate()

