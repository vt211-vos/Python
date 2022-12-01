class Shop:
    def __init__(self, name, type, units = 0):
        self.number_of_units  = units
        self.shop_name = name
        self.shop_type = type
    def describe_shop(self):
        return f"Name=>{self.shop_name}  Type=>{self.shop_type}"
    def open_shop(self):
        return f"{self.shop_name} is open"
    def set_number_of_units(self, numb):
        self.number_of_units = numb
    def increment_number_of_units(self):
        self.number_of_units += 1
