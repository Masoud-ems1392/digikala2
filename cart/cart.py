from shop.models import Product, Profile

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.request = request

        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id = self.request.user.id)
            db_cart = str(self.cart).replace('\'','\"')

            current_user.update(old_cart=str(db_cart))

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id = self.request.user.id)
            db_cart = str(self.cart).replace('\'','\"')

            current_user.update(old_cart=str(db_cart))
         
    def __len__(self):    
        return len(self.cart)  


    def get_prods(self):
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)
        return products 

    def get_quants(self):
        quantities = self.cart
        return quantities

    def get_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        total = 0

        for key,value in self.cart.items():
            key = int(key)
            for product in products:    
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price*value)
                    else:
                        totla = total + (product.price *value)
        return total    

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        ourcart = self.cart   # {'2':4, '3':5}
        ourcart[product_id] = product_qty
        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id = self.request.user.id)
            db_cart = str(self.cart).replace('\'','\"')

            current_user.update(old_cart=str(db_cart))
        alaki = self.cart
        return alaki

    def delete(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id = self.request.user.id)
            db_cart = str(self.cart).replace('\'','\"')

            current_user.update(old_cart=str(db_cart))
            

