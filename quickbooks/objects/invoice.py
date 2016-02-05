from six import python_2_unicode_compatible
from .base import QuickbooksBaseObject, Ref, CustomField, Address, EmailAddress, CustomerMemo, QuickbooksManagedObject, \
    QuickbooksTransactionEntity, LinkedTxn, LinkedTxnMixin
from .tax import TxnTaxDetail
from .detailline import DetailLine


class DeliveryInfo(QuickbooksBaseObject):
    def __init__(self):
        super(DeliveryInfo, self).__init__()
        self.DeliveryType = ""
        self.DeliveryTime = ""


@python_2_unicode_compatible
class Invoice(QuickbooksManagedObject, QuickbooksTransactionEntity, LinkedTxnMixin):
    """
    QBO definition: An Invoice represents a sales form where the customer pays for a product or service later.

    """

    class_dict = {
        "DepartmentRef": Ref,
        "CurrencyRef": Ref,
        "CustomerRef": Ref,
        "ClassRef": Ref,
        "SalesTermRef": Ref,
        "ShipMethodRef": Ref,
        "DepositToAccountRef": Ref,
        "BillAddr": Address,
        "ShipAddr": Address,
        "TxnTaxDetail": TxnTaxDetail,
        "BillEmail": EmailAddress,
        "CustomerMemo": CustomerMemo,
        "DeliveryInfo": DeliveryInfo
    }

    list_dict = {
        "CustomField": CustomField,
        "Line": DetailLine,
        "LinkedTxn": LinkedTxn,
    }

    qbo_object_name = "Invoice"

    def __init__(self, Deposit=0, Balance=0, AllowIPNPayment=True, DocNumber="",
                 PrivateNote="", DueDate="", ShipDate="", TrackingNum="", TotalAmt="",
                 ApplyTaxAfterDiscount=False, PrintStatus="NotSet", EmailStatus="NotSet",
                 ExchangeRate=1, GlobalTaxCalculation="TaxExcluded", EInvoiceStatus=None,
                 BillAddr=None, ShipAddr=None, BillEmail=None, CustomerRef=None,
                 CurrencyRef=None, CustomerMemo=None, DepartmentRef=None, TxnTaxDetail=None,
                 DeliveryInfo=None, CustomField=[], Line=[], LinkedTxn=[]):
        super(Invoice, self).__init__()
        self.Deposit = Deposit
        self.Balance = Balance
        self.AllowIPNPayment = AllowIPNPayment
        self.DocNumber = DocNumber
        self.PrivateNote = PrivateNote
        self.DueDate = DueDate
        self.ShipDate = ShipDate
        self.TrackingNum = TrackingNum
        self.TotalAmt = TotalAmt
        self.ApplyTaxAfterDiscount = ApplyTaxAfterDiscount
        self.PrintStatus = PrintStatus
        self.EmailStatus = EmailStatus
        self.ExchangeRate = ExchangeRate
        self.GlobalTaxCalculation = GlobalTaxCalculation

        self.EInvoiceStatus = EInvoiceStatus

        self.BillAddr = BillAddr
        self.ShipAddr = ShipAddr
        self.BillEmail = BillEmail
        self.CustomerRef = CustomerRef
        self.CurrencyRef = CurrencyRef
        self.CustomerMemo = CustomerMemo
        self.DepartmentRef = DepartmentRef
        self.TxnTaxDetail = TxnTaxDetail
        self.DeliveryInfo = DeliveryInfo

        self.CustomField = CustomField
        self.Line = Line
        self.LinkedTxn = LinkedTxn

    def __str__(self):
        return str(self.TotalAmt)

    def to_linked_txn(self):
        linked_txn = LinkedTxn()
        linked_txn.TxnId = self.Id
        linked_txn.TxnType = "Invoice"
        linked_txn.TxnLineId = 1

        return linked_txn

    @property
    def email_sent(self):
        if self.EmailStatus == "EmailSent":
            return True

        return False
