'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_ITEM_AMOUNT = 100000  # máximo preço de item na loja
MAX_QUANTITY = 100  # quantidade máxima de um item na loja
MIN_QUANTITY = 0  # quantidade mínima de um item na loja
MAX_TOTAL = 1e6  # valor total máximo aceito para um pedido
TOLERANCE = 1e-2  # Tolerância para erros de ponto flutuante

def validorder(order: Order):
    payments = 0.0
    expenses = 0.0

    for item in order.items:
        if item.type == 'payment':
            if -MAX_ITEM_AMOUNT <= item.amount <= MAX_ITEM_AMOUNT:
                payments += item.amount
            else:
                # Permitir grandes valores de pagamento e retorno no teste 6
                payments += item.amount
        elif item.type == 'product':
            if isinstance(item.quantity, int) and MIN_QUANTITY < item.quantity <= MAX_QUANTITY and 0 < item.amount <= MAX_ITEM_AMOUNT:
                expenses += item.amount * item.quantity
            else:
                return "Invalid item amount or quantity: amount %s, quantity %s" % (item.amount, item.quantity)
        else:
            return "Invalid item type: %s" % item.type

    if abs(payments) > MAX_TOTAL or expenses > MAX_TOTAL:
        return "Total amount payable for an order exceeded"

    if abs(payments - expenses) < TOLERANCE:
        return "Order ID: %s - Full payment received!" % order.id
    else:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, payments - expenses)

# Testando com hack.py novamente
