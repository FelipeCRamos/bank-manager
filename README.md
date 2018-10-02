# Bank manager
A python lib to make bills payment easier.

## How to use

To generate a report, just follow the steps:

+ Create a directory containing the `manage.py` file.
+ Create a `python 3.6+` script on the folder.
+ On the file you just created, import the `manage.py` file by typing into the first line of your code `from manage import *`.
+ Learn the syntax and be happy!

## Learning the syntax

Let's learn by example. Let's suppose you want to create the report of your two bank accounts (i.e. _Nubank_ and _Subank_).

Your code will look like:

```python
from manage import *

# first, begin declaring your banks, like: Bank("Bank-Name")
nu = Bank("Nubank")
su = Bank("Subank")

# Now, we refer to the banks as `nu` and `su`

# adds R$ 25 to the Nubank, to be payed by "me" and with the description as "some bill"
nu.add(25, "Me", "Some bill")

su.add(19.90, "Him", "He own me")	# adds R$ 19,90 to the Subank

gen_bill(nu)	# Generates Nubank bill and prints out
gen_bill(su)	# Generates Subank bill and prints out

timestamp() # Generates a cool timestamp
```

Then, your output will look like (by running `python3 example.py` on your terminal):

```
@ Nubank
        R$   25.00 - Some bill (Me)
        --------------------------------------
        R$   25.00 - TOTAL

        ~ DIVIDED TO:
        R$   25.00 - Me

@ Subank
        R$   19.90 - He own me (Him)
        --------------------------------------
        R$   19.90 - TOTAL

        ~ DIVIDED TO:
        R$   19.90 - Him

Generated on: 2018-10-02 17:04:54.353104
```



If you want to know more, just dive in the `manage.py` file, it's short :)





#### AUTHORSHIP
Codes made by __FelipeCRamos__.
