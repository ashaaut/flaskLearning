
class Product:
    def __init__(self, id, pname, pprice, pven, pcategory):
        self.product_id = id
        self.product_name = pname
        self.product_price = pprice
        self.product_vendor = pven
        self.product_category  = pcategory

    def __str__(self):
        return "ID :{}, Name: {} , Price : {}, Vendor:{}, Category:{}".format(self.product_id, self.product_name,
                                                                              self.product_price,
                                                                              self.product_vendor,
                                                                              self.product_category)

    def __repr__(self):
        return str(self)


# obj = Product(1,"Laptop",25000,"Amazon", "Electronics")
# obj1 = Product(2,"Mobile",5000,"Amazon", "Electronics")
# list_of_product = [obj1,obj]
# print(obj1)
# print(list_of_product)
