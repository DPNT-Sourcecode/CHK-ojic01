from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        #Map prices and offers
        prices = {'A' : 50,
        'B' : 30,
        'C' : 20,
        'D' : 15
        }
        offers = {
            'A' : (3,130),
            'B' : (2,45)
        }

        #Check items are valid
        for item in skus:
            if item not in prices:
                return -1
        
        #Count how many occurances of each item
        counterMapping = Counter(skus)

        totalPrice = 0

        #Iterate through item
        for item, count in counterMapping.items():
            #Check if item is involved in an offer
            if item in offers:
                #Get details of offer
                quantity, price = offers[item]
                #Check how many times offer can be applied and apply it
                totalPrice += (count // quantity) * price
                #Apply normal price to remainder items
                totalPrice += (count % quantity) * prices[item]
            else:
                #Apply normal price if no offers apply
                totalPrice += count * prices[item]

        return totalPrice



