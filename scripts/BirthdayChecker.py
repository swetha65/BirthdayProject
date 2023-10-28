# import required packages
import datetime
import pandas as pd
import os

def checkBirthday():
	cur_path = os.path.dirname(__file__)
	print(cur_path)
	pathlist = os.path.split(cur_path)
	print(pathlist)
	new_path = os.path.join(pathlist[0], "data")
	print(new_path)
	new_path = os.path.join(new_path,"Birthdays.xlsx")
	print(new_path)
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

	return([numOfBirthdays,birthdayList])

checkBirthday()

