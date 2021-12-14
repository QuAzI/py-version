import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.version import (
    generate_rc
)


def test_generate_rc():
    assert generate_rc('v1.2.3.4-deadbeef-dev') == """VSVersionInfo(
  ffi=FixedFileInfo(
  filevers=(1, 2, 3, 4),
  prodvers=(1, 2, 3, 4),
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
      [StringStruct(u'CompanyName', u'Just Me'),
      StringStruct(u'FileDescription', u'py-version'),
      StringStruct(u'FileVersion', u'1.2.3.4'),
      StringStruct(u'InternalName', u'py-version'),
      StringStruct(u'LegalCopyright', u'Copyright 2021 by Me'),
      StringStruct(u'OriginalFilename', u'py-version.exe'),
      StringStruct(u'ProductName', u'py-version'),
      StringStruct(u'ProductVersion', u'v1.2.3.4-deadbeef-dev')])
    ]),
    VarFileInfo([VarStruct(u'Translation', [1033, 1049])])
  ]
)"""
