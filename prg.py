import smtplib
sender_email = 'clientpri22@gmail.com'
rec_email= 'primmmtu19@gmail.com'
password=input(str('Please enter your password:'))
message = 'Hey you might be suffering from '
a = int(input('Enter value for Heart-rate '))
b = int(input('Enter value for SPO2 '))
c = int(input('Enter value for Body Temperature '))

if (a<=100 and c>38):
    message=message+'\n ->fever  Remedies: Sit in a bath of lukewarm water, which will feel cool when you have a fever.'
if (a>100 and b<90):
    message=message+'\n ->Hypoxemia  Remedies: Oxygen therapy can be utilized'
if (a>100):
    message=message+'\n ->Tachycardia  Remedies: Catheter ablation'
if (a<60):
    message=message+'\n ->Bradycardia  Remedies: Pacemeaker needs to be implanted'
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email, password)
print('login sucess')
server.sendmail(sender_email,rec_email,message)

print('Email has been sent to',rec_email)
print('Report')
print(message)
k=input('Press any key to exit')