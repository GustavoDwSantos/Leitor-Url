from ast import Break
import email
import smtplib
from email.mime.text import MIMEText

def sendemail(subject,to,msg, user, senha, login):
    
    sender = to
    receivers = [to]

    port = 587
    msg = MIMEText(msg)

    msg['Subject'] = subject
    msg['From'] = user
    msg['To'] = to


    try:
        server =smtplib.SMTP('smtp.gmail.com', port) 
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user=user, password=senha)
        server.sendmail(sender, receivers, msg.as_string())
        print("Successfully sent email")
        server.quit()
        return True
        
        
    except(smtplib.SMTPAuthenticationError): 
        print ("dados de autenticação incorretos, tente novamente")
        return False
        
def loginemail():
    user = input("insira sua conta gmail:\n")
    senha = input("insira sua senha para app:\n")
    return user,senha