def solution(id_pw, db):
    answer = 'fail'

    for i in range(len(db)):
        if (id_pw[0] == db[i][0]) and (id_pw[1] == db[i][1]):
            answer = 'login'
        elif (id_pw[1] != db[i][1]) and (id_pw[0] == db[i][0]):
            answer = 'wrong pw'
        # elif (id_pw[0] != db[i][0]):
        #     answer = 'fail'
        else:
            answer = answer
    return answer