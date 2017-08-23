def multiReverse(li):
    if type(li) == type([]):
        li.reverse()
        for ele in li:
            multiReverse(ele)
    return(li)
    

def question2(num):
    for i in range(num):
        i += 1
        if i % 15 == 0:
            print(i)
            continue
        if i % 3 == 0 or i % 5 == 0:
            continue
        print(i)

testlist = [1, [12, 3, [4, [5, 16]]]]
if __name__ == '__main__':

    print('question1')
    print(multiReverse(testlist))
    print('question2')
    question2(15)
