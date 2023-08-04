class QuotationStore:

    def __init__(self):
        self.__quotation_list = []

    def store_quotation(self, quotation):
        # TODO: Add validation
        self.__quotation_list.append(quotation)

    def read_quotes(self):
        return self.__quotation_list.copy()
