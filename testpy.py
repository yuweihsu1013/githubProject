# import random
# c = 10
# while c <=10 and c >=0:
#     print('目前血量','*'*c)
#     print('zombie來了，配對決勝負!')
#     z = random.randint(1,6)
#     game = int(input('請輸入數字1~6: '))
#     if game == z:
#         print('配中了，沒事~')
#     else:
#         print('配錯了，扣一命!')
#         c -= 1
#     while c == 0:
#         print('game over!')
#         c -=1


wd = 'Programming'
print('字串: ', wd)
print('結合其他字串: ')
print('Python ' + wd[:7])
opr = '-' *5
print(opr)
lst=['one', 'two', 'three']
print(' '.join(lst))
opr *=4
print(opr)
