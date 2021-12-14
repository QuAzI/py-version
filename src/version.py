import sys

"""
Version data. Similar to AssemblyInfo

Format:
  MAJOR_VERSION.MINOR_VERSION.PATCH.BUILD-sha1short-dev

Where MAJOR_VERSION and MINOR_VERSION versions you have to set depends on
  application roadmap and milestones
PATCH: 0 - alpha, 1 - beta, 2 - release candidate, 3 - release
BUILD - incremental build number
sha1short - 8 chars of sha1 to identify wich commit used
dev - optional tag to mark that it is not real release and made internally
  for tests

Please read https://semver.org/ for extra information
"""

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
      StringStruct(u'ProductVersion', u'{version}')])
    ]),
    VarFileInfo([VarStruct(u'Translation', [1033, 1049])])
  ]
)"""


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--get-head':
        print(version_head)
    else:
        if (len(sys.argv) > 1):
            print(generate_rc(sys.argv[1]))
        else:
            print(generate_rc())
