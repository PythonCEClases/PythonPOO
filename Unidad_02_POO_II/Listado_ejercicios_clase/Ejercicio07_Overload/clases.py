class Pedido:
    def __init__(self, id, pedido_date, customer, products):
        self.id = id
        self.pedido_date = pedido_date
        self.customer = customer
        self.products = products

    def __str__(self):
        return f"pedido: {self.id} - Customer: {self.customer} - Nº Products: {len(self.products)}"

    def __add__(self, other_product):
        self.products.append(other_product)

    def __sub__(self, product):
        self.products.remove(product)

    def __len__(self):
        return len(self.products)

    def __iadd__(self, otro_pedido):
        for p in otro_pedido.products:
            self.products.append(p)
        return self

    def __bool__(self):
        return len(self.products) > 0
