from lesson_24_live.pratcice_exercies.Quotation import Quotation
from lesson_24_live.pratcice_exercies.QuotationStore import QuotationStore

import unittest


class BasicQuotationTest(unittest.TestCase):
    def test_store_empty(self):
        quotation_store = QuotationStore()
        result = quotation_store.read_quotes()
        self.assertEqual(0, len(result))

    def test_store_quotation(self):
        quotation_store = QuotationStore()
        quotation = Quotation("EURUSD", 1.2, 1.3, 1)
        quotation_store.store_quotation(quotation)
        result = quotation_store.read_quotes()
        self.assertEqual(1, len(result))

    def test_read_quotes(self):
        quotation1 = Quotation("USDJPY", 111.1, 111.2, 2)
        quotation2 = Quotation("EURUSD", 1.2, 1.3, 1)
        quotation_list = [quotation1, quotation2]
        quotation_store = QuotationStore()
        quotation_store.store_quotation(quotation1)
        quotation_store.store_quotation(quotation2)
        result = quotation_store.read_quotes()
        self.assertEqual(quotation_list, result)

    def test_impodency_of_read(self):
        quotation1 = Quotation("USDJPY", 111.1, 111.2, 2)
        quotation2 = Quotation("EURUSD", 1.2, 1.3, 1)
        quotation_store = QuotationStore()
        quotation_store.store_quotation(quotation1)
        quotation_store.store_quotation(quotation2)
        qout_list = quotation_store.read_quotes()
        qout_list.append(quotation1)
        self.assertEqual(len(quotation_store.read_quotes()), 2)
