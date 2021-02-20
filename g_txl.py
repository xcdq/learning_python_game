# 通讯录
import sqlite3


def opendb():
    conn = sqlite3.connect('db/mydb.db')
    cur = conn.execute(
        'create table if not exists tongxinlu( usernum integer primary key,username varchar(128), passworld varchar(128),address varchar(128),telnum varchar(128))')
    return cur, conn


def showalldb():
    print('-----------数据-----------')
    hel = opendb()
    cur = hel[1].cursor()
    cur.execute('select * from tongxinlu')
    res = cur.fetchall()
    for line in res:
        # for h in line:
        #     print(h,)
        print(line)
    cur.close()


def into():
    usernum = input('学号：')
    username1 = input('姓名：')
    passworld1 = input('密码：')
    address1 = input('地址：')
    telnum1 = input('电话：')
    return usernum, username1, passworld1, address1, telnum1


def adddb():
    print('-----welcome')
    person = into()
    hel = opendb()
    hel[1].execute(
        'insert into tongxinlu(usernum,username,passworld,address,telnum) values (?,?,?,?,?)', (person[0], person[1], person[2], person[3], person[4]))
    hel[1].commit()
    print('-----ok-----')
    showalldb()
    hel[1].close()


def deldb():
    print('------del')
    delchoice = input('输入学号：')
    hel = opendb()
    hel[1].execute('delete from tongxinlu where usernum ='+delchoice)
    hel[1].commit()
    print('-----del  ok-----')
    hel[1].close()


def alter():
    print('-----update-----')
    changechoice = input('学号：')
    hel = opendb()
    person = into()
    hel[1].execute(
        'update tongxinlu set usernum=?,username=?,passworld=?,address=?,telnum=? where usernum='+changechoice, person)
    hel[1].commit()
    showalldb()
    hel[1].close()


def searchdb():
    print('-------search')
    choice = input('学号：')
    hel = opendb()
    cur = hel[1].cursor()
    cur.execute('select * from tongxinlu where usernum='+choice)
    hel[1].commit()
    for row in cur:
        print(row)
    cur.close()
    hel[1].close()


def conti(a):
    choice = input('y/n: ')
    if choice == 'y':
        a = 1
    else:
        a = 0
    return a


if __name__ == '__main__':
    flag = 1
    while flag:
        print('---start')

        choice = input('(add,del,update,search): \n')
        if choice == 'add':
            adddb()
            flag = conti(flag)
        elif choice == 'del':
            deldb()
            flag = conti(flag)
        elif choice == 'update':
            alter()
            flag = conti(flag)
        elif choice == 'search':
            searchdb()
            flag = conti(flag)
        else:
            print('error')
