import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    基礎 Config
    """
    UPLOAD_FOLDER = '/path/to/the/uploads'
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    DEBUG = False
    CSRF_ENABLE = True
    SECRET_KEY = "dsff" #os. getenv("SECRET")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir,"sqlalchemy_main.db")

class Development(Config):
    """
    開發人員環境
    debug = True
    """
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'sqlalchemy_test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class StagingConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    """
    
    """
    DEBUG = False
    TESTING = False

app_config = dict(
    development = Development,
    testing = TestingConfig,
    staging = StagingConfig,
    production = ProductionConfig,
)