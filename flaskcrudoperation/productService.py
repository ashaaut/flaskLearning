from abc import ABC,abstractmethod

class productService(ABC):
    
    @abstractmethod
    def add_product(self,prod):
        pass
    
    
    @abstractmethod
    def get_all_product(self):
        pass
    
    
    @abstractmethod
    def get_single_product(self,id):
        pass
    
    
    @abstractmethod
    def delete_product(self,id):
        pass
    
    
    @abstractmethod
    def update_product(self,prod):
        pass