class Account:
    def __init__(self):
        pass
    #vstup do kasina
    def first_in_casino(self):
        with open("accounts_list", mode="w")as account_databases:
            print("---")   
        with open("accounts_and_passwords_list", mode="w") as accounts_and_passwords_databases:
            print("----------")
        with open("badget_databases", mode="w")as badget_databases:
            print("vsechno pro vas pripravujueme")
            print("---------------")
        print("vse je pripraveno")
    #Tvorba uctu
    #Kontrola uctu
    #1. priprava
    def sorter_account_list(self):
        with open("accounts_list", mode="r") as account_databases:
            account_databases_list=[]
            accounts_prepare_to_list=account_databases.readlines()
            for one_account in accounts_prepare_to_list:
                one_account=one_account.strip()
                account_databases_list.append(one_account)
            return account_databases_list   

    def sorter_accounts_and_passwords_dictonary(self):
        with open("accounts_and_passwords_list", mode="r") as account_and_paswords_databases:
            a_or_p=0
            account_list=[]
            password_list=[]
            account_and_paaswords_databases_dictonary={}
            accounts_prepare_to_dictonay=account_and_paswords_databases.readlines()
            
            for one_account in accounts_prepare_to_dictonay:
                
                one_account=one_account.strip()
                if a_or_p==0:
                    account_list.append(one_account)
                    a_or_p+=1
                else:
                    password_list.append(one_account)
                    a_or_p=0
          
            for one_c_account in  account_list:
                
                count_password=0
                
                account_and_paaswords_databases_dictonary[one_c_account]=password_list[count_password]
                
                count_password+=1
            return account_and_paaswords_databases_dictonary
    # nacitani badgetove database            
    def sorter_badget_databases_to_dictonary(self):
        with open("badget_databases", mode="r") as account_and_badget_databases:
            a_or_p=0
            account_list=[]
            badget_list=[]
            account_and_badget_databases_dictonary={}
            accounts_prepare_to_dictonay=account_and_badget_databases.readlines()
            
            for one_account in accounts_prepare_to_dictonay:
                
                one_account=one_account.strip()
                if a_or_p==0:
                    account_list.append(one_account)
                    a_or_p+=1
                else:
                    badget_list.append(one_account)
                    a_or_p=0



            for one_c_account in  account_list:
                
                count_badget=0
                
                account_and_badget_databases_dictonary[one_c_account]=badget_list[count_badget]
                
                count_badget+=1
            
        return account_and_badget_databases_dictonary    
    # nacitani listu uctu
    def sorter_badget_to_list(self):
        with open("badget_databases", mode="r") as account_and_badget_databases:
            a_or_p=0
            account_list=[]
            badget_list=[]
            account_and_badget_databases_dictonary={}
            accounts_prepare_to_dictonay=account_and_badget_databases.readlines()
            
            for one_account in accounts_prepare_to_dictonay:
                
                one_account=one_account.strip()
                if a_or_p==0:
                    account_list.append(one_account)
                    a_or_p+=1
                else:
                    badget_list.append(one_account)
            
                    a_or_p=0
        return account_list


    #2. vytvareni uctu
    # Check databaze
    def account_databases_checking(self, new_account):
        account_databases_list=self.sorter_account_list()
        if new_account in account_databases_list:
            return False
        else:
            return True

    # samotna tvorba uctu
    def creating_account(self):
        a_name=input("jak se chcete jmenovat?\n")
        account_dont_exist=self.account_databases_checking(a_name)
        
        while account_dont_exist!=True:
            a_name=input("Tento ucet jiz bohuzel existuje musite pouzit jiny.\njak se chcete jmenovat?\n")
            account_dont_exist=self.account_databases_checking(a_name)
        password=input("vymyslete heslo. min. 5 znaku\n")
        while len(password)<5:
            password=input("heslo je moc kratke.\npotrbujete min 5 znaku\n zkuste vymyslet nove")
        vise_badgetu=0
        
        with open("accounts_list", mode="a")as account_list:
            account_list.write(f"{a_name}\n")
        with open("accounts_and_passwords_list", mode="a")as accounts_and_passwords_list:
            accounts_and_passwords_list.write(f"{a_name}\n")
            accounts_and_passwords_list.write(f"{password}\n")
        with open("badget_databases", mode="a")as badget_databases:
            badget_databases.write(f"{a_name}\n")
            badget_databases.write(f"{vise_badgetu}\n")
        print("Vse je v poradku vas ucet byl vytvoren")
    

    # login
    def login(self):
        account_name=input("zadejte jmeno vaseho uctu\n")
        check_a_exist=self.account_databases_checking(account_name)
        while check_a_exist!=False:
            account_name=input("Litujeme dany ucet bohuzel neexistuje.\nzadejte jmeno vaseho uctu\n")
            check_a_exist=self.account_databases_checking(account_name)
        user_password=input("zadejte heslo\n")
        all_acounts_and_paswords_dictonary=self.sorter_accounts_and_passwords_dictonary()
        while all_acounts_and_paswords_dictonary[account_name]!=user_password:
            user_password=input("Heslo bohuzel neni spravne.\n zkuste to znovu\nzadejte heslo\n")
        print(f"Vytejte v casinu royale {account_name}")

    # prepisovani bodu uctech
    def badget_updating_function(self, account, actual_badget):
        
        dictonary_accounts=self.sorter_badget_databases_to_dictonary()
        list_accounts=self.sorter_badget_to_list()
        dictonary_accounts[account]=actual_badget
        with open("badget_databases", mode="w")as badget_databases:
            badget_databases.seek(0)
            length=len(list_accounts)
            for one_member in range(0,length):
                badget_databases.write(f"{list_accounts[one_member]}\n")
                badget_databases.write(f"{dictonary_accounts[list_accounts[one_member]]}\n")
                
    def inporting_badget(self, account):
        dict_bag=self.sorter_badget_databases_to_dictonary()
        badget=dict_bag[account]        
        return badget  
        
        
