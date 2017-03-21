import sys

from samtools.render import only_render

'''##exemple of multi import form a folder
from samtools.render import (
    only_render,
    sauce,
    )
'''

# register the addon + modules found in globals() (taken from Amaranth addon)
bl_info = {
    "name": "Samtools",
    "author": "Samuel Bernou",
    "version": (0, 0, 1),
    "blender": (2, 78),
    "location": "Anywhere!",
    "description": "Complementary tools",
    "warning": "",
    "wiki_url": "",

    "tracker_url": "",
    "category": "Scene",
}


def _call_globals(attr_name):
    for m in globals().values():
        if hasattr(m, attr_name):
            getattr(m, attr_name)()


def _flush_modules(pkg_name):
    pkg_name = pkg_name.lower()
    for k in tuple(sys.modules.keys()):
        if k.lower().startswith(pkg_name):
            del sys.modules[k]


def register():
    _call_globals("register")


def unregister():
    _call_globals("unregister")
    _flush_modules("samtools")  # reload samtools
