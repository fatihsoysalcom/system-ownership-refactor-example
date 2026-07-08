import logging

# Configure basic logging for better visibility into system operations.
# This is a first step towards taking ownership: understanding what the system is doing.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- System State (Managed with Ownership in Mind) ---
# In a real application, this would be a database or a more sophisticated state management.
# For this example, we use a dictionary, but the principles of clear access and modification apply.
inventory = {
    "Laptop": 10,
    "Mouse": 50,
    "Keyboard": 25
}

# --- Core Business Logic: Processing Orders ---
# This function embodies the "safe harbor" approach.
# It's designed to be robust, predictable, and easy to understand.
def process_order(item_name: str, quantity: int) -> bool:
    """
    Processes an order for a given item and quantity.

    Demonstrates ownership by:
    1. Clear Function Signature: Defines expected inputs.
    2. Input Validation: Prevents invalid operations early.
    3. State Management: Modifies shared state (inventory) in a controlled way.
    4. Error Handling: Provides clear feedback on failures.
    5. Logging: Records operations for traceability and debugging.
    """
    logging.info(f"Attempting to process order: {quantity} x {item_name}")

    # Ownership Principle 1: Input Validation
    # Prevent "garbage in, garbage out" scenarios that lead to unpredictable system behavior.
    if not isinstance(item_name, str) or not item_name:
        logging.error("Order failed: Item name must be a non-empty string.")
        return False
    if not isinstance(quantity, int) or quantity <= 0:
        logging.error("Order failed: Quantity must be a positive integer.")
        return False

    # Ownership Principle 2: Clear State Access and Modification
    # Ensure that shared resources (like inventory) are accessed and modified predictably.
    if item_name not in inventory:
        logging.warning(f"Order failed: Item '{item_name}' not found in inventory.")
        return False

    current_stock = inventory[item_name]

    # Ownership Principle 3: Business Rule Enforcement & Error Handling
    # Prevent the system from entering an invalid state (e.g., negative stock).
    # This prevents the "bomb" from exploding due to unmet business constraints.
    if current_stock < quantity:
        logging.warning(f"Order failed: Insufficient stock for '{item_name}'. "
                        f"Available: {current_stock}, Requested: {quantity}")
        return False

    # If all checks pass, proceed with the transaction.
    inventory[item_name] -= quantity
    logging.info(f"Order successful: {quantity} x {item_name}. Remaining stock: {inventory[item_name]}")
    return True

# --- Main Execution Block ---
if __name__ == "__main__":
    logging.info("--- Starting Inventory Management System ---")
    logging.info(f"Initial Inventory: {inventory}")

    print("\n--- Processing various orders ---")

    # Example 1: Successful order
    print("\nProcessing a valid order:")
    process_order("Laptop", 1) # Should succeed
    print(f"Current Inventory: {inventory}")

    # Example 2: Another successful order
    print("\nProcessing another valid order:")
    process_order("Mouse", 5) # Should succeed
    print(f"Current Inventory: {inventory}")

    # Example 3: Order with insufficient stock
    print("\nProcessing an order with insufficient stock:")
    process_order("Keyboard", 30) # Should fail
    print(f"Current Inventory: {inventory}")

    # Example 4: Order for a non-existent item
    print("\nProcessing an order for a non-existent item:")
    process_order("Monitor", 2) # Should fail
    print(f"Current Inventory: {inventory}")

    # Example 5: Order with invalid quantity
    print("\nProcessing an order with invalid quantity:")
    process_order("Laptop", -1) # Should fail
    print(f"Current Inventory: {inventory}")

    # Example 6: Order with invalid item name
    print("\nProcessing an order with invalid item name:")
    process_order("", 1) # Should fail
    print(f"Current Inventory: {inventory}")

    logging.info("--- Inventory Management System Finished ---")
    logging.info(f"Final Inventory: {inventory}")
