# import required packages
import datetime
import pandas as pd
import os

def prepareTemplate():
	name = getnameString()
	if name == "":
		return ""
	else:
		cur_path = os.path.dirname(__file__)
		new_path_dir = os.path.join(os.path.split(cur_path)[0], "templates")
		new_path = os.path.join(new_path_dir,"birthdaytemplate.html")
		with open(new_path, "r") as f:
			body = f.read()
			body = body.replace("birthday_names", name)
		final_template = os.path.join(new_path_dir,"birthdaytemplatereplaced.html")
		with open(final_template, "w") as f:
			f.write(body)
		return final_template

def getnameString():
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
	return name


        

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


print(prepareTemplate())
