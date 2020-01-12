import pymysql



def show_animals(conn):
    cursor = conn.cursor()
    cursor.execute("select * from Animals")
    for row in cursor:
        print(row[0])


def addAnimal(conn):
    cursor = conn.cursor()
    animal={}
    animal["name"] = input('Please Type Animal Name:')
    animal["age"] = input('Please Type Animal Age:')
    animal["legs"] = input('Please Type Animal legs:')
    animal["color"] = input('Please Type Animal color:')
    cursor.execute("INSERT INTO Animals (name, age, legs, color) VALUES ('%s', '%d', '%d', '%s');" % (animal["name"], animal["age"], animal["legs"], animal["color"]))


my_connection = pymysql.connect(host='127.0.0.1',port=3306, user='root', password='my-secret-pw', db='ZOO', autocommit=True)
addAnimal(my_connection)
my_connection.close()


