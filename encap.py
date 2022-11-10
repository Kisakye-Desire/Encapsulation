class ServiceProvider:
    email="fotogenixs@gmail.com"
    discount=0.02
    
    def __init__(self,name,phone):
        #Making my method private(self._name=name,self._phone=phone)
        self.__name= name
        self.__phone= phone
     
     
     #Regular methods   
    def get_name(self):
        return self.name
    
    #Defining class methods
    @classmethod
    def isuing_invoice(cls):
        return f"Here is the invoice"
    
    #Inheritance creating baby service provider
class JuniorServiceProvider(ServiceProvider):
        def __init__(self,name,phone,location):
            
            #For inheritance to occur use the super class
            super().__init__(name,phone,location)
            self.location = location
    
    
    
service1=ServiceProvider("Photogenix", 708898424)
service2=ServiceProvider("Desire",752905559)

#creating junior service provider
service3=JuniorServiceProvider("UNRA",782533577,"Kololo")

print(service1.email)

#Update discount for service provider 1
service1.discount=0.30
print(service1.discount)
print(service2.discount)
print(service3.discount)

#print(ServiceProvider(service1))

#Updating email details.
ServiceProvider.email="dhisayar@gmail.com"

print(service1.email)    
    
    
    
    
    
    
