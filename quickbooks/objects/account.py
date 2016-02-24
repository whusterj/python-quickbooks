from six import python_2_unicode_compatible
from .base import Ref, QuickbooksManagedObject, QuickbooksTransactionEntity


@python_2_unicode_compatible
class Account(QuickbooksManagedObject, QuickbooksTransactionEntity):
    """
    QBO definition: Account is a component of a Chart Of Accounts, and is part of a Ledger. Used to record a total
    monetary amount allocated against a specific use. Accounts are one of five basic types: asset, liability,
    revenue (income), expenses, or equity. Delete is achieved by setting the Active attribute to false in an entity
    update request; thus, making it inactive. In this type of delete, the record is not permanently deleted, but
    is hidden for display purposes. References to inactive objects are left intact.
    """

    class_dict = {
        "CurrencyRef": Ref,
        "ParentRef": Ref,
        "TaxCodeRef": Ref,
    }

    qbo_object_name = "Account"

    def __init__(self, Name="", SubAccount=False, FullyQualifiedName="",
                 Active=True, Classification="", AccountType="", AccountSubType="",
                 Description="", AcctNum="", CurrentBalance=None,
                 CurrentBalanceWithSubAccounts=None, CurrencyRef=None,
                 ParentRef=None, TaxCodeRef=None, **kwargs):
        super(Account, self).__init__(**kwargs)

        self.Name = Name
        self.SubAccount = SubAccount
        self.FullyQualifiedName = FullyQualifiedName
        self.Active = Active
        self.Classification = Classification
        self.AccountType = AccountType
        self.AccountSubType = AccountSubType
        self.Description = Description
        self.AcctNum = AcctNum
        self.CurrentBalance = CurrentBalance  # Readonly
        self.CurrentBalanceWithSubAccounts = CurrentBalanceWithSubAccounts  # Readonly
        self.CurrencyRef = CurrencyRef
        self.ParentRef = ParentRef
        self.TaxCodeRef = TaxCodeRef

    def __str__(self):
        return self.FullyQualifiedName

    def to_ref(self):
        ref = Ref()
        ref.name = self.FullyQualifiedName
        ref.type = self.qbo_object_name
        ref.value = self.Id
        return ref
