# The challenge
The development team needs to make some tests with the file named "customers.csv". 

This file contains sensitive data so we need to apply some data masking on certain columns.
The data masking would consist on replacing with the character 'X' all the letter appearances on the alphanumeric columns,
but keeping symbols such as '@', ',' or '.'. 

We also want to replace the numbers in the numeric columns with the average 
value of all the quantities.

The columns containing sensitive data are "Name", "Email" and "Billing". 
The output file should be named "masked_clients.csv" and will contain the same 
columns as "customers.csv". 
For example:
 * john@mail.com should be transformed to XXXX@XXXX.XXX, keeping the same length and format
 * If there are 2 rows in the billing column with values 10 and 5, both of them should be converted to 7.5

As the input source might change in the near future (values will come from a database),
it is important that the code is as reusable as possible.


# What we are expecting
The minimum requirements for the challenge are:
* Program can be executed with Python3
* A README.md file with the instructions to run the code is included
* Good practices: code is readable and extensible
* For the sake of the exercise, no dependencies on the standard `csv` module or any 3rd-party modules are allowed

We will also run your program against a set of different input csv files to test some
edge cases.

# Extras
If you have some extra time:
* Print a report (to standard output) containing:
  * Maximum, minimum and average length of the "Name" field value
  * Maximum, minimum and average of the "Billing" field value

For example:
```
Name: Max. 10, Min. 5, Avg. 7.5
Billing: Max. 2000.00, Min. 500.00, Avg. 1250.0
```
