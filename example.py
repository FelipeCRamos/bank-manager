#!/usr/bin/env python3
from lib.manage import *

nu = Bank("Nubank")

nu.add(600.50, "Me", "New PC Part")
nu.add(200.00, "Me", "Transport")
nu.add(400.00, "Me", "Food")

bb = Bank("Banco do Brasil")

bb.add(9.90, "Me", "Snacks")
bb.add(34.99, "My-friend", "UBER")
bb.add(30.00, "My-friend", "Present")

bill(nu)
bill(bb)
