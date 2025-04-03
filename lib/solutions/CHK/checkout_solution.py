
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = {'A' : 50,
        'B' : 30,
        'C' : 20,
        'D' : 15
        }
        offers = {
            'A' : (3,130),
            'B' : (2,45)
        }

        for item in skus:
            if item not in prices:
                return -1

