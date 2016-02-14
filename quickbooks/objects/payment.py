from six import python_2_unicode_compatible
from .base import QuickbooksBaseObject, Ref, LinkedTxn, QuickbooksManagedObject, QuickbooksTransactionEntity
from .creditcardpayment import CreditCardPayment


@python_2_unicode_compatible
class PaymentLine(QuickbooksBaseObject):
    list_dict = {
        "LinkedTxn": LinkedTxn,
    }

    def __init__(self, Id=None, LineNum=None, Description=None,
                 Amount=0, LinkedTxn=[]):
        super(PaymentLine, self).__init__()
        self.Id = Id
        self.LineNum = LineNum
        self.Description = Description
        self.Amount = Amount

        self.LinkedTxn = LinkedTxn

    def __str__(self):
        return "[{0}] {1} {2}".format(self.LineNum, self.Description, self.Amount)


@python_2_unicode_compatible
class Payment(QuickbooksManagedObject, QuickbooksTransactionEntity):
    """
    QBO definition: A Payment entity records a payment in QuickBooks. The payment can be applied for a particular
    customer against multiple Invoices and Credit Memos. It can also be created without any Invoice or Credit Memo,
    by just specifying an amount.

        - A Payment can be updated as a full update or a sparse update.
        - A Payment can be linked to multiple Invoices and Credit Memos
        - A Payment can be created as unapplied to any Invoice or Credit Memo, in which case it is recorded as a credit.
        - If any element in any line needs to be updated, all the Lines of a Payment have to be provided. This is true
            for full or sparse update. Lines can be updated only ALL or NONE.
        - To remove all lines, send an empty Lines tag.
        - To remove some of the lines, send all the Lines that need to be present MINUS the lines that need to
            be removed.
        - To add some lines, send all existing and new Lines that need to be present.
        - The sequence in which the Lines are received is the sequence in which lines are preserved.
    """

    class_dict = {
        "ARAccountRef": Ref,
        "CustomerRef": Ref,
        "PaymentMethodRef": Ref,
        "DepositToAccountRef": Ref,
        "CurrencyRef": Ref,
        "CreditCardPayment": CreditCardPayment,
    }

    list_dict = {
        "Line": PaymentLine
    }

    qbo_object_name = "Payment"

    def __init__(self, PaymentRefNum=None, TotalAmt=0, UnappliedAmt=None, ExchangeRate=None,
                 TxnDate=None, TxnSource=None, PrivateNote=None, TxnStatus=None,
                 CreditCardPayment=None, ARAccountRef=None, CustomerRef=None,
                 CurrencyRef=None, PaymentMethodRef=None, DepositToAccountRef=None,
                 Line=[], **kwargs):
        super(Payment, self).__init__(**kwargs)
        self.PaymentRefNum = PaymentRefNum
        self.TotalAmt = TotalAmt
        self.UnappliedAmt = UnappliedAmt
        self.ExchangeRate = ExchangeRate
        self.TxnDate = TxnDate
        self.TxnSource = TxnSource
        self.PrivateNote = PrivateNote
        self.TxnStatus = TxnStatus

        self.CreditCardPayment = CreditCardPayment
        self.ARAccountRef = ARAccountRef
        self.CustomerRef = CustomerRef
        self.CurrencyRef = CurrencyRef
        self.PaymentMethodRef = PaymentMethodRef
        self.DepositToAccountRef = DepositToAccountRef
        self.Line = Line

    def __str__(self):
        return str(self.TotalAmt)
