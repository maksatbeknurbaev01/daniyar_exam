class MobilePhone:
    brand = ''
    model = ''
    cost = 10000.00
    is_two_sim = True
    def print_mobile(self):
        print(self.brand, self.model, self.cost, self.is_two_sim)


phone1 = MobilePhone()
phone1.brand = 'Apple'
phone1.model = 'Smartphone'
phone1.cost = 56000.00
phone1.is_two_sim = True
phone2 = MobilePhone()
phone2.brand = 'Nokia'
phone2.model = 'Cellphone'
phone2.cost = 2000.00
phone2.is_two_sim = False
phone3 = MobilePhone()
phone3.brand = 'Samsung'
phone3.model = 'Smartphone'
phone3.cost = 45000.00
phone3.is_two_sim = True
phone4 = MobilePhone()
phone4.brand = 'Sony'
phone4.model = 'Smartphone'
phone4.cost = 56000.00
phone4.is_two_sim = True
phone5 = MobilePhone()
phone5.brand = 'Xiaomi'
phone5.model = 'Smartphone'
phone5.cost = 12500.00
phone5.is_two_sim = True
phone6 = MobilePhone()
phone6.brand = 'Huawei'
phone6.model = 'Smartphone'
phone6.cost = 21000.00
phone6.is_two_sim = True
phone7 = MobilePhone()
phone7.brand = 'Motorola'
phone7.model = 'Cellphone'
phone7.cost = 3200.00
phone7.is_two_sim = True
print(phone1.print_mobile())
print(phone2.print_mobile())
print(phone3.print_mobile())
print(phone4.print_mobile())
print(phone5.print_mobile())
print(phone6.print_mobile())
print(phone7.print_mobile())





