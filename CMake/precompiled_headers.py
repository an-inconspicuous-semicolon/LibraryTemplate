# argument 1: the name of the target
# argument 2: the absolute path to the sources list for the target
# argument 3: the absolute path to the output file

import sys
import re

if len(sys.argv) != 4:
    print("Usage: precompiled_headers.py target_name target_sources output_file")
    sys.exit(1)

# read the sources file
print("-- Generating precompiled header")
print("--- Reading target source list")
sources = []
try:
    handle = open(sys.argv[2], 'r')
    sources = handle.read().splitlines()
    handle.close()
except ...:
    print("Failed to read target source list")
    sys.exit(2)

print("--- Reading sources")
content = ""
try:
    for source in sources:
        handle = open(source, 'r')
        content += handle.read() + '\n'
        handle.close()
except ...:
    print("Failed to read sources")
    sys.exit(3)

define_matches = re.findall(
    r"#define(?:.|(?<=\\)\n)*",
    content
)

include_matches = re.findall(
    r"#include(?:[ \t]|\\\n)*<(?:[^>]|(?<=\\)\n)*>",  # black magic.
    content
)

include_matches = set(include_matches)
include_matches = sorted(include_matches)

define_matches = set(define_matches)
define_matches = sorted(define_matches)

output = "// Auto generated: Do not edit!\n\n" + "\n".join(define_matches) + "\n".join(include_matches)

print("--- Comparing old files")
old_file = ""
try:
    handle = open(sys.argv[3], 'r')
    old_file = handle.read()
    handle.close()
except FileNotFoundError:
    print("--- No previous precompiled header was found")
except ...:
    print("Failed to read target source list")
    sys.exit(2)

if old_file == output:
    print("--- No changes required")
    print("-- Generated precompiled header")
    sys.exit(0)

print("--- Writing Output")

try:
    handle = open(sys.argv[3], 'w')
    handle.write(output)
    handle.close()
except ...:
    print("Failed to write output")
    sys.exit(5)

print("-- Generated precompiled header")
