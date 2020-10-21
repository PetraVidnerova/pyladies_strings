import random

cislo1 = 3
cislo2 = 4
vysledek = str(cislo1) + 'x' + str(cislo2) + ' je ' + str(cislo1*cislo2)
print(vysledek)

print(f"{cislo1}x{cislo2} je {cislo1*cislo2}")


# anezka = False
# if anezka == True:
#     y_a = 'á'
#     osloveni = 'Anežko'
# else:
#     y_a = 'ý'
#     osloveni = 'neznámý'

# soucet = 3 + 4
# podpis = 'Váš Program'


# print(f"""
# Mil{y_a} {osloveni},
# Váš výsledek je {soucet}.

# S pozdravem,
# {podpis}
# """)


# sablona = """
# Mil{y_a} {osloveni},
# Váš výsledek je {soucet}.

# S pozdravem,
# {podpis}
# """

# for anezka in True, False:
#     if anezka == True:
#         y_a = 'á'
#         osloveni = 'Anežko'
#     else:
#         y_a = 'ý'
#         osloveni = 'neznámý'
#     soucet = random.randrange(5) + random.randrange(5)

#     print(sablona.format(y_a=y_a,
#                          osloveni=osloveni,
#                          soucet=soucet,
#                          podpis="Váš Program")
#           )
