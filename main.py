from Email_envio     import loginemail, sendemail
from urlopen import urlopen
from time import sleep

def main():
    login = False
    #Definições para configuração do email
    subject = "Preço café"
    to = "emailexemplo@gmail.com"
    #Loop para verificação de texto
    while True:
        
        preço = urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
        
        if float(preço) < 4.70:
            msg = f"o preço do cafe é {preço}\nPode comprar"   
            if login == False:
                user, senha = loginemail()
            login = sendemail(subject,to,msg,user,senha, login)
        else: 
            print(f"o preço do cafe é {preço} \nNão pode comprar")
        if login == True:
            sleep(10)
    

if __name__ == '__main__':
    main()