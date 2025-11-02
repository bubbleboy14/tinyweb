from .server import run_dez_webserver
from .util import succeed, succeed_sync, fail, redirect, local, cgi_get, cgi_dump, set_pre_close
from .memcache import getmem, setmem, delmem, clearmem, getcache
from .requesters import fetch, post
from .version import __version__