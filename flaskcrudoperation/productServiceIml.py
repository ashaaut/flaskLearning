from flaskcrudoperation.productservice import ProductService
from flaskcrudoperation.db_util import get_connection
from flaskcrudoperation.productinfo import Product


class ProductServiceImpl(ProductService):

    def add_product(self,prod):
        connection = get_connection()
        print(connection)
        comm_channel = connection.cursor()

        INSERT_QUERY = "INSERT into product_info values({},\'{}\',{}, \'{}\',\'{}\')".format(prod.product_id,
                                                                                             prod.product_name,
                                                                                             prod.product_price,
                                                                                             prod.product_vendor,
                                                                                             prod.product_category)

        print(INSERT_QUERY)
        comm_channel.execute(INSERT_QUERY)
        connection.commit()
        print("Product is Added")

    def get_all_products(self):
        connection = get_connection()
        comm_channel = connection.cursor()
        FETCH_ALL_QUERY = "SELECT * from product_info"
        comm_channel.execute(FETCH_ALL_QUERY)
        products = comm_channel.fetchall()
        list_of_products = []
        for row in products:
            product = Product(id=row[0],pname=row[1], pprice=row[2], pven=row[3], pcategory=row[4])
            list_of_products.append(product)
        return list_of_products


    def get_single_product(self,id):
        connection = get_connection()
        comm_channel = connection.cursor()
        FETCH_QUERY = "select * from product_info where pid = "+str(id)
        comm_channel.execute(FETCH_QUERY)
        product = comm_channel.fetchone()
        return product

    def update_product(self,prod):
        connection = get_connection()
        comm_channel = connection.cursor()
        dbproduct = self.get_single_product(prod.product_id)
        if dbproduct:
            UPDATE_QUERY = '''UPDATE product_info SET name =\'{}\',price = {}, vendor = \'{}\', category = \'{}\' where pid = {}
            '''.format(prod.product_name, prod.product_price, prod.product_vendor, prod.product_category, prod.product_id)
            comm_channel.execute(UPDATE_QUERY)
            connection.commit()
            print("Product Updated Successfully")
        else:
            print("Product is not available")

    def delete_product(self,id):
        connection = get_connection()
        comm_channel = connection.cursor()
        dbproduct = self.get_single_product(id)
        if dbproduct:
            DELETE_QUERY = "delete from product_info where pid = " + str(id)
            comm_channel.execute(DELETE_QUERY)
            connection.commit()
            print("Product is deleted")
        else:
            print("Product is not available")





# implobj = ProductServiceImpl()
# implobj.add_product(Product(id=2, pname= 'Samsung', pprice=10000, pven="Flipkart", pcategory="Electronics"))
# s = implobj.get_all_products()
# print(s)