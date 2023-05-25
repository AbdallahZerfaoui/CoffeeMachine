# Coffee Machine Program

This is a simple coffee machine program that allows users to select their desired drink, check the available resources, process coins for payment, and dispense the selected drink. The program also provides a report of the current resource levels and tracks the profit made from the sales.

## Program Requirements

1. Prompt the user by asking, "What would you like? (espresso/latte/cappuccino):"
   - Check the user's input to decide the next steps.
   - The prompt should be displayed every time an action is completed, such as after dispensing a drink, and should appear again to serve the next customer.

2. Turn off the Coffee Machine by entering "off" in the prompt:
   - The secret word "off" is used by maintainers to turn off the machine.
   - When "off" is entered, the program should terminate.

3. Print a report:
   - When the user enters "report" in the prompt, a report should be generated displaying the current resource levels, such as:
     ```
     Water: 100ml
     Milk: 50ml
     Coffee: 76g
     Money: $2.5
     ```

4. Check if resources are sufficient:
   - When the user selects a drink, the program should check if there are enough resources available to make that drink.
   - If there are insufficient resources (e.g., not enough water, milk, or coffee), the program should display a message such as "Sorry, there is not enough water."

5. Process coins:
   - If there are sufficient resources to make the selected drink, the program should prompt the user to insert coins.
   - The accepted coin denominations are: quarters ($0.25), dimes ($0.10), nickels ($0.05), and pennies ($0.01).
   - The program should calculate the total monetary value of the coins inserted by the user.

6. Check if the transaction is successful:
   - The program should check if the user has inserted enough money to purchase the selected drink.
   - If the inserted amount is insufficient, the program should display a message such as "Sorry, that's not enough money. Money refunded."
   - If the inserted amount is equal to or exceeds the cost of the drink, the program should add the cost to the machine's profit and display an appropriate message.

7. Make the selected drink:
   - If the transaction is successful and there are sufficient resources, the program should deduct the required ingredients from the available resources.
   - After deducting the resources, the program should display a message such as "Here is your latte. Enjoy!" (if latte was the chosen drink).

## Getting Started

To run the Coffee Machine program, follow these steps:

1. Clone the repository or download the source code files.
2. Make sure you have Python installed on your machine.
3. Open the terminal or command prompt and navigate to the project directory.
4. Run the command `python main.py` to start the program.
5. Follow the prompts and interact with the Coffee Machine.

Enjoy your coffee!
