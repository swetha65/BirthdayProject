from BirthdayChecker import *
import os

def prepareTemplate():
	name = getnameString()
	if name == "":
		return ""
	else:
		cur_path = os.path.dirname(__file__)
		new_path_dir = os.path.join(os.path.split(cur_path)[0], "templates")
		new_path = os.path.join(new_path_dir,"birthdaytemplate.html")
		img_path = os.path.join(os.path.split(cur_path)[0], "data", "cake2.jpg")
		with open(new_path, "r") as f:
			body = f.read()
			body = body.replace("birthday_names", name)
		final_template = os.path.join(new_path_dir,"birthdaytemplatereplaced.html")
		with open(final_template, "w") as f:
			f.write(body)
		return final_template