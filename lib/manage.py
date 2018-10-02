#!/usr/bin/env python3

tab = '    '

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
        return 'R$ {:7.2f} - {} ({})'.format(
            self.amount, self.description, self.payer)

    def get_amount(self):
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

    def report(self):
        ''' see all bills in a pretty print '''
        print("@ {}".format(self.bank_name))
        for bill in self.bills_list:
            print('\t', end='')
            print(bill)

    def sum(self):
        ''' get total bank sum '''
        sum = float()
        for bill in self.bills_list:
            sum += bill.get_amount()
        return sum

    def sum_payer(self, payer):
        ''' get specific payer bank sum '''
        sum = float()
        for bill in self.bills_list:
            if(bill.get_payer() == payer):
                sum += bill.get_amount()
        return sum

    def payers(self):
        ''' returns a set of payers of a given bank '''
        set_payers = list()
        for bill in self.bills_list:
            set_payers.append(bill.get_payer())
        set_payers = set(set_payers)
        return set_payers

def gen_bill(bank):
    ''' general function to give a report '''
    bank.report()
    print('\t' + "-" * 38)
    print('\t' + "R$ {:7.2f} - TOTAL".format(bank.sum()))
    print("\n\t~ DIVIDED TO:")
    for payer in bank.payers():
        print('\t' + "R$ {:7.2f} - {}".format(bank.sum_payer(payer), payer))
    print()

