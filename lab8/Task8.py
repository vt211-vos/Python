from shop import Shop

class Discount(Shop):
    def __init__(self, arr):
        self.discount_products = arr

    def get_discounts_ptoducts(self):
        print(self.discount_products)
#    A)
print("a)")
store = Shop("АТБ","Продуктовий")
print(store.shop_name)
print(store.shop_type)
store.open_shop()
store.describe_shop()

store2 = Shop("Сільпо", 'Продутовий')
store3 = Shop("Епіцентр", 'Буд. матеріали')
#    B)
print("\nb)")
store.describe_shop()
store2.describe_shop()
store3.describe_shop()

#    C)
print("\nc)")
store = Shop("АТБ","Продуктовий")
print(store.number_of_units)
store.number_of_units = 5
print(store.number_of_units)

#    D)
print("\nd)")
store.set_number_of_units(7)
print(store.number_of_units)
store.increment_number_of_units()
print(store.number_of_units)

#    E)
print("\ne)")
store_discount = Discount(["Apple","Banana","Rise"])
store_discount.get_discounts_ptoducts()

#    F)
print("\nf)")
all_store = Shop("Сільпо", 'Продутовий')
all_store.describe_shop()