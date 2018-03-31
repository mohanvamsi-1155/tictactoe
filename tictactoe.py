def compare(arr1):
    c = list(zip(*arr1))
    for i in range(3):
        if list(set(arr1[i])) == ['X']:
            return 1
        elif list(set(arr1[i])) == ['O']:
            return 2
    for i in range(3):
        if list(set(c[i])) == ['X']:
            return 1
        elif list(set(c[i])) == ['O']:
            return 2
    count_x = 0
    count_o = 0
    for i in range(3):
        if arr[i][i] == 'X':
            count_x += 1
        elif arr[i][i] == 'O':
            count_o += 1
    if count_x == 3:
        return 1
    elif count_o == 3:
        return 2
    count_x = 0
    count_o = 0
    j = 2
    for i in range(3):
        if arr[i][j] == 'X':
            count_x += 1
        elif arr[i][j] == 'O':
            count_o += 1
        j -= 1
    if count_x == 3:
        return 1
    elif count_o == 3:
        return 2
    return 3


print("welcome to tic tac toe  ")
arr = [['-' for i in range(3)] for j in range(3)]
print("Initial game is :")
for i in range(3):
        print(' '.join(str(e) for e in arr[i]))
count = 0
while count < 9:
    print("Player 1 has the choice :")
    print("Enter index to place X in terms of spaces :")
    x, y = list(input().strip().split(' '))
    x, y = [int(x), int(y)]
    arr[x][y] = 'X'
    if compare(arr) == 1:
        print("Player 1 has won!")
        break
    print("The Tic Tac toe is")
    for i in range(3):
        print(' '.join(str(e) for e in arr[i]))
    count += 1
    if count == 9:
        break
    print("Player 2 has the choice :")
    print("Enter index to place O in terms of spaces :")
    x, y = list(input().strip().split(' '))
    x, y = [int(x), int(y)]
    arr[x][y] = 'O'
    if compare(arr) == 2:
        print("Player 2 has won!")
        break
    for i in range(3):
        print(' '.join(str(e) for e in arr[i]))
    count += 1
    print(count)
if compare(arr) == 3:
    print("Its a tie")
