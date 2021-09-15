print('Please type "C" for a cube and "T" tetrahedron')
while True:
    option = input()
    if option == 'C' or 'c':
        cube = int(input('Enter the length of the side of the cube in centimeters: '))
        result = cube ** 3
        print('The volume of the cube is ' + str(result) + ' cm^3')
    elif option == 'T' or 't':
        tetrahedron = int(input('Enter the length of the side of the tetrahedron in centimeters: '))
        result = tetrahedron ** 3 / (6 * (2 ** 0.5))
        print('The volume of the tetrahedron is ' + str(result) + ' cm^3')
    again = input("Press Enter to continue or type n to finish")
    if again == "n":
            break
    else:
        print('Please type "C" for a cube and "T" tetrahedron')