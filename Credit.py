IDEAL_CREDIT_SCORE = 720

userScore = int(input("Please enter your credit score:  "))
housePrice = int(input("Please enter the price of the house:  "))

if userScore >= IDEAL_CREDIT_SCORE:
    downPayment = 0.1 * housePrice

elif userScore < IDEAL_CREDIT_SCORE and userScore > 600:
        downPayment = 0.2 * housePrice
else:
    downPayment = 0.3 * housePrice

print ("Your down pament is: ${}".format(downPayment))
