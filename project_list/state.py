from unicodedata import category

import reflex as rx
from project_list.classify import classify

class InputState(rx.State):
    product: str = ""
    product_list: list[dict] = []

    marketplace: str = ""
    location: str = ""

    is_loading: bool = False

    next_id: int = 0

    @rx.var
    def product_valid(self):
        return bool(self.product.strip())  # Está vacío el input??
    def set_product(self, value: str):
        self.product = value

    def marketplace_valid(self):
        return bool(self.marketplace.strip())
    def set_marketplace(self, value: str):
        self.marketplace = value

    def location_valid(self):
        return bool(self.location.strip())
    def set_location(self, value: str):
        self.location = value

    def save(self):
        print("Saved")
        if self.marketplace_valid and self.location_valid:
            self.update_product_list()

    def remove(self, product_id: int):
        print("Deleted")

        for product in self.product_list:
            if product_id == product["id"]:
                self.product_list.remove(product)


    def classify_product(self):
        self.is_loading = True
        print("Loading: ", self.is_loading)

        if self.product_valid and self.marketplace_valid and self.location_valid:
            classify_result = classify(self.product, self.marketplace, self.location)

            classify_result["id"] = self.next_id
            self.next_id += 1

            self.product_list.append(classify_result)
            self.product_list.sort(key=lambda x: float(x["Distancia"]))
            print(self.product_list)

            self.product = ""

        self.is_loading = False
        print("Loading: ", self.is_loading)

    def update_product_list(self):
        self.is_loading = True
        print("Loading: ", self.is_loading)

        updated_list = []

        for product in self.product_list:
            classify_result = classify(product['Producto'], self.marketplace, self.location)
            print(f"Clasificando producto: {product['Producto']} en {self.marketplace} - {self.location}")
            print(f"Resultado de classify: {classify_result}")

            if classify_result:
                product.update(classify_result)

            updated_list.append(product)

        updated_list.sort(key=lambda x: float(x["Distancia"]))

        if updated_list != self.product_list:
            self.product_list = updated_list
            print("Lista de productos actualizada: ", self.product_list)

        self.is_loading = False
        print("Loading: ", self.is_loading)
