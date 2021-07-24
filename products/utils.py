from accounts.models import Account
from .models import Product

def get_category_product_name(data):
    my_list = []
    for item in range(len(data)):
        item["created_by"] = Account.objects.get(id=data["created_by"])
        item["category"] = Product.objects.get(id=data["category"])
        my_list.append(item)
    return my_list
