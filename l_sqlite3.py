import sqlite3
con = sqlite3.connect('other/sales.db')
# cur = con.cursor()
# cur.execute('CREATE TABLE category(id primary key, sort, name)')
# cur.execute('INSERT INTO category VALUES (1,1,"computer")')
# cur.execute('select * from catagory')
# print(cur.fetchall())
con.execute('create table book(id primary key, price, name)')

# # 插入
books = [('021', 25, 'apple'), ('022', 30, 'book'), ('033', 66, 'come')]
cur = con.cursor()
cur.execute('insert into book(id,price,name) values ("001",33,"ditto")')
cur.execute('insert into book(id,price,name) values(?,?,?)',
            ('002', 28, 'eye'))
cur.executemany('insert into book(id,price,name) values (?,?,?)', books)
# cur.execute('update book set price=? where name=?', (25, 'book'))
# n = cur.execute('delete from book where price=?', (25,))
# print('删除了', n.rowcount, '行记录')

cur.execute('select id,price,name from book')
for row in cur:
    print(row)
con.commit()
cur.close()
con.close()
