USE_LOCAL_SETTINGS = True

if USE_LOCAL_SETTINGS:
    from vision11.main_settings import *
else:
    from vision11.heroku_settings import *