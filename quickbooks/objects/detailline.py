from six import python_2_unicode_compatible
from .base import QuickbooksBaseObject, Ref, CustomField, LinkedTxn, MarkupInfo


@python_2_unicode_compatible
class DetailLine(QuickbooksBaseObject):
    list_dict = {
        "LinkedTxn": LinkedTxn,
        "CustomField": CustomField,
    }

    def __init__(self, Id=None, LineNum=0, Description="", Amount=0,
                 DetailType="", LinkedTxn=None, CustomField=None):

        super(DetailLine, self).__init__()

        self.Id = Id
        self.LineNum = LineNum
        self.Description = Description
        self.Amount = Amount
        self.DetailType = DetailType

        self.LinkedTxn = LinkedTxn if LinkedTxn is not None else []
        self.CustomField = CustomField if CustomField is not None else []

    def __str__(self):
        return "[{0}] {1} {2}".format(self.LineNum, self.Description, self.Amount)


class DiscountOverride(QuickbooksBaseObject):
    class_dict = {
        "DiscountRef": Ref,
        "DiscountAccountRef": Ref,
    }

    qbo_object_name = "DiscountOverride"

    def __init__(self):
        super(DiscountOverride, self).__init__()
        self.PercentBased = False
        self.DiscountPercent = 0
        self.DiscountRef = None
        self.DiscountAccountRef = None


class DiscountLineDetail(QuickbooksBaseObject):
    class_dict = {
        "Discount": DiscountOverride,
        "ClassRef": Ref,
        "TaxCodeRef": Ref,
    }

    def __init__(self):
        super(DiscountLineDetail, self).__init__()

        self.Discount = None
        self.ClassRef = None
        self.TaxCodeRef = None


class DiscountLine(DetailLine):
    class_dict = {
        "DiscountLineDetail": DiscountLineDetail
    }

    def __init__(self):
        super(DiscountLine, self).__init__()
        self.DetailType = "DiscountLineDetail"
        self.DiscountLineDetail = None


class SubtotalLineDetail(QuickbooksBaseObject):
    class_dict = {
        "ItemRef": Ref
    }

    def __init__(self):
        super(SubtotalLineDetail, self).__init__()
        self.ItemRef = None


class SubtotalLine(DetailLine):
    class_dict = {
        "SubtotalLineDetail": SubtotalLineDetail
    }

    def __init__(self):
        super(SubtotalLine, self).__init__()
        self.DetailType = "SubtotalLineDetail"
        self.SubtotalLineDetail = None


class DescriptionLineDetail(QuickbooksBaseObject):
    class_dict = {
        "TaxCodeRef": Ref
    }

    def __init__(self, ServiceDate="", TaxCodeRef=None):
        super(DescriptionLineDetail, self).__init__()
        self.ServiceDate = ServiceDate
        self.TaxCodeRef = TaxCodeRef


class DescriptionLine(DetailLine):
    class_dict = {
        "DescriptionLineDetail": DescriptionLineDetail
    }

    def __init__(self, DescriptionLineDetail=None, **kwargs):
        super(DescriptionLine, self).__init__(**kwargs)
        self.DetailType = "DescriptionOnly"
        self.DescriptionLineDetail = DescriptionLineDetail


@python_2_unicode_compatible
class SalesItemLineDetail(QuickbooksBaseObject):
    class_dict = {
        "ItemRef": Ref,
        "ClassRef": Ref,
        "TaxCodeRef": Ref,
        "PriceLevelRef": Ref,
        "MarkupInfo": MarkupInfo,
    }

    def __init__(self, UnitPrice=None, Qty=None, ServiceDate=None, TaxInclusiveAmt=None,
                 MarkupInfo=None, ItemRef=None, ClassRef=None, TaxCodeRef=None,
                 PriceLevelRef=None):

        super(SalesItemLineDetail, self).__init__()

        self.UnitPrice = UnitPrice
        self.Qty = Qty
        self.ServiceDate = ServiceDate
        self.TaxInclusiveAmt = TaxInclusiveAmt

        self.MarkupInfo = MarkupInfo
        self.ItemRef = ItemRef
        self.ClassRef = ClassRef
        self.TaxCodeRef = TaxCodeRef
        self.PriceLevelRef = PriceLevelRef

    def __str__(self):
        return str(self.UnitPrice)


class SalesItemLine(DetailLine):
    class_dict = {
        "SalesItemLineDetail": SalesItemLineDetail
    }

    def __init__(self, SalesItemLineDetail=SalesItemLineDetail(), **kwargs):

        super(SalesItemLine, self).__init__(**kwargs)

        self.DetailType = "SalesItemLineDetail"
        self.SalesItemLineDetail = SalesItemLineDetail


class GroupLineDetail(QuickbooksBaseObject):
    pass


class GroupLine(DetailLine):
    class_dict = {
        "GroupLineDetail": GroupLineDetail
    }

    def __init__(self):
        super(GroupLine, self).__init__()
        self.DetailType = "SalesItemLineDetail"
        self.SalesItemLineDetail = None


class DescriptionLineDetail(QuickbooksBaseObject):
    class_dict = {
        "TaxCodeRef": Ref,
    }

    def __init__(self):
        super(DescriptionLineDetail, self).__init__()
        self.ServiceDate = ""
        self.TaxCodeRef = None


class DescriptionOnlyLine(DetailLine):
    class_dict = {
        "DescriptionLineDetail": DescriptionLineDetail
    }

    def __init__(self):
        super(DescriptionOnlyLine, self).__init__()
        self.DetailType = "DescriptionLineDetail"
        self.DescriptionLineDetail = None


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


class AccountBasedExpenseLine(DetailLine):
    class_dict = {
        "AccountBasedExpenseLineDetail": AccountBasedExpenseLineDetail
    }

    def __init__(self):
        super(AccountBasedExpenseLine, self).__init__()

        self.DetailType = "AccountBasedExpenseLineDetail"
        self.AccountBasedExpenseLineDetail = None


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


class ItemBasedExpenseLine(DetailLine):
    class_dict = {
        "ItemBasedExpenseLineDetail": ItemBasedExpenseLineDetail
    }

    def __init__(self):
        super(ItemBasedExpenseLine, self).__init__()

        self.DetailType = "ItemBasedExpenseLineDetail"
        self.ItemBasedExpenseLineDetail = None
