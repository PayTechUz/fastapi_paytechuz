from paytechuz.gateways.payme import PaymeGateway
from paytechuz.gateways.click import ClickGateway

from app import config


def get_gateways(name=None):
    """
    Get payment gateway(s).

    Args:
        name: Gateway name ('payme' or 'click').
              If None, returns all gateways.

    Returns:
        Single gateway instance if name is provided,
        or dict of all gateways if name is None.
    """
    if name:
        if name == "payme":
            return PaymeGateway(
                payme_id=config.PAYME_ID,
                payme_key=config.PAYME_KEY,
                is_test_mode=config.IS_TEST_MODE
            )
        if name == "click":
            return ClickGateway(
                service_id=config.CLICK_SERVICE_ID,
                merchant_id=config.CLICK_MERCHANT_ID,
                merchant_user_id=config.CLICK_MERCHANT_USER_ID,
                secret_key=config.CLICK_SECRET_KEY,
                is_test_mode=config.IS_TEST_MODE
            )

        return None

    return {
        "payme": PaymeGateway(
            payme_id=config.PAYME_ID,
            payme_key=config.PAYME_KEY,
            is_test_mode=config.IS_TEST_MODE
        ),
        "click": ClickGateway(
            service_id=config.CLICK_SERVICE_ID,
            merchant_id=config.CLICK_MERCHANT_ID,
            merchant_user_id=config.CLICK_MERCHANT_USER_ID,
            secret_key=config.CLICK_SECRET_KEY,
            is_test_mode=config.IS_TEST_MODE
        )
    }
