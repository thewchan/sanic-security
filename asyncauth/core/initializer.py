from asyncauth.core.verification import verification_init
from asyncauth.lib.tortoise import tortoise_init


def initialize_auth(app):
    app.add_task(tortoise_init())
    app.add_task(verification_init())

