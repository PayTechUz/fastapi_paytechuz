from environs import Env

env = Env()
env.read_env()

PAYME_ID = env.str("PAYME_ID")
PAYME_KEY = env.str("PAYME_KEY")

CLICK_SERVICE_ID = env.str("CLICK_SERVICE_ID")
CLICK_MERCHANT_ID = env.str("CLICK_MERCHANT_ID")
CLICK_MERCHANT_USER_ID = env.str("CLICK_MERCHANT_USER_ID")
CLICK_SECRET_KEY = env.str("CLICK_SECRET_KEY")

IS_TEST_MODE = env.bool("IS_TEST_MODE", True)
