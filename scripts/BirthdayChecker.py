# import required packages
import datetime
import smtplib

# your gmail credentials here
GMAIL_ID = 'swetha1654@gmail.com'
GMAIL_PWD = 'Swethas_47'

# define a function for sending email
def sendEmail(to, sub, msg):

	# connection to gmail
	gmail_obj = smtplib.SMTP('smtp.gmail.com', 587) 
	
	# starting the session
	gmail_obj.starttls()	 
	
	# login using credentials
	gmail_obj.login(GMAIL_ID, GMAIL_PWD) 
	
	# sending email
	gmail_obj.sendmail(GMAIL_ID, to, 
				f"Subject : {sub}\n\n{msg}") 
	
	# quit the session
	gmail_obj.quit() 
	
	print("Email sent to " + str(to) + " with subject "
		+ str(sub) + " and message :" + str(msg))
	

# driver code
if __name__=="__main__":
	
	# today date in format : DD-MM
	today = datetime.datetime.now().strftime("%d-%m") 
	
	# current year in format : YY
	yearNow = datetime.datetime.now().strftime("%Y")
	
	msg = "Test Email : " + today											 

	sendEmail("swetha6530@gmail.com", "Test Email",	msg) 

