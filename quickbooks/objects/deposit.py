from six import python_2_unicode_compatible
from .base import QuickbooksBaseObject, Ref, LinkedTxn, QuickbooksManagedObject, LinkedTxnMixin, \
    QuickbooksTransactionEntity, CustomField


class AttachableRef(QuickbooksBaseObject):
    class_dict = {
        "EntityRef": Ref,
    }

    list_dict = {
        "CustomField": CustomField
    }

    def __init__(self, LineInfo="",  IncludeOnSend=False, Inactive=False,
                 NoRefOnly=False, EntityRef=None):
        super(AttachableRef, self).__init__()
        self.LineInfo = ""
        self.IncludeOnSend = False
        self.Inactive = False
        self.NoRefOnly = False
        self.EntityRef = None

        self.CustomField = []


class CashBackInfo(QuickbooksBaseObject):
    class_dict = {
        "AccountRef": None
    }

    def __init__(self, Amount=0, Memo="", AccountRef=None):
        super(CashBackInfo, self).__init__()
        self.Amount = Amount
        self.Memo = Memo
        self.AccountRef = AccountRef


class DepositLineDetail(QuickbooksBaseObject):
    class_dict = {
        "Entity": Ref,
        "ClassRef": Ref,
        "AccountRef": Ref,
        "PaymentMethodRef": Ref,
    }

    def __init__(self, CheckNum=None, TxnType=None, Entity=None, ClassRef=None,
                 AccountRef=None, PaymentMethodRef=None):
        super(DepositLineDetail, self).__init__()
        self.CheckNum = CheckNum
        self.TxnType = TxnType

        self.Entity = Entity
        self.ClassRef = ClassRef
        self.AccountRef = AccountRef
        self.PaymentMethodRef = PaymentMethodRef


@python_2_unicode_compatible
class DepositLine(QuickbooksBaseObject):
    class_dict = {
        "DepositToAccountRef": Ref,
        "DepositLineDetail": DepositLineDetail,
    }

    list_dict = {
        "LinkedTxn": LinkedTxn,
        "CustomField": CustomField,
    }

    qbo_object_name = "Deposit"

    def __init__(self, Id=None, LineNum=0, Description="", Amount=0,
                 DetailType="DepositLineDetail", LinkedTxn=[], CustomField=[],
                 DepositToAccountRef=None, DepositLineDetail=None):
        super(DepositLine, self).__init__()

        self.Id = Id
        self.LineNum = LineNum
        self.Description = Description
        self.Amount = Amount
        self.DetailType = DetailType
        self.LinkedTxn = LinkedTxn
        self.CustomField = CustomField

        self.DepositToAccountRef = DepositToAccountRef
        self.DepositLineDetail = DepositLineDetail

    def __str__(self):
        return str(self.Amount)


@python_2_unicode_compatible
class Deposit(QuickbooksManagedObject, QuickbooksTransactionEntity, LinkedTxnMixin):
    """
    QBO definition: A deposit object is a transaction that records one or more deposits of the following types:

        -A customer payment, originally held in the Undeposited Funds account, into the Asset Account specified by
        the Deposit.DepositToAccountRef attribute. The Deposit.line.LinkedTxn sub-entity is used in this
        case to hold deposit information.

        -A new direct deposit specified by Deposit.Line.DepositLineDetail line detail.
    """

    class_dict = {
        "DepositToAccountRef": Ref,
        "DepartmentRef": Ref,
        "CurrencyRef": Ref,
        "AttachableRef": AttachableRef,
        "CashBack": CashBackInfo,
    }

    list_dict = {
        "Line": DepositLine
    }

    detail_dict = {
        "DepositLineDetail": DepositLine
    }

    qbo_object_name = "Deposit"

    def __init__(self, TotalAmt=0, HomeTotalAmt=0, TxnDate="", DocNumber="",
                 ExchangeRate=1, GlobalTaxCalculation="TaxExcluded", PrivateNote="",
                 TxnStatus="", TxnSource="", DepositToAccountRef=None, DepartmentRef=None,
                 CurrencyRef=None, AttachableRef=None, Line=[], **kwargs):
        super(Deposit, self).__init__(**kwargs)
        self.TotalAmt = TotalAmt
        self.HomeTotalAmt = HomeTotalAmt
        self.TxnDate = TxnDate
        self.DocNumber = DocNumber
        self.ExchangeRate = ExchangeRate
        self.GlobalTaxCalculation = GlobalTaxCalculation
        self.PrivateNote = PrivateNote
        self.TxnStatus = TxnStatus
        self.TxnSource = TxnSource

        self.DepositToAccountRef = DepositToAccountRef
        self.DepartmentRef = DepartmentRef
        self.CurrencyRef = CurrencyRef
        self.AttachableRef = AttachableRef
        self.Line = Line

    def __str__(self):
        return str(self.TotalAmt)
