from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    sender_email= "iftakher@zoho.com"
    sender_password= "esY7KU8w5pxx"
    receiver_email= email

    subject= "Height statistics"
    message= f"Hey there, your height is <strong>{height}</strong> cm <br> and average height is <strong>{average_height}</strong> cm <br> and that is derived out of <strong> {count} </strong> people's data "

    msg= MIMEText(message, "html") # this means the string inside 'message' variable will be read as html
    
    msg["Subject"]= subject
    msg["To"]= receiver_email
    msg["From"]= sender_email

    zoho_mail= smtplib.SMTP('smtp.zoho.com', 587) # putting smtp server address and port no and later applying some methods.
    zoho_mail.ehlo()
    zoho_mail.starttls()
    zoho_mail.login(sender_email, sender_password)
    zoho_mail.send_message(msg)





