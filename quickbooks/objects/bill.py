from six import python_2_unicode_compatible
from .base import QuickbooksBaseObject, Ref, LinkedTxn, QuickbooksManagedObject, \
    QuickbooksTransactionEntity, LinkedTxnMixin, MarkupInfo
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

    def __init__(self, BillableStatus=None, TaxAmount=None, TaxInclusiveAmt=None, CustomerRef=None,
                 AccountRef=None, TaxCodeRef=None, **kwargs):

        super(AccountBasedExpenseLineDetail, self).__init__(**kwargs)

        self.BillableStatus = BillableStatus
        self.TaxAmount = TaxAmount
        self.TaxInclusiveAmt = TaxInclusiveAmt

        self.CustomerRef = CustomerRef
        self.AccountRef = AccountRef
        self.TaxCodeRef = TaxCodeRef

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

    def __init__(self, BillableStatus=None, UnitPrice=0, TaxInclusiveAmt=0, Qty=0,
                 ItemRef=None, ClassRef=None, PriceLevelRef=None, TaxCodeRef=None,
                 MarkupInfo=None, CustomerRef=None, **kwargs):

        super(ItemBasedExpenseLineDetail, self).__init__(**kwargs)

        self.BillableStatus = BillableStatus
        self.UnitPrice = UnitPrice
        self.TaxInclusiveAmt = TaxInclusiveAmt
        self.Qty = Qty
        self.ItemRef = ItemRef
        self.ClassRef = ClassRef
        self.PriceLevelRef = PriceLevelRef
        self.TaxCodeRef = TaxCodeRef
        self.MarkupInfo = MarkupInfo
        self.CustomerRef = CustomerRef


@python_2_unicode_compatible
class BillLine(QuickbooksBaseObject):
    class_dict = {
        "AccountBasedExpenseLineDetail": AccountBasedExpenseLineDetail,
        "ItemBasedExpenseLineDetail": ItemBasedExpenseLineDetail,
    }

    list_dict = {
        "LinkedTxn": LinkedTxn
    }

    def __init__(self, Id=0, Amount='', LineNum=0, Description='',
                 DetailType='AccountBasedExpenseLineDetail', AccountBasedExpenseLineDetail=None,
                 ItemBasedExpenseLineDetail=None, **kwargs):

        super(BillLine, self).__init__(**kwargs)

        self.Id = Id
        self.Amount = Amount

        self.LineNum = LineNum
        self.Description = Description
        self.DetailType = DetailType

        self.AccountBasedExpenseLineDetail = AccountBasedExpenseLineDetail
        self.ItemBasedExpenseLineDetail = ItemBasedExpenseLineDetail

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
                 ExchangeRate=None, GlobalTaxCalculation=None, SalesTermRef=None, CurrencyRef=None,
                 AttachableRef=None, VendorRef=None, DepartmentRef=None, APAccountRef=None,
                 LinkedTxn=[], Line=[], **kwargs):

        super(Bill, self).__init__(**kwargs)

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
