from six import python_2_unicode_compatible
from quickbooks.objects.detailline import DetailLine, ItemBasedExpenseLine, \
    AccountBasedExpenseLine, AccountBasedExpenseLineDetail, ItemBasedExpenseLineDetail
from .base import Ref, LinkedTxn, QuickbooksBaseObject, QuickbooksManagedObject, \
    QuickbooksTransactionEntity, LinkedTxnMixin
from .tax import TxnTaxDetail


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
        "Line": DetailLine,
    }

    detail_dict = {
        "ItemBasedExpenseLineDetail": ItemBasedExpenseLine,
        "AccountBasedExpenseLineDetail": AccountBasedExpenseLine,
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

    def to_linked_txn(self):
        linked_txn = LinkedTxn()
        linked_txn.TxnId = self.Id
        linked_txn.TxnType = "Bill"
        linked_txn.TxnLineId = 1

        return linked_txn

    def to_ref(self):
        ref = Ref()

        ref.name = self.DisplayName
        ref.type = self.qbo_object_name
        ref.value = self.Id

        return ref
