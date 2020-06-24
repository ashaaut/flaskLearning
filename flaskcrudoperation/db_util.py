import pymysql
connection  = None

CREATE_TABLE_QUERY = '''create table product_info(pid INT NOT NULL AUTO_INCREMENT,
                                    name varchar(100) NOT NULL, 
                                    price float, 
                                    vendor VARCHAR(100) NOT NULL, 
                                    category VARCHAR(100), PRIMARY KEY(pid))'''

def get_connection():
    global connection
    if connection==None:
        connection = pymysql.connect("localhost", "root", "Zoom@123", "product")
    return connection


def create_product_table():
    connection = get_connection()
    comm_channel = connection.cursor()
    comm_channel.execute(CREATE_TABLE_QUERY)
    connection.commit()


