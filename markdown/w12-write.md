---
title: inventory.py
...

# Task

In a file called `inventory.py`, create a set of functions that read, write, and update a product inventory CSV file.

Your file should be a CSV file with three columns: product name, quantity, price.
Each product should have at most one row, and no quantity should be zero or negative.

An example inventory CSV file might be

````
eggplant,8,2.35
cannonball,2,14.20
stuffed red panda (toy),1503,16.50
````

## Functions

Write the following functions.

-   `restock(filename, product, quantity)` should 
    
    1.  Increase the quantity of the given product by the given ammount.
    2.  If the product is not found, it should use `input` to ask the user for a price, re-asking until a valid positive float is entered.
    3.  Return the new quantity in stock.

-   `sell(filename, product, quantity)` should 
    
    1.  If there are not enough of this item, leave the number of items unchanged and return `None`
    2.  Decrease the quantity of the given product by the given ammount.
    3.  If this results in zero items in stock, remove the entire row from the inventory.
    4.  Return the new quantity.

You may assume that all provided quantities are positive integers.

## Approach

As discussed in class, files are not easy to modify in-place.
Thus it is suggested that both `restock` and `sell` operate by

1.  open the existing file for reading
2.  open a new temporary file for writing, using the temporary file name `_temp_inventory.csv`
3.  copy lines from one file to the other, modifying, adding, or skipping lines as needed
4.  close both files
5.  remove the old file and rename the new one to replace it, using `os.remove(filename)` followed by `os.rename('_temp_inventory.csv', filename)`

Both functions should work both if the `filename` represents a file that exists and if it does not.
One way to handle this is to make a special helper function that checks if a file `os.path.exists` and if not creates it (by opening it for writing and then immediately closing it), then call that helper function at the beginning of both functions.

# Example Runs

If you run `inventory.py`, nothing should happen.  If defines functions, it does not run them.

If in a separate file you write the following:

````python
print(inventory.restock('shop.csv', 'toaster', 5))
print(inventory.restock('shop.csv', 'marmalade', 5))
print(inventory.sell('shop.csv', 'marmalade', 4))
print(inventory.restock('shop.csv', 'toaster', 2))
print(inventory.sell('shop.csv', 'toaster', 6))
print(inventory.restock('shop.csv', 'marmalade', 2))
print(inventory.sell('shop.csv', 'toaster', 6))
print(inventory.sell('shop.csv', 'toaster', 1))
````

you should see a dialog like the following:

````
What is the price of toaster? 23.50
5
What is the price of marmalade? 1.35
5
1
7
1
3
None
0
````

and should end up with a file named `shop.csv` that has one line in it:

````
marmalade,3,1.35
````

If you run the same code a second time, you'll have a different experience because there is already some marmalade in the shop, so it won't re-ask the price and will have more marmalde:

````
What is the price of toaster? zero
What is the price of toaster? 
What is the price of toaster? 185.95
5
8
4
7
1
6
None
0
````

You can get back to the original behavior by deleting `shop.csv`

Note that this example does not test some functionality, such as what happens if you sell before you restock, use several csv files in the same program, etc.
You should probably test those things on your own.

# Thought Questions

This sort of load-save file is inefficient; ask disk technology changes, more and more systems are using [append-only files](append-only.html).
We wrote up an assignment using those, but decided not to require it.
However, exploring it can be an interesting learning experience.
