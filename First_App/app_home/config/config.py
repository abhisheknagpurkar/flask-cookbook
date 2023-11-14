class BaseConfig(object):
    'Base Configuration Class'
    SECRET_KEY = 'random secret key'
    DEBUG = True
    TESTING = False
    NEW_CONFIG_VARIABLE = 'my value'


class ProductionConfig(BaseConfig):
    'Production Configuration Class'
    SECRET_KEY = open('./secret.txt').read()
    DEBUG = False


class StagingConfig(BaseConfig):
    'Staging Configuration Class'
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    'Development Configuration Class'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'random secret key'
