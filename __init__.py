# this __init__.py is only meant for local package development
try:
    from .lib_cast import *
# this we need for pip install --install-option test
except ImportError:
    import lib_cast
