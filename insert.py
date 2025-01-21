from sqlmodel import Session, create_engine
from models import Menu, Order  # Replace with your actual file path

# Connect to the PostgreSQL database
engine = create_engine("postgresql://postgres:fidele95@localhost:5432/resturantdb")

# Create 30 sample menus
menus = [
    Menu(name="Spaghetti Bolognese", ingredients="Pasta, Tomato Sauce, Ground Beef", ratings=4.5,
         description="Classic Italian dish", target_age_group="Adults"),
    Menu(name="Chicken Nuggets", ingredients="Chicken, Bread Crumbs, Spices", ratings=4.0,
         description="Kids' favorite meal", target_age_group="Children"),
    Menu(name="Caesar Salad", ingredients="Lettuce, Croutons, Parmesan, Caesar Dressing", ratings=4.2,
         description="Refreshing salad with a creamy dressing", target_age_group="All"),
    Menu(name="Margherita Pizza", ingredients="Tomato, Mozzarella, Basil", ratings=4.8,
         description="Traditional Italian pizza", target_age_group="All"),
    Menu(name="Grilled Salmon", ingredients="Salmon, Lemon, Dill, Olive Oil", ratings=4.7,
         description="Perfectly grilled salmon fillet", target_age_group="Adults"),
    Menu(name="Beef Burger", ingredients="Beef Patty, Lettuce, Tomato, Cheese, Bun", ratings=4.5,
         description="Juicy burger with a beef patty", target_age_group="All"),
    Menu(name="Vegan Burger", ingredients="Plant-based Patty, Lettuce, Tomato, Vegan Bun", ratings=4.3,
         description="Healthy and delicious vegan option", target_age_group="Adults"),
    Menu(name="Mac and Cheese", ingredients="Pasta, Cheese Sauce, Butter", ratings=4.1,
         description="Comfort food for all ages", target_age_group="Children"),
    Menu(name="Chicken Alfredo", ingredients="Pasta, Alfredo Sauce, Grilled Chicken", ratings=4.6,
         description="Rich and creamy pasta dish", target_age_group="Adults"),
    Menu(name="Vegetable Stir-fry", ingredients="Broccoli, Carrots, Bell Peppers, Soy Sauce", ratings=4.4,
         description="Healthy stir-fried vegetables", target_age_group="All"),
    Menu(name="Fish Tacos", ingredients="Fish, Tortilla, Lime, Cabbage, Sauce", ratings=4.5,
         description="Crispy fish tacos with tangy sauce", target_age_group="All"),
    Menu(name="Pad Thai", ingredients="Rice Noodles, Tofu, Shrimp, Tamarind Sauce", ratings=4.7,
         description="Thai stir-fried noodles", target_age_group="Adults"),
    Menu(name="Clam Chowder", ingredients="Clams, Potatoes, Cream, Bacon", ratings=4.3,
         description="Creamy New England soup", target_age_group="Adults"),
    Menu(name="Sushi Platter", ingredients="Rice, Fish, Seaweed, Soy Sauce", ratings=4.8,
         description="Assorted sushi rolls", target_age_group="All"),
    Menu(name="Fried Chicken", ingredients="Chicken, Flour, Spices, Oil", ratings=4.5,
         description="Crispy and flavorful fried chicken", target_age_group="All"),
    Menu(name="Ramen", ingredients="Noodles, Broth, Pork, Egg, Seaweed", ratings=4.6,
         description="Japanese noodle soup", target_age_group="All"),
    Menu(name="Pancakes", ingredients="Flour, Eggs, Milk, Syrup", ratings=4.4,
         description="Fluffy breakfast pancakes", target_age_group="All"),
    Menu(name="French Fries", ingredients="Potatoes, Salt, Oil", ratings=4.2,
         description="Crispy and golden fries", target_age_group="All"),
    Menu(name="Ice Cream Sundae", ingredients="Ice Cream, Syrup, Whipped Cream, Nuts", ratings=4.7,
         description="Sweet dessert treat", target_age_group="All"),
    Menu(name="Tandoori Chicken", ingredients="Chicken, Yogurt, Spices", ratings=4.8,
         description="Indian-style grilled chicken", target_age_group="Adults"),
    Menu(name="Chocolate Cake", ingredients="Flour, Cocoa, Sugar, Butter", ratings=4.9,
         description="Rich and moist chocolate cake", target_age_group="All"),
    Menu(name="Cheeseburger", ingredients="Beef Patty, Cheese, Lettuce, Tomato, Bun", ratings=4.6,
         description="Classic cheeseburger with toppings", target_age_group="All"),
    Menu(name="BBQ Ribs", ingredients="Pork Ribs, BBQ Sauce, Spices", ratings=4.8,
         description="Tender and smoky BBQ ribs", target_age_group="Adults"),
    Menu(name="Falafel Wrap", ingredients="Falafel, Pita, Vegetables, Sauce", ratings=4.3,
         description="Middle Eastern wrap with falafel", target_age_group="Adults"),
    Menu(name="Greek Salad", ingredients="Tomato, Cucumber, Feta, Olives, Dressing", ratings=4.4,
         description="Mediterranean salad", target_age_group="All"),
    Menu(name="Stuffed Bell Peppers", ingredients="Bell Peppers, Rice, Ground Beef, Cheese", ratings=4.5,
         description="Baked stuffed peppers", target_age_group="Adults"),
    Menu(name="Lobster Bisque", ingredients="Lobster, Cream, Butter, Sherry", ratings=4.7,
         description="Rich seafood soup", target_age_group="Adults"),
    Menu(name="Apple Pie", ingredients="Apples, Sugar, Cinnamon, Pastry", ratings=4.9,
         description="Classic dessert pie", target_age_group="All"),
    Menu(name="Curry Goat", ingredients="Goat, Spices, Coconut Milk, Potatoes", ratings=4.8,
         description="Caribbean-style curry", target_age_group="Adults"),
    Menu(name="Dim Sum Platter", ingredients="Dumplings, Spring Rolls, Bao Buns", ratings=4.6,
         description="Assorted Chinese appetizers", target_age_group="All"),
]

# Insert menus and some orders
with Session(engine) as session:
    session.add_all(menus)
    session.commit()

    # Create sample orders
    orders = [
        Order(menu_id=menus[0].id, quantity=2),
        Order(menu_id=menus[5].id, quantity=3),
        Order(menu_id=menus[10].id, quantity=1),
        Order(menu_id=menus[15].id, quantity=4),
        Order(menu_id=menus[20].id, quantity=2),
    ]
    session.add_all(orders)
    session.commit()
