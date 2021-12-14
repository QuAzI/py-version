import sys

__title__ = 'py-version'
__author__ = 'Just Me'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021 by Me'

version_head = '1.0.0'
__version__ = f'v{version_head}.0-dev'


def generate_rc(version=__version__) -> str:
    version_raw = "".join(
        filter(
            lambda s: str.isdigit(s) or s == '.',
            version.split('-')[0]
        )
    )
    __version_info__ = tuple(
        [int(n) for n in version_raw.split('.', maxsplit=5)]
    )

    return f"""VSVersionInfo(
  ffi=FixedFileInfo(
  filevers={__version_info__},
  prodvers={__version_info__},
  mask=0x3f,
  flags=0x0,
  OS=0x4,
  fileType=0x1,
  subtype=0x0,
  date=(0, 0)
  ),
  kids=[
    StringFileInfo(
    [
      StringTable(
      u'040904B0',
      [StringStruct(u'CompanyName', u'{__author__}'),
      StringStruct(u'FileDescription', u'{__title__}'),
      StringStruct(u'FileVersion', u'{version_raw}'),
      StringStruct(u'InternalName', u'{__title__}'),
      StringStruct(u'LegalCopyright', u'{__copyright__}'),
      StringStruct(u'OriginalFilename', u'{__title__}.exe'),
      StringStruct(u'ProductName', u'{__title__}'),
      StringStruct(u'ProductVersion', u'{__version__}')])
    ]),
    VarFileInfo([VarStruct(u'Translation', [1033, 1049])])
  ]
)
    """


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--get-head':
        print(version_head)
    else:
      if (len(sys.argv) > 1):
        print(generate_rc(sys.argv[1]))
      else:
        print(generate_rc())
