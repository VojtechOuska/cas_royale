from brain import Account
from casino_machine import CasinoMachine
from side_functions import Cookie

cookie=Cookie()
player=Account()
casino=CasinoMachine()
first=input("jste v kasinu poprve? ano nebo ne?\n")
while first!="ano" and first!="ne":
    first=input("Muzete zadat poza ano nebo ne\njste v kasinu poprve? ano nebo ne?\n")
if first=="ano":
    player.first_in_casino()
print("vytejte v kasinu royale")

def casino_space():
    
    has_account=input("Mate jiz u nas ucet 'ano' nebo 'ne'\n")
    while has_account!="ano" and has_account!="ne":
        has_account=input("Muzete odpovedet pouze ano nebo ne.\nMate jiz u nas ucet 'ano' nebo 'ne'\n")
    if has_account=="ne":
        account=player.creating_account()
    account=player.login()
    badget=player.inporting_badget(account)
    badget=int(badget)
    print(f"vas badget je {badget}.")
    lets_bet="ano"
    while lets_bet=="ano":
        vklad=input("Chcete provest vklad\n")
        while vklad!="ano" and vklad!="ne":
            vklad=input("Muzete vlozit pouze!!! ano nebo ne.\nChcete provest vklad\n")
        if vklad=="ano":
            badget=casino.vklad_function(badget)
        while badget<=0:
            print("Mate na ucte moc malo penez, musito provest vklad")
            badget=casino.vklad_function(badget)
        lets_continue="ano"
        while badget>0 and lets_continue=="ano":
            badget=casino.game_p_or_o(badget)
            if badget<=0:
                break
            lets_continue=input("Chcete si jeste vsadit? ano nebo ne\n")
            while lets_continue!="ano" and lets_continue!="ne":
                lets_continue=input("Smite odpovidat pouze ano nebo ne.\nChcete si jeste vsadit? ano nebo ne\n")
        lets_bet=input("chcete pokracovat? ano nebo ne\n")
        while lets_bet!="ano" and lets_bet!="ne":
            lets_bet=input("Muzete zadat poze ano nebo ne chcete pokracovat? ano nebo ne\n")
    player.badget_updating_function(account, badget)
    print("Byli jste odhlaseni")
    ukonceni=input("Chcete kasino uplne vypnout?\n")
    while ukonceni!="ano" and ukonceni!="ne":
        ukonceni=input("Muzete zadat pouze ano nebo ne.\nChcete kasino uplne vypnout?\n")
    if ukonceni=="ne":
        casino_space()
casino_space()
print("Dekujeme za vas cas a tesime se na priste")
