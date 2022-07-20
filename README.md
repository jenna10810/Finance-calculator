# Finance-calculator

## Uses
This finance calculator is used to access two types of different finacial calculators - an investment calculator and a home loan calculator.
The user is prompted to choose either _"investment"_ or _"bond"_ and then the respective code will run to determine the bond cost or the value of the investment after a certain time. 

## Useful features
When the user is prompted to enter either _"bond"_ or _"investment"_, the input is automatically capitilized. This ensures that the program can check the input and run the appropriate code to determine the value of their bond or investment. If the user does not enter a valid option, an appropriate error message is printed.

## Actual code
When the user selects _"investment"_, the user is prompted to enter:
* the amount of money that is being deposited
* the investment rate (as a percentage), but only the number should be entered, not the % sign
* the number of years that they plan on investing
* whether it is simple or compound intrest - from there a different formula is used to determine the final value

When the user selects the _"bond"_ option, the user is prompted to enter:
* the present value of the house
* the interest rate (as a percentage), but only the number should be entered, not the % sign
* the number of months they plan to take to repay the bond

Then the values are calculated and printed to the screen
