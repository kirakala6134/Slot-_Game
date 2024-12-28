import random
makine_bakiyesi = 1000000
baslangic_cash = int(input('TL cinsinden bakiyenizi giriniz:'))
cash = baslangic_cash
if cash > makine_bakiyesi:
    print("Mevcut bakiyeniz makine bakiyesini aşmaktadır. \n Lütfen 1.000.000 TL'den daha az bir miktar giriniz.")
    exit()
slot1=['🍒', '🍊', '🍇', '🍀', '🔔', '💰']
slot2=['🍒', '🍊', '🍇', '🍀', '🔔', '💰']
slot3=['🍒', '🍊', '🍇', '🍀', '🔔', '💰']

print('güncel bakiyeniz > ',cash)
while cash!=0:
    don=(input('slotları cevirmek için lütfen (dön) yazınız: '))
    if don=='dön':
        cash=cash-50
        a=random.choice(slot1)
        b=random.choice(slot2)
        c=random.choice(slot3)
        if a==b==c :
            print('-'*16)
            print( '|',a,'|',b,'|',c,'|')
            print('-'*16)
            cash=cash+500
            print('tebrikler üçte üç yaparak büyük ödülü kazandınız! güncel bakiyeniz >',cash)
        elif a==b!=c or a==c!=b or a!=b==c or a!=c==b or b==a!=c or b==c!=a or b!=a==c or b!=c==a or c==a!=b or c==b!=a or c!=a==b or c!=b==a :
            print('-'*16)
            print( '|',a,'|',b,'|',c,'|')
            print('-'*16)
            cash=cash+150
            print('tebrikler iki de iki yaprak küçük ölçekli ödülü kazandınız! güncel bakiyeniz >',cash,'TL')
        else:
            print('-'*16)
            print( '|',a,'|',b,'|',c,'|')
            print('-'*16)
            cash=cash-300
            print('hiç bir şey kazanamadınız lütfen tekrar deneyin! güncel bakiyeniz >',cash,'TL')
        if cash<= -1000:
            print('haciz geldi')
            exit()
        devam=input('oyuna devam etmek istiyormusunuz? \n devam etmek istiyorsanız(devam), çekilmek istiyorsanız(çık), yazınız: ')
        if devam=='çık':
            if cash < baslangic_cash:
                print('oyundan çekildiniz zararınız > ', (baslangic_cash)-(cash),'TL')
            elif cash > baslangic_cash:
                print('oyundan çekildiniz kârınız > ', (cash)-(baslangic_cash),'TL')
            else :
                print('kâr veya zararınız bulunmamaktır.')
            exit()
        elif devam=='devam':
            continue
        else:
            print('doğru cümleyi yazınız!')
            exit()
    else:
        print('lütfen doğru kelimeyi giriniz!')
        exit()