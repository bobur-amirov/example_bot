from bot import dp
from middlewares.sub_check import CheckUserInChannel

if __name__ == "middlewares":
    dp.middleware.setup(CheckUserInChannel())