# 'accounts' URLs
def url_get_all_accounts(api_key):
    return "http://api.reimaginebanking.com/accounts?key={}".format(api_key)

def url_get_account_aid(account_id, api_key):
    return "http://api.reimaginebanking.com/accounts/{}?key={}".format(account_id, api_key)

def url_get_account_cid(customer_id, api_key):
    return "http://api.reimaginebanking.com/customers/{}/accounts?key={}".format(customer_id, api_key)

def url_account_create(account_id, api_key):
    return "http://api.reimaginebanking.com/customers/{}/accounts?key={}".format(customer_id, api_key)

def url_account_modify(account_id, api_key):
    return "http://api.reimaginebanking.com/accounts/{}?key={}".format(account_id, api_key)

def url_account_delete(account_id, api_key):
    return "http://api.reimaginebanking.com/accounts/{}?key={}".format(account_id, api_key)
#------------------------------------------------------------------------------
# 'customer' URLs
# 'merchants' URLs
# 'purchases' urls
def url_get_purchases_aid(account_id, api_key):
    return "http://api.reimaginebanking.com/accounts/{}/purchases?key={}".format(account_id, api_key)

def url_get_purchases_mid(merchant_id, api_key):
    return "http://api.reimaginebanking.com/merchants/{}/purchases?key={}".format(merchant_id, api_key)

def url_get_purchase_pid(purchase_id, api_key):
    return "http://api.reimaginebanking.com/purchases/{}?key={}".format(purchase_id, api_key)

def url_purchase_aid(account_id, api_key):
    return "http://api.reimaginebanking.com/accounts/{}/purchases?key={}".format(account_id, api_key)

def url_purchase_modify(purchase_id, api_key):
    return "http://api.reimaginebanking.com/purchases/{}?key={}".format(purchase_id, api_key)

def url_purchase_delete(purchase_id, api_key):
    return "http://api.reimaginebanking.com/purchases/{}?key={}".format(purchase_id, api_key)
