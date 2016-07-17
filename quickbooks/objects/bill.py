from six import python_2_unicode_compatible
from .base import QuickbooksBaseObject, Ref, LinkedTxn, QuickbooksManagedObject, QuickbooksTransactionEntity, \
    LinkedTxnMixin, MarkupInfo
from .tax import TxnTaxDetail


@python_2_unicode_compatible
class AccountBasedExpenseLineDetail(QuickbooksBaseObject):
    class_dict = {
        "CustomerRef": Ref,
        "AccountRef": Ref,
        "TaxCodeRef": Ref,
        "ClassRef": Ref,
        "MarkupInfo": MarkupInfo,
    }

    def __init__(self):
        super(AccountBasedExpenseLineDetail, self).__init__()
        self.BillableStatus = ""
        self.TaxAmount = 0
        self.TaxInclusiveAmt = 0

        self.CustomerRef = None
        self.AccountRef = None
        self.TaxCodeRef = None

    def __str__(self):
        return self.BillableStatus


class ItemBasedExpenseLineDetail(QuickbooksBaseObject):
    class_dict = {
        "ItemRef": Ref,
        "ClassRef": Ref,
        "PriceLevelRef": Ref,
        "TaxCodeRef": Ref,
        "CustomerRef": Ref,
        "MarkupInfo": MarkupInfo
    }

    def __init__(self):
        super(ItemBasedExpenseLineDetail, self).__init__()
        self.BillableStatus = ""
        self.UnitPrice = 0
        self.TaxInclusiveAmt = 0
        self.Qty = 0
        self.ItemRef = None
        self.ClassRef = None
        self.PriceLevelRef = None
        self.TaxCodeRef = None
        self.MarkupInfo = None
        self.CustomerRef = None


@python_2_unicode_compatible
class BillLine(QuickbooksBaseObject):
    class_dict = {
        "AccountBasedExpenseLineDetail": AccountBasedExpenseLineDetail,
        "ItemBasedExpenseLineDetail": ItemBasedExpenseLineDetail,
    }

    list_dict = {
        "LinkedTxn": LinkedTxn
    }

    def __init__(self):
        super(BillLine, self).__init__()

        self.Id = 0
        self.LineNum = 0
        self.Description = ""
        self.Amount = ""
        self.DetailType = "AccountBasedExpenseLineDetail"

        self.AccountBasedExpenseLineDetail = None
        self.ItemBasedExpenseLineDetail = None

    def __str__(self):
        return str(self.Amount)


@python_2_unicode_compatible
class Bill(QuickbooksManagedObject, QuickbooksTransactionEntity, LinkedTxnMixin):
    """
    QBO definition: A Bill entity is an AP transaction representing a request-for-payment from a third party for
    goods/services rendered and/or received.
    """

    class_dict = {
        "SalesTermRef": Ref,
        "CurrencyRef": Ref,
        "APAccountRef": Ref,
        "VendorRef": Ref,
        "AttachableRef": Ref,
        "DepartmentRef": Ref,
        "TxnTaxDetail": TxnTaxDetail,
    }

    list_dict = {
        "Line": BillLine,
        "LinkedTxn": LinkedTxn
    }

    qbo_object_name = "Bill"

    def __init__(self, DueDate="", Balance=0, TotalAmt=0, TxnDate="", DocNumber="", PrivateNote="",
                 ExchangeRate=None, GlobalTaxCalculation="", SalesTermRef=None, CurrencyRef=None,
                 AttachableRef=None, VendorRef=None, DepartmentRef=None, APAccountRef=None,
                 LinkedTxn=[], Line=[]):

        super(Bill, self).__init__()

        self.DueDate = DueDate
        self.Balance = Balance
        self.TotalAmt = TotalAmt
        self.TxnDate = TxnDate
        self.DocNumber = DocNumber
        self.PrivateNote = PrivateNote
        self.ExchangeRate = ExchangeRate
        self.GlobalTaxCalculation = GlobalTaxCalculation

        self.SalesTermRef = SalesTermRef
        self.CurrencyRef = CurrencyRef
        self.AttachableRef = AttachableRef
        self.VendorRef = VendorRef
        self.DepartmentRef = DepartmentRef
        self.APAccountRef = APAccountRef

        self.LinkedTxn = LinkedTxn
        self.Line = Line

    def __str__(self):
        return str(self.Balance)
