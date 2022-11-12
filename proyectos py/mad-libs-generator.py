#Loop back to this point code finishes
loop = 1

while (loop < 10):
    #Todas las preguntas que realizara el usuario para que las conteste
    noun = input('Selecciona un sustantivo: ')
    p_noun = input('Selecciona un sustantivo en plural: ')
    noun2 = input('Selecciona un sustantivo: ')
    place = input('Nombra un lugar: ')
    adjetive = input('seleciona un adjetivo')
    noun3=input('selecciona un sustantivo: ')
    
    #Displays the story based on the users input
    
    print('------------------------------------------------------')
    print('Be kind to your',noun,' - footed',p_noun)
    print('For a duck may be somebody s',noun2,',')
    print('Be kind to your ',p_noun,'in',place)
    print('Where the weather in always',adjetive,'.')
    print()
    print('You may think that is this the', noun3,',')
    print('-------------------------------------------------------')
    
    # Loop back to 'loop = 1'
    
    loop = loop + 1