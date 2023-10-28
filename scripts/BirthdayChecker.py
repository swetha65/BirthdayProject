# import required packages
import datetime
import pandas as pd

def checkBirthday():
	df = pd.read_excel("data\Birthdays.xlsx")
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

