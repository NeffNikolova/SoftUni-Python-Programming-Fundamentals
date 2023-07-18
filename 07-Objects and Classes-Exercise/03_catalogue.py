class Catalogue:

    products = []

    def __init__(self, name:str):
        self.name = name

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter:str):
        filtered_products = [product for product in self.products if product[0] == first_letter]
        return filtered_products

    def __repr__(self):
        output = f"Items in the {self.name} catalogue:\n"
        output += '\n'.join(sorted(self.products))
        return output

#
# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)
#
