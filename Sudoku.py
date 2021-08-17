import random as rn

def display(a):
    print('\t {}'.format(('_'*35)))
    #print(f"\t|  {1}  {2}  {3}  |  {1}  {2}  {3}  |  {1}  {2}  {3}  |")
    print("\t|  {0[0]}  {0[1]}  {0[2]}  |  {1[0]}  {1[1]}  {1[2]}  |  {2[0]}  {2[1]}  {2[2]}  |".format((a[0][0]),(a[1][0]),(a[2][0])))
    print("\t|  {0[0]}  {0[1]}  {0[2]}  |  {1[0]}  {1[1]}  {1[2]}  |  {2[0]}  {2[1]}  {2[2]}  |".format((a[0][1]),(a[1][1]),(a[2][1])))
    print("\t|  {0[0]}  {0[1]}  {0[2]}  |  {1[0]}  {1[1]}  {1[2]}  |  {2[0]}  {2[1]}  {2[2]}  |".format((a[0][2]),(a[1][2]),(a[2][2])))

    print('\t|{0}|{0}|{0}|'.format(('_'*11)))

    print("\t|  {0[0]}  {0[1]}  {0[2]}  |  {1[0]}  {1[1]}  {1[2]}  |  {2[0]}  {2[1]}  {2[2]}  |".format((a[3][0]),(a[4][0]),(a[5][0])))
    print("\t|  {0[0]}  {0[1]}  {0[2]}  |  {1[0]}  {1[1]}  {1[2]}  |  {2[0]}  {2[1]}  {2[2]}  |".format((a[3][1]),(a[4][1]),(a[5][1])))
    print("\t|  {0[0]}  {0[1]}  {0[2]}  |  {1[0]}  {1[1]}  {1[2]}  |  {2[0]}  {2[1]}  {2[2]}  |".format((a[3][2]),(a[4][2]),(a[5][2])))

    print('\t|{0}|{0}|{0}|'.format(('_'*11)))

    print("\t|  {0[0]}  {0[1]}  {0[2]}  |  {1[0]}  {1[1]}  {1[2]}  |  {2[0]}  {2[1]}  {2[2]}  |".format((a[6][0]),(a[7][0]),(a[8][0])))
    print("\t|  {0[0]}  {0[1]}  {0[2]}  |  {1[0]}  {1[1]}  {1[2]}  |  {2[0]}  {2[1]}  {2[2]}  |".format((a[6][1]),(a[7][1]),(a[8][1])))
    print("\t|  {0[0]}  {0[1]}  {0[2]}  |  {1[0]}  {1[1]}  {1[2]}  |  {2[0]}  {2[1]}  {2[2]}  |".format((a[6][2]),(a[7][2]),(a[8][2])))

    print('\t|{0}|{0}|{0}|'.format(('_'*11)))


def sudoku(size):

    mydict = {}
    n = 0
    while len(mydict) < 9:
        n += 1
        x = range(1, size+1)
        testlist = rn.sample(x, len(x))

        isgood = True
        for dictid,savedlist in mydict.items():
            if isgood == False:
                break
            j=0
            row_position=len(mydict)
            row_factor=(row_position)%3
            for v in savedlist:
                x=j//3
                if testlist[j] == v:
                    isgood = False
                    break
                if row_factor>0:
                    for i in range(3*x,3*(x+1)):
                        if i==j:
                            continue
                        if mydict[row_position-1][i]==testlist[j]:
                            isgood = False
                            break
                        if row_factor==2:
                            if mydict[row_position - 2][i] == testlist[j]:
                                isgood = False
                                break

                j+=1
        if isgood == True:
            #print 'success', testlist
            mydict[len(mydict)] = testlist
    return mydict, n


def result(k):
    if k==81:                                             #k represents no of positions filled
        return 'Congrats, Sudoku completed!'

def error(a,b,r,c,n):
    for i in a[b]:                                        #checking whether the number is in same box or not
        if n in i:
            return 'That is a wrong step'
            break
    x=(b)//3                                              #constant that represents the boxes of same row in the below range
    for j in range(3*x,3*(x+1)):                          #checking whether the number is in same row or not
        if j==b:
            continue
        elif n in a[j][r]:
            return 'That is a wrong step'
            break
    y=(b)%3                                               #constant that represents the boxes of same column in the below range
    for k in range(y,y+7,3):                              #checking whether the number is in same column or not
        if k==b:
            continue
        elif n in (a[k][0][c],a[k][1][c],a[k][2][c]):
            return 'That is a wrong step'
            break


def game(a,m,d):                                #m represents no. of positions filled
    display(a)
    print(f'Start the game!')
    res=result(m)
    while not res:
        ins = input()
        if ins=='key':
            for q,w in d.items:
                print(q,w)
            res=result(81)
        else:
            ins=[int(i) for i in ins.split(' ')]
            box, row, column, num = (ins[0] - 1, ins[1] - 1, ins[2] - 1, ins[3])
            why=error(a,box,row,column,num)                                             #checking if error exists

            while why:
                print(f'That is a wrong move, Please re-enter correctly!')
                ins = [int(i) for i in input().split(' ')]
                box, row, column, num = (ins[0] - 1, ins[1] - 1, ins[2] - 1, ins[3])
                why = error(a, box, row, column, num)

            a[box][row][column]=num                                              #if no error, placing the number into respective position
            display(a)
            m += 1                                                              #increament of positions filled
            res = result(m)
            if not res:
                print(f"make a move")
    print('Your game:')
    print(res)


grid=[[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]]

return_dict,total_tries= sudoku(9)
alpha=return_dict
for n,v in return_dict.items():
    p=n//3
    k=0
    for i in range(3*p,3*(p+1)):
        grid[i][n%3]=v[k:k+3]
        k+=3

empty_positions = 75
empty_boxes= 0
while(empty_boxes< empty_positions):
    p=rn.randrange(0,9)
    r=rn.randrange(0,3)
    c=rn.randrange(0,3)
    if grid[p][r][c]!=' ':
        grid[p][r][c]= ' '
        empty_boxes+=1

game(grid,82-empty_boxes,alpha)