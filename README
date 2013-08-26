Stamps.com API for Python


The Idea
========

The goal of this API is to provide a thin Python wrapper around the Stamps.com
Web Services API. As to why anyone would be generating big W-S APIs in the 21st
century? Don't get me started.

This API gives you a flexible configuration mechanism, calls for the more
common operations, cached authenticator token, conversation out-of-sync
detection, and examples as test cases.

This API depends on Python "Suds" and exerts minimal opinion on the format or
results of the Stamps.com operations. In other words, the naming conventions
for Suds-based I/O are not Pythonic and are dictated, instead, by the backing
WSDL. You'll probably want to extend the API here with your own so you can bury
all of the weird syntax under your own version of awesomeness.


The Installation
================

Simple with pip:

$ pip install stamps.py

Easy with setuptools (but you really shouldn't):

$ easy_install stamps.py


The Interface
=============

These and other public functions are documented in
stamps.services.StampsService:

add_postage
    Add postage to your account so you can start creating labels.

create_*
    Convenience methods for creating various call objects. In general, these
    will be bare objects that need to be populated with detail information
    based on the call you wish to make. See the get_* functions in tests.py for
    details.

get_account
    Account information accessor.

get_label
    Get a shipping label from one address to another based on a given rate.

get_rates
    Get the available rates for a given shipping object.

get_tracking
    Get the tracking events for a given label ID.

register_account
    Register a new account with Stamps.com.

remove_label
    Cancel a shipping label (triggers a postage refund with Stamps.com).


The Instantiation
=================

The best way to get started is to digest the code in tests.py, which uses a
file to initialize a test StampsConfiguration. Below is a simple example that
uses the API to retrieve account information. Register with
developer.stamps.com to get your own integration ID, username, and password.

    from stamps.config import StampsConfiguration
    from stamps.services import StampsService

    integration_id = "XXXXXXXX-1111-2222-3333-YYYYYYYYYYYY"
    username = "stampy"
    password = "secret"
    configuration = StampsConfiguration(integration_id=integration_id,
        username=username, password=password)
    service = StampsService(configuration=configuration)
    account = service.get_account()
