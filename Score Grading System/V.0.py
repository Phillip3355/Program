'''
Author: Phillip
Date: 25.09.18
'''

L = []
while True:
    print('')
    print('1. show ranking & mean of scores')
    print('2. Add scores')
    print('3. Delete a score')
    print('4. Exit')
    print('')
    menu = input('choice : ')

    if menu == '1':
        if len(L) == 0:
            print('\nNo data error')
            continue
        print('\nScore board\n')
        print('==============')
        for i in range(0,len(L)):
            print(i+1,'\t',L[i])
        print('==============')
        print('score mean : ', end =(''))
        print(sum(L)/len(L))

    elif menu == '2':
        print()
        while True:
            add = input('Enter score (0..100) (otherwise exit)')
            add = int(add)
            if 0<=add<=100:
                L.append(add)
                print(L)
                continue
            else:
                L.sort(reverse=True)
                break

    elif menu == '3':
        kill = int(input('Enter a score to delete : '))
        if kill in L :
            L.remove(kill)
        else :
            print('Score missing error')
        
    elif menu == '4':
        break
    
    else:
        print('\nTry again.')
