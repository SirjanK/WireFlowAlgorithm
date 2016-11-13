import numpy as np
from scipy import optimize

def main():
    c = np.array([0,0,0,1])
    Aub = np.array([[-2,5,-4,-1], [-1,-5,8,-1], [3, -1, -3,-1]])
    bub = np.array([0, 0, 0])
    Aeq = np.array([[1,1,1,0]])
    beq = np.array([1])
    result = optimize.linprog(c, Aub, bub, A_eq=Aeq, b_eq=beq)
    print(result)


def get_currency_bank(currency):
    return 'fake bank'

def get_transcations_for_currency(currency, total_fees, total_amount_sent):
    transactions = []
    currency_bank = get_currency_bank(currency)
    for payment in currency_bank.get_out_payments():
        payment_amount = payment.get_amount()
        sender, receiver = payment.get_sender(), payment.get_receiver()
        transactions += [Payment(sender, currency_bank, payment_amount)]
        transactions += [Payment(currency_bank, receiver, payment_amount)]
    return transactions


if __name__ == '__main__':
    main()
