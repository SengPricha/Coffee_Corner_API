from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.mount("/img", StaticFiles(directory="img"), name="img")
# Define product model
class Product(BaseModel):
    id: int
    title: str
    image: str
    price: float
    description: str
    category: str

# Sample in-memory data
products = [
    Product(id=1,
            title="Matcha Coconut Cream",
            image="/img/Matcha Coconut Cream.png",
            price=1.89,
            description="Smooth matcha blended with creamy coconut for a rich and refreshing drink (For ref only)",             
            category="Popular"
            ),
    Product(id=2,
             title="Passion Corner",
             image="/img/Passion Corner.png",
             price=1.89,
             description="The special creation and a perfect drink on a hot summer day and even at parties (For ref only)",
             category="Popular"
            ),
    Product(id=3,
             title="Salt Coffee",
             image="/img/Salt Coffee.png",
             price=1.89,
             description="A bold coffee topped with a unique salted foam layer, creating a perfect balance of savory and sweet (For ref only)",
             category="Popular"
            ),
    Product(id=4,
             title="Tpea Dong",
             image="/img/Tpea Dong.png",
             price=2.59,
             description="a refreshing and unique beverag ce thatombines the rich flavors of Paste of fermented rice (eaten as a dessert) with coconut",
             category="Popular"
            ),
    Product(id=5,
             title="Chocolate Coconut Cream",
             image="/img/Chocolate Coconut Cream.png",
             price=1.89,
             description="Decadent chocolate combined with creamy coconut for a deliciously smooth drink (For ref only)",
             category="Popular"
            ),
    Product(id=6,
             title="Milk Tea Corner",
             image="/img/Milk Tea Corner.png",
             price=3.19,
             description="Make your tea time creamy and sweet with milk tea",
             category="Popular"
            ),
    Product(id=7,
             title="Coffee Coco",
             image="/img/Coffee Coco.png",
             price=1.89,
             description="a refreshing and unique beverage that combines the rich flavors of coffee with the tropical taste of coconut",
             category="New Drinks"
            ),
    Product(id=8,
             title="Matcha Chocolate",
             image="/img/Matcha Chocolate.png",
             price=2.09,
             description="a delightful fusion of creamy chocolate and the earthy, slightly bitter flavor of matcha, a finely ground green tea powder",
             category="New Drinks"
            ),
    Product(id=9,
             title="Tpea Dong",
             image="/img/Tpea Dong.png",
             price=2.59,
             description="a refreshing and unique beverag ce thatombines the rich flavors of Paste of fermented rice (eaten as a dessert) with coconut",
             category="New Drinks"
            ),
    Product(id=10,
             title="Matcha Tiramisu",
             image="/img/Matcha Tiramisu.png",
             price=2.69,
             description="Tiramisu drink (For ref only)",
             category="New Drinks"
            ),
    Product(id=11,
             title="Cafe Tiramisu",
             image="/img/Cafe Tiramisu.png",
             price=2.49,
             description="Tiramisu drink (For ref only)",
             category="New Drinks"
            ),
    Product(id=12,
             title="Cafe Charcoal",
             image="/img/Cafe Charcoal.png",
             price=2.09,
             description="Refreshing Drink (For ref only)",
             category="New Drinks"
            ),
    Product(id=13,
             title="Chocolate Coconut Cream",
             image="/img/Chocolate Coconut Cream.png",
             price=1.89,
             description="Decadent chocolate combined with creamy coconut for a deliciously smooth drink (For ref only)",
             category="New Drinks"
            ),
    Product(id=14,
            title="Matcha Coconut Cream",
            image="/img/Matcha Coconut Cream.png",
            price=1.89,
            description="Smooth matcha blended with creamy coconut for a rich and refreshing drink (For ref only)",             
            category="New Drinks"
            ),
    Product(id=15,
             title="Salt Coffee",
             image="/img/Salt Coffee.png",
             price=1.89,
             description="A bold coffee topped with a unique salted foam layer, creating a perfect balance of savory and sweet (For ref only)",
             category="New Drinks"
            ),
     Product(id=16,
             title="Passion Corner",
             image="/img/Passion Corner.png",
             price=1.89,
             description="The special creation and a perfect drink on a hot summer day and even at parties (For ref only)",
             category="Corner Signature"
            ),
    Product(id=17,
             title="Milk Tea Corner",
             image="/img/Milk Tea Corner.png",
             price=3.19,
             description="Make your tea time creamy and sweet with milk tea",
             category="Corner Signature"
            ), 
    Product(id=18,
             title="Coffee Corner",
             image="/img/Coffee Corner.png",
             price=1.89,
             description="The most signature items in store and also the best coffee",
             category="Corner Signature"
            ), 
    Product(id=19,
             title="Strawberry Frappe",
             image="/img/Strawberry Frappe.png",
             price=3.26,
             description="A healthy and refreshing drink made of fresh strawberry blended with milk (For ref only)",
             category="Frappe"
            ), 
    Product(id=20,
             title="Blueberry Frappe",
             image="/img/Blueberry Frappe.png",
             price=3.26,
             description="A refreshing blended drink made with blueberries, milk, and ice",
             category="Frappe"
            ),   
    Product(id=21,
             title="Passion Frappe",
             image="/img/Passion Frappe.png",
             price=3.26,
             description="This drink tastes incredibly good, and is packed with vitamins! (For ref only)",
             category="Frappe"
            ), 
    Product(id=22,
             title="Coconut Frappe",
             image="/img/Coconut Frappe.png",
             price=3.26,
             description="A healthy and refreshing drink made of fresh coconut blended with milk (For ref only)",
             category="Frappe"
            ),
    Product(id=23,
             title="Raspberry Frappe",
             image="/img/Raspberry Frappe.png",
             price=3.26,
             description="Refreshing raspberry drink blended into a cool, fruity frappe (For ref only)",
             category="Frappe"
            ),
    Product(id=24,
             title="Vanilla Frappe",
             image="/img/Vanilla Frappe.png",
             price=3.26,
             description="A thick vanilla milkshake, just not quite as sweet (For ref only)",
             category="Frappe"
            ),  
    Product(id=25,
             title="Chocolate Frappe",
             image="/img/Chocolate Frappe.png",
             price=3.26,
             description="A foamy, creamy delicious drink that combines with milk, chocolate powder, and ice blend in together (For ref only)",
             category="Frappe"
            ), 
    Product(id=26,
             title="Mocha Frappe",
             image="/img/Mocha Frappe.png",
             price=3.26,
             description="Blended mocha and milk to the smooth consistency (For ref only)",
             category="Frappe"
            ),
     Product(id=27,
             title="Coffee Frappe",
             image="/img/Coffee Frappe.png",
             price=3.26,
             description="A summer favorite drink that blend with milk, ice and coffee (For ref only)",
             category="Frappe"
            ),
     Product(id=28,
             title="Iced Latte",
             image="/img/Iced Latte.png",
             price=1.89,
             description="A coffee based drink made primarily from espresso and steamed milk (For ref only)",
             category="Iced Beverages"
            ),
     Product(id=29,
             title="Iced Mocha",
             image="/img/Iced Mocha.png",
             price=1.89,
             description="Drink to keep you awake (For ref only)",
             category="Iced Beverages"
            ),
     Product(id=30,
             title="Iced Caramel Latte",
             image="/img/Iced Caramel Latte.png",
             price=1.89,
             description="The combination of espresso with caramel syrup and steamed milk on top (For ref only)",
             category="Iced Beverages"
            ),
     Product(id=31,
             title="Iced Americano",
             image="/img/Iced Americano.png",
             price=1.89,
             description="Iced Americano tastes like a slightly diluted espresso and much colder due to ice (For ref only)",
             category="Iced Beverages"
            ),
     Product(id=32,
             title="Iced Chocolate",
             image="/img/Iced Chocolate.png",
             price=1.89,
             description="A perfect balance between chocolate and the sweetness of milk (For ref only)",
             category="Iced Beverages"
            ),
     Product(id=33,
             title="Iced Matcha Latte",
             image="/img/Iced Matcha Latte.png",
             price=1.89,
             description="A refreshing drink made from Japanese green tea powder hot water and milk (For ref only)",
             category="Iced Beverages"
            ),
     Product(id=34,
             title="Iced Matcha Espresso",
             image="/img/Iced Matcha Espresso.png",
             price=2.19,
             description="A refreshing drink made from Japanese green tea powder mix with espresso coffee and milk",
             category="Iced Beverages"
            ),
     Product(id=35,
             title="Iced Matcha Strawberry",
             image="/img/Iced Matcha Strawberry.png",
             price=2.19,
             description="A refreshing drink made from Japanese green tea powder mix with strawberry powder and milk",
             category="Iced Beverages"
            ),
     Product(id=36,
             title="Hot Americano",
             image="/img/Hot Americano.png",
             price=1.89,
             description="Is an espresso based drink designed to resemble coffee brewed in a drip filter (For ref only)",
             category="Hot Beverages"
            ),
     Product(id=37,
             title="Hot Latte",
             image="/img/Hot Latte.png",
             price=1.89,
             description="A concoction of hard brewed espresso with sweetened milk and milk foam to top it up (For ref only)",
             category="Hot Beverages"
            ),
      Product(id=38,
             title="Hot Mocha",
             image="/img/Hot Mocha.png",
             price=1.89,
             description="It combines cold brew with milk and chocolate flavoring (For ref only)",
             category="Hot Beverages"
            ),
      Product(id=39,
             title="Hot Chocolate",
             image="/img/Hot Chocolate.png",
             price=1.89,
             description="A velvety and indulgent treat made with rich cocoa and steaming milk creating a comforting beverage that's both soothing and utterly delicious (For ref only)",
             category="Hot Beverages"
            ),
     Product(id=40,
             title="Hot Cappuccino",
             image="/img/Hot Cappuccino.png",
             price=1.89,
             description="A rich and velvety coffee with a strong espresso flavor complemented by the frothy texture of the milk foam (For ref only)",
             category="Hot Beverages"
            ),
     Product(id=41,
             title="Brown Sugar Milk Tea",
             image="/img/Brown Sugar Milk Tea.png",
             price=1.99,
             description="Brown sugar milk tea is an iced black tea drink with brown sugar and milk (For ref only)",
             category="Milk Tea"
            ),
     Product(id=42,
             title="Strawberry Cream Milk Tea",
             image="/img/Strawberry Cream Milk Tea.png",
             price=1.89,
             description="A perfect drink on a hot summer day and even at parties (For ref only)",
             category="Milk Tea"
            ),
     Product(id=43,
             title="Honey Pearl Milk Tea",
             image="/img/Honey Pearl Milk Tea.png",
             price=1.89,
             description="This classic milk tea is sweet creamy and delicious with chewy pearl (For ref only)",
             category="Milk Tea"
            ),
      Product(id=44,
             title="Watermelon Soda",
             image="/img/Watermelon Soda.png",
             price=1.89,
             description="A fresh watermelon mixing with soda water is the best drink to keep yourself refreshing",
             category="Soda"
            ),
      Product(id=45,
             title="Mint Mojito Soda",
             image="/img/Mint Mojito Soda.png",
             price=1.89,
             description="Mint mixing with soda water and lemon is the signature drink to keep you awake and refreshing also",
             category="Soda"
            ),
      Product(id=46,
             title="Passion Soda",
             image="/img/Passion Soda.png",
             price=1.89,
             description="The sourness from passion mixing with soda water to refresh your whole day",
             category="Soda"
            ),
     Product(id=47,
             title="Strawberry Soda",
             image="/img/Strawberry Soda.png",
             price=1.89,
             description="The sourness from strawberry mixing with soda water to refresh your whole day",
             category="Soda"
            ),
     Product(id=48,
             title="Blue Curacao Soda",
             image="/img/Blue Curacao Soda.png",
             price=1.89,
             description="A perfect drink on a hot summer day and even at parties (For ref only)",
             category="Soda"
            ),
]

# Return full URL for image
def add_full_image_url(product: Product, base_url: str) -> Product:
    product_copy = product.copy()
    product_copy.image = f"{base_url.rstrip('/')}{product.image}"
    return product_copy

# Get all products
@app.get("/products", response_model=List[Product])
def get_products(request: Request):
    base_url = str(request.base_url)
    return [add_full_image_url(p, base_url) for p in products]

# Get single product by ID
@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int, request: Request):
    base_url = str(request.base_url)
    for product in products:
        if product.id == product_id:
            return add_full_image_url(product, base_url)
    return {"error": "Product not found"}

# Create a new product
@app.post("/products", response_model=Product)
def create_product(product: Product, request: Request):
    base_url = str(request.base_url)
    products.append(product)
    return add_full_image_url(product, base_url)