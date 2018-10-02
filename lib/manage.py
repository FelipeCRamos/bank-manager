#!/usr/bin/env python3

class Bill:
    '''
    This is the class to represent each bill, having the info about:
        - $$
        - Author
        - Description
    '''
    def __init__(self, bill_amount, bill_payer, bill_name):
        ''' Default constructor, takes ($, Author, Description) '''
        self.amount = bill_amount
        self.description = bill_name
        self.payer = bill_payer

    def __repr__(self):
        ''' Representation when called direcly '''
        return 'R$ {:7.2f} - ({}) {}'.format(
            self.amount, self.payer, self.description)

    def get_bill(self):
        ''' get method for $$ '''
        return self.amount

    def get_payer(self):
        ''' get method for payer '''
        return self.payer

    def get_description(self):
        ''' get method for description '''
        return self.description

class Bank:
    def __init__(self, b_name):
        ''' default constructor for creating a new bank (i.e.: Bank("Name")) '''
        self.bank_name = str()
        self.bills_list = list()
        self.bank_name = b_name

    def add(self, bill, payer, description):
        '''
        Add a specific bill to the bank, like:
        bank.add(1.99, "Me", "Something")
        '''
        b = Bill(bill, payer, description)
        self.bills_list.append(b)

    def see_bills(self):
        ''' see all bills in a pretty print '''
        print("\n" + "-"*80)
        print("Bank {}".format(self.bank_name))
        print("-" * 80 + "\n")
        for bill in self.bills_list:
            print(" "*3, bill)
        print("\n" + "-" * 80)

    def sum(self):
        ''' get total bank sum '''
        sum = float()
        for bill in self.bills_list:
            sum += bill.get_bill()
        return sum

    def sum_bills(self, payer):
        ''' get specific payer bank sum '''
        sum = float()
        for bill in self.bills_list:
            if(bill.get_payer() == payer):
                sum += bill.get_bill()
        return sum

    def payers(self):
        ''' returns a set of payers of a given bank '''
        set_payers = list()
        for bill in self.bills_list:
            set_payers.append(bill.get_payer())
        set_payers = set(set_payers)
        return set_payers

def bill(bank):
    ''' general function to give a report '''
    bank.see_bills()
    print("Total: R$ {:7.2f}".format(bank.sum()))
    for payer in bank.payers():
        print("\t{} : R$ {:7.2f}".format(payer, bank.sum_bills(payer)))

