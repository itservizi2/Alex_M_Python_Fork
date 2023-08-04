class Quotation:
    def __init__(self, product_id, bid_price, ask_price, timestamp):
        self.__product_id = product_id
        self.__bid_price = bid_price
        self.__ask_price = ask_price
        self.__timestamp = timestamp
        self.__spread = ask_price - bid_price

    def get_product_id(self):
        return self.__product_id

    def get_bid_price(self):
        return self.__bid_price

    def get_ask_price(self):
        return self.__ask_price

    def get_timestamp(self):
        return self.__timestamp

    def get_spread(self):
        return self.__spread
