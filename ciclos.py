ETHUSD = 239
cryptoCurrency = input('enter the name of the cryptocurency you want to invest: ')
cryptoCurrencyVal = float(input('enter the quantity of ' + str(cryptoCurrency) + ' that you have in your account: '))
i = cryptoCurrencyVal
while True: 
    invest = float(input('enter the quantity you want to invest in ' + str(cryptoCurrency) + ': '))
    i += invest
    print('Now you have',i,cryptoCurrency,'in your account')
    continueInvest = input('you want to continue investing in ' + str(cryptoCurrency) + '? :')
    if continueInvest == None or continueInvest == 'no' or continueInvest == 'No': 
        print('your balance in USD with',cryptoCurrency,'is :', i * ETHUSD)
        break
