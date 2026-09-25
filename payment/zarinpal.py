from zarinpal import ZarinPal
from utils.config import Config
from django.conf import settings



def initiate_payment(amount,callback_url,description):
    try:
        config = Config(merchant_id=settings.ZARINPAL_MERCHANT_ID,sandbox=True)
        zarinpal = ZarinPal(config=config)

        response = zarinpal.payments.create(
            {
                "amount":amount,
                'callback_url':callback_url,
                "description":description
            }
        )

        print('payment successfully:',response)

        if 'data' in response and 'authority' in response['data']:
            authority = response['data']['authority']
            payment_url = zarinpal.payments.generate_payment_url(authority)
            print('payment url: ',payment_url)
            return authority,payment_url

        else:
            print('authority not found')

    except Exception as e:
        print("error during payment creation: ",e)