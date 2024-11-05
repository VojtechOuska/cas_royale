class CasinoMachine:
    import random
    def __init__(self,):
        pass

    #vklad
    def vklad_function(self, badget):
        vyse_vkladu=int(input("kolik chcete vlozit"))
        celkovy_stav_uctu=vyse_vkladu+badget
        return celkovy_stav_uctu

    # logika hry
    def panna_nabo_orel(self):
        list_p_o=("panna", "orel")
        nahoda=self.random.choice(list_p_o)
        return nahoda

    # hra panna nebo orel
    def game_p_or_o(self,badget):
        bet=int(input("kolik chcete vsadit"))
        while bet>badget:
            bet=int(input("kolik chcete vsadit"))
        na_co=input("Na co chcete vsadit, 'panna' nebo 'orel'")
        while na_co!="panna" or na_co!="orel":
            na_co=input("Muzete vsadit jenom na pannu nabo orla.\nNa co chcete vsadit, 'panna' nebo 'orel'")
        
        nahoda=self.game_p_or_o
        if nahoda=="panna":
            print("padla panna")
        else:
            print("padl orel")    
        
        if nahoda==na_co:
            badget+=bet
            print(f"Vyhrali jste vas stav uctu je {badget}")
        else:
            badget-=bet  
            print(f"Prohrali jste vas stav uctu je {badget}")

        if nahoda=="panna":
            print("padla panna")
        else:
            print("padl orel")    
        return badget