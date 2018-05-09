


def get_response(url, kwords):
    import requests
    """ This function creates a session from kwords dict
    which you passed as parameter.

    Then it sends datas to url you passd as parameter as well. 
    """

    # session = requests.session()
    try:
        response = requests.post(url, data=kwords, verify=False)
        return response
    except:
        print("=======================HATA====================")
        raise Exception
        print("===============================================")
