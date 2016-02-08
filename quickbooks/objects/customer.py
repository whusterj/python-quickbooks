from six import python_2_unicode_compatible
from .base import (
    Address, PhoneNumber, EmailAddress, WebAddress,
    Ref, QuickbooksManagedObject, QuickbooksTransactionEntity,
)


@python_2_unicode_compatible
class Customer(QuickbooksManagedObject, QuickbooksTransactionEntity):
    """
    QBO definition: A customer is a consumer of the service or product that your business offers. The Customer object
    allows you to categorize customers according to your business requirements. You must first create a customer
    and then create a job referencing that customer as a parent with the ParentRef attribute. Some areas a
    sub-customer/job can be used include:

      -To track a job for the top-level customer, such as a kitchen remodel or bathroom remodel.
      -Members of a team or league.
      -Properties managed by a Homeowner Association or Property Management Company.
    """

    class_dict = {
        "BillAddr": Address,
        "ShipAddr": Address,
        "PrimaryPhone": PhoneNumber,
        "AlternatePhone": PhoneNumber,
        "Mobile": PhoneNumber,
        "Fax": PhoneNumber,
        "PrimaryEmailAddr": EmailAddress,
        "WebAddr": WebAddress,
        "DefaultTaxCodeRef": Ref,
        "SalesTermRef": Ref,
        "PaymentMethodRef": Ref,
        "CurrencyRef": Ref,
        "ParentRef": Ref,
        "ARAccountRef": Ref,
    }

    qbo_object_name = "Customer"

    def __init__(self, Title="", GivenName="", MiddleName="", FamilyName="", Suffix="",
                 FullyQualifiedName="", CompanyName="", DisplayName="", PrintOnCheckName="",
                 Notes="", Active=True, Job=False, BillWithParent=False, Taxable=True,
                 Balance=0, BalanceWithJobs=0, PreferredDeliveryMethod="", ResaleNum="",
                 Level=0, OpenBalanceDate="", BillAddr=None, ShipAddr=None, PrimaryPhone=None,
                 AlternatePhone=None, Mobile=None, Fax=None, PrimaryEmailAddr=None, WebAddr=None,
                 DefaultTaxCodeRef=None, SalesTermRef=None, PaymentMethodRef=None, ParentRef=None,
                 ARAccountRef=None, **kwargs):
        super(Customer, self).__init__(**kwargs)
        self.Title = Title
        self.GivenName = GivenName
        self.MiddleName = MiddleName
        self.FamilyName = FamilyName
        self.Suffix = Suffix
        self.FullyQualifiedName = FullyQualifiedName
        self.CompanyName = CompanyName
        self.DisplayName = DisplayName  # Constraints:Must be unique
        self.PrintOnCheckName = PrintOnCheckName
        self.Notes = Notes
        self.Active = Active
        self.Job = Job
        self.BillWithParent = BillWithParent
        self.Taxable = Taxable
        self.Balance = Balance
        self.BalanceWithJobs = BalanceWithJobs
        self.PreferredDeliveryMethod = PreferredDeliveryMethod
        self.ResaleNum = ResaleNum
        self.Level = Level
        self.OpenBalanceDate = OpenBalanceDate

        self.BillAddr = BillAddr
        self.ShipAddr = ShipAddr
        self.PrimaryPhone = PrimaryPhone
        self.AlternatePhone = AlternatePhone
        self.Mobile = Mobile
        self.Fax = Fax
        self.PrimaryEmailAddr = PrimaryEmailAddr
        self.WebAddr = WebAddr
        self.DefaultTaxCodeRef = DefaultTaxCodeRef
        self.SalesTermRef = SalesTermRef
        self.PaymentMethodRef = PaymentMethodRef
        self.ParentRef = ParentRef
        self.ARAccountRef = ARAccountRef

    def __str__(self):
        return self.DisplayName

    def to_ref(self):
        return Ref(
            name=self.DisplayName,
            type=self.qbo_object_name,
            value=self.Id
        )
