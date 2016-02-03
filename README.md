# python-quickbooks

[![Build Status](https://travis-ci.org/sidecars/python-quickbooks.svg?branch=master)](https://travis-ci.org/sidecars/python-quickbooks)
[![Coverage Status](https://coveralls.io/repos/sidecars/python-quickbooks/badge.svg?branch=master&service=github)](https://coveralls.io/github/sidecars/python-quickbooks?branch=master)

A Python library for accessing the Quickbooks API. 
Complete rework of [quickbooks-python](https://github.com/troolee/quickbooks-python).

These instructions were written for a Django application. Make sure to change it to whatever framework/method you're using. 

## Connecting your application to Quickbooks Online

1. Create the Authorization URL for your application:

        from quickbooks import QuickBooks
        
        quickbooks = QuickBooks(
            sandbox=True,
            consumer_key=QUICKBOOKS_CLIENT_KEY,
            consumer_secret=QUICKBOOKS_CLIENT_SECRET,
            callback_url=CALLBACK_URL
        )

        authorize_url = quickbooks.get_authorize_url()

    Store the authorize_url, request_token, and request_token_secret for use in the Callback method.

2. Handle the callback:

        quickbooks = QuickBooks(
            sandbox=True,
            consumer_key=QUICKBOOKS_CLIENT_KEY,
            consumer_secret=QUICKBOOKS_CLIENT_SECRET,
            callback_url=CALLBACK_URL
        )
    
        quickbooks.authorize_url = authorize_url
        quickbooks.request_token = request_token
        quickbooks.request_token_secret = request_token_secret
        quickbooks.set_up_service()
    
        quickbooks.get_access_tokens(request.GET['oauth_verifier'])
    
        realm_id = request.GET['realmId']
        access_token = quickbooks.access_token
        access_token_secret = quickbooks.access_token_secret

    Store realm_id, access_token, and access_token_secret need to be stored for later use.


## Accessing the API

QuickBooks client uses a singleton pattern. Just be sure to create the QuickBooks object before you make any calls to QBO.
Setup the client connection using the stored `access_token` and the `access_token_secret` and `realm_id`:

    from quickbooks import QuickBooks

    QuickBooks(
        sandbox=True,
        consumer_key=QUICKBOOKS_CLIENT_KEY,
        consumer_secret=QUICKBOOKS_CLIENT_SECRET,
        access_token=access_token,
        access_token_secret=access_token_secret,
        company_id=realm_id
    )


If you need to access a minor version (See [Minor versions](https://developer.intuit.com/docs/0100_accounting/0300_developer_guides/minor_versions) for details)
pass in minorversion when setting up the client:

    QuickBooks(
        sandbox=True,
        consumer_key=QUICKBOOKS_CLIENT_KEY,
        consumer_secret=QUICKBOOKS_CLIENT_SECRET,
        access_token=access_token,
        access_token_secret=access_token_secret,
        company_id=realm_id,
        minorversion=4
    )


List of objects:

    from quickbooks.objects.customer import Customer
    customers = Customer.all()

__Note:__ The maximum number of entities that can be returned in a response is 1000.  If the result size is not specified, the default number is 100. 
(See [Intuit developer guide](https://developer.intuit.com/docs/0100_accounting/0300_developer_guides/querying_data) for details)

Filtered list of objects:

    customers = Customer.filter(Active=True, FamilyName="Smith")
    

Filtered list of objects with paging:

    customers = Customer.filter(start_position=1, max_results=25, Active=True, FamilyName="Smith")
    

List Filtered by values in list:

    customer_names = ['Customer1', 'Customer2', 'Customer3']
    customers = Customer.choose(customer_names, field="DisplayName")


List with custom Where Clause (do not include the "WHERE"):
        
    customers = Customer.where("Active = True AND CompanyName LIKE 'S%'")
 

List with custom Where Clause with paging:
 

    customers = Customer.where("CompanyName LIKE 'S%'", start_position=1, max_results=25)
 
 
Filtering a list with a custom query (See [Intuit developer guide](https://developer.intuit.com/docs/0100_accounting/0300_developer_guides/querying_data) for supported SQL statements):

    customer = Customer.query("SELECT * FROM Customer WHERE Active = True")

Filtering a list with a custom query with paging:

    customer = Customer.query("SELECT * FROM Customer WHERE Active = True STARTPOSITION 1 MAXRESULTS 25")

Get single object by Id and update:

    customer = Customer.get(1)
    customer.CompanyName = "New Test Company Name"
    customer.save()


Create new object:

    customer = Customer()
    customer.CompanyName = "Test Company"
    customer.save()


## Batch Operations

The batch operation enables an application to perform multiple operations in a single request
(See [Intuit Batch Operations Guide](https://developer.intuit.com/docs/0100_accounting/0300_developer_guides/batch_operations) for full details).


Batch create a list of objects: 

    from quickbooks.batch import batch_create
    
    customer1 = Customer()
    customer1.CompanyName = "Test Company 1"
    customer1.save()
    
    customer2 = Customer()
    customer2.CompanyName = "Test Company 2"
    customer2.save()
    
    customers = []
    customers.append(customer1)
    customers.append(customer2)
    
    results = batch_create(customers)
    
    
Batch update a list of objects:
    
    from quickbooks.batch import batch_update
    
    customers = Customer.filter(Active=True)
    
    # Update customer records
    
    results = batch_update(customers)
    
    
Batch delete a list of objects:
    
    from quickbooks.batch import batch_delete
    
    customers = Customer.filter(Active=False)
    results = batch_delete(customers)
    
    
Review results for batch operation:
    
    # successes is a list of objects that were successfully updated 
    for obj in results.successes:
        print "Updated " + obj.DisplayName
    
    # faults contains list of failed operations and associated errors
    for fault in results.faults:
        print "Operation failed on " + fault.original_object.DisplayName 
        
        for error in fault.Error:
            print "Error " + error.Message 
    

__Note:__ Objects and object property names match their Quickbooks counterparts and do not follow PEP8. 

__Note:__ This is a work-in-progress made public to help other developers access the QuickBooks API. 
Built for a Django project running on Python 2.


