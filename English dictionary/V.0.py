m = {}
scoreboard = []
while True:
    print("\n\n\n\n\n**********************************\n*              Dictionary               *\n**********************************")
    print("1. Save words")
    print("2. Delete words")
    print("3. Print all words")
    print("4. Search word")
    print("5. Word Test")
    print("6. Show Test score")
    print("7. Exit")
    print('**********************************')
    
    menu = input('Select >> ')
    
    if menu == '1':
        print("Enter word to save. Press 'Enter' to finish")
        while True:
            word = input('\nWord : ')
            if len(word) == 0:
                break
            elif word in m:
                print('Already Exist')
                continue
            mean = input('mean : ')
            m[word] = mean

    if menu == '2':
        print('Enter word to deleted\n')
        while True:
            kill = input('Word : ')
            if kill in m:
                del m[kill]
                print('Deletion is completed')
                break
            else:
                print('No such words')
                continue

    if menu == '3':
        print('\n\n')
        for qq in m:
            print(qq,'\t',m[qq])

    if menu == '4':
        print('Enter word to search')
        sw = input('word : ')
        if sw in m:
            print('\n',sw,'\t',m[sw])
        else:
            print('Try again')

    if menu == '5':
        score = 0
        if len(m) == 0:
            print("Test can't be started, because of no words")
        else:
            for k in m:
                answer = input(f'{k}: ')
                if answer == m[k]:
                    print('Correct!')
                    score+=1
                else:
                    print('Wrong...')
            print('you got',score,'answers.')
            scoreboard.append(score)
            scoreboard.sort(reverse = True)

    if menu == '6':
        mem = 0
        cash = 0
        for p in range (1,len(scoreboard)):
                if mem == scoreboard[p]:
                        cash += 1
                else:
                        mem = scoreboard[p]
                        cash = 0
                print(p-cash,'rank',scoreboard[p],'answers')
        

    if menu == '7':
        print('Thanks for using dictionary')
        break
