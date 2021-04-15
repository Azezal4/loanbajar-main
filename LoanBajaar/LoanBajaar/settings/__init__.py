try:
    from .local_settings import *
except:
    from .production_settings import *

#Temporary Settings
try:
    from .temporary_settings import *
except:pass