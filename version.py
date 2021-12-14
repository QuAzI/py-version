__version__ = 'v1.0.0.0-dev'
__version_info__ = (1, 0, 0, 0)
__title__ = 'py-version'
__author__ = 'Just Me'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021 by Me'


def generate_rc() -> str:
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
      StringStruct(u'FileVersion', u'{__version_info__}'),
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
    print(generate_rc())
