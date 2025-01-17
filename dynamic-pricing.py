import random

class DynamicPricingSystem:
    def __init__(self):
        # Initialize product details
        self.products = {
            "product_1": {"base_price": 100, "inventory": 50, "demand": 0.8},
            "product_2": {"base_price": 200, "inventory": 20, "demand": 0.4},
            "product_3": {"base_price": 300, "inventory": 10, "demand": 0.6},
        }
        self.competitor_prices = {
            "product_1": 95,
            "product_2": 190,
            "product_3": 310,
        }

    def adjust_price(self, product_name):
        """Adjust the price of a product dynamically based on demand, inventory, and competitor prices."""
        product = self.products[product_name]
        base_price = product["base_price"]
        inventory = product["inventory"]
        demand = product["demand"]
        competitor_price = self.competitor_prices[product_name]

        # Adjust price based on demand (higher demand -> higher price)
        if demand > 0.7:
            demand_factor = 1.1
        elif demand > 0.5:
            demand_factor = 1.05
        else:
            demand_factor = 0.95

        # Adjust price based on inventory (lower inventory -> higher price)
        if inventory < 10:
            inventory_factor = 1.2
        elif inventory < 20:
            inventory_factor = 1.1
        else:
            inventory_factor = 0.9

        # Adjust price based on competitor prices
        if base_price > competitor_price:
            competitor_factor = 0.95
        else:
            competitor_factor = 1.05

        # Calculate final price
        adjusted_price = base_price * demand_factor * inventory_factor * competitor_factor
        return round(adjusted_price, 2)

    def update_prices(self):
        """Update prices for all products in the system."""
        updated_prices = {}
        for product_name in self.products:
            updated_prices[product_name] = self.adjust_price(product_name)
        return updated_prices

    def display_prices(self, updated_prices):
        """Display the updated prices."""
        print("Updated Product Prices:")
        for product, price in updated_prices.items():
            print(f"{product}: ${price}")


# Example Usage
if __name__ == "__main__":
    # Initialize the pricing system
    pricing_system = DynamicPricingSystem()

    # Simulate price updates
    updated_prices = pricing_system.update_prices()

    # Display the updated prices
    pricing_system.display_prices(updated_prices)
