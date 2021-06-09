y = 0
n = 5
end = ''
candy = [1,2,3,4,5]
def try_y(y):
    if y == len(candy):
        end_y = 0
    else:
        end_y = y
    return end_y
for i in candy:
    x = i//3
    candy[y] = x
    one = candy[y-1]
    candy[y-1] = one + x
    two = candy[try_y(y)]
    candy[try_y(y)] = two + x
    y += 1
for i in candy:
    end += str(i)
print(end)