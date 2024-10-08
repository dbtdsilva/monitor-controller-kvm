from collections import namedtuple


__version__ = "1.5.5"

_AppInfo = namedtuple("AppInfo", [
    'APP_NAME',
    'APP_AUTHOR',
    'APP_PUBLISHER',
    'APP_URL',
    'APP_VERSION'
])

APP_INFO = _AppInfo(
    APP_NAME="Swiss Windows Knife",
    APP_AUTHOR="Diogo Silva",
    APP_PUBLISHER="Diogo Silva",
    APP_URL="https://github.com/dbtdsilva/swiss-windows-knife",
    APP_VERSION=__version__
)
