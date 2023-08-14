def total(galleons, sickles, knuts):
    return (galleons*17 + sickles) * 29 +knuts

coins = [100, 50, 25]

# use
# *coins
# so you can pass all the values of the list to the function
# instead of coins[0], coins[1], coins[2]
print("###########\nEXAMPLE 1\n")
print (total(*coins), "Knuts")

#### EXAMPLE 2
print("###########\nEXAMPLE 2\n")
print(total(galleons=100, sickles=50, knuts=25), "Knuts")


#### EXAMPLE 3
print("###########\nEXAMPLE 3\n")

coins_dic = {"galleons":100,  "knuts":25, "sickles":50}
# for dictionaries, use two **
# the effect is similar to EXAMPLE 2, order doesnt matter because use the same name
print (total(**coins_dic), "Knuts")
