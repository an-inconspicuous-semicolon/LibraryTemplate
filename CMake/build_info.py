import os
import sys

output = os.popen("git config --global user.email")
email = output.read().replace("\n", '')

output = os.popen("git config --global user.name")
username = output.read().replace("\n", '')

output = os.popen("git log -1 --pretty=\"%H\"")
commit_id = output.read().replace("\n", '')

output = os.popen("cpp --version | head -n1")
compiler = output.read().replace("\n", '')

library_name = sys.argv[1] if len(sys.argv) > 1 else "Library"
library_version = sys.argv[2] if len(sys.argv) > 2 else "Unspecified"

print(f"""
--------------------
Build Information for {library_name} 
Version: {library_version}
Built by: {username} ({email})
Compiler: {compiler}
Commit ID: {commit_id}

--------------------
""")
