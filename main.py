print('Please type "C" for a cube and "T" tetrahedron')
while True:
    option = input()
    if option == 'C':
        cube = int(input('Enter the length of the side of the cube in centimeters: '))
        result = cube ** 3
        print('The volume of the cube is ' + str(result) + ' centimeters')
    elif option == 'T':
        tetrahedron = int(input('Enter the length of the side of the tetrahedron in centimeters: '))
        result = tetrahedron ** 3 / (6 * (2 ** 0.5))
        print('The volume of the tetrahedron is ' + str(result) + ' centimeters')
    again = input("Next calculation? (yes/no): ")
    if again == "no":
            break
    else:
        print('Please type "C" for a cube and "T" tetrahedron')








#Programmet ska räkna ut volymen för en liksidig kub samt en liksidig tetrahedron
#Liksidig = alla sidor lika långa
#Ta in data från användaren och printa ut svaret
#Tänk på enheter, bestäm en enhet ni tar in information i, t.ex cm
#Då får ni också ut svaren i kubikcentimeter (cm3) 1000 cm3 = 1 liter
#Eftersom programmet ska kunna räkna ut både en kub och en tetrahedron behöver ni låta användaren välja detta
#Exakt utförande är upp till individen.
#Försök först helt själv, hur långt kommer du? Låt det guida dina övningar
#Snegla på koden från gruppen (compound interest)
#Låna gärna från gruppens kod men gör om för att passa labben
#Google dig fram men försök undvika att kopiera rakt av
#Formeln för volymen av en kub: V=a3
#Formeln för volymen av en tetrahedron: V=a3/62