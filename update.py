#!/usr/bin/env python3

import sys
import subprocess
from pathlib import Path

# wget -qL https://raw.githubusercontent.com/modm-ext/partial/main/partial.py
import partial
partial.keepalive()

repo = "FreeRTOS/FreeRTOS"
src = Path("freertos_src")
# Kernel and Plus-TCP are git submodules of the FreeRTOS LTS repository
submodules = ["FreeRTOS/Source", "FreeRTOS-Plus/Source/FreeRTOS-Plus-TCP"]

tag = partial.latest_release_tag(repo)
if "--fast" not in sys.argv:
    partial.clone_repo(repo, src, branch=tag)
    subprocess.check_call(["git", "-C", str(src), "submodule", "update",
                           "--init", "--depth=1", "--jobs=2", *submodules])

files = partial.copy_files(src, [
    "FreeRTOS/Source/portable/GCC/ARM_CM0/**/*",
    "FreeRTOS/Source/portable/GCC/ARM_CM3/**/*",
    "FreeRTOS/Source/portable/GCC/ARM_CM4F/**/*",
    "FreeRTOS/Source/portable/GCC/ARM_CM7/**/*",
    "FreeRTOS/Source/portable/GCC/ARM_CM33_NTZ/**/*",
    "FreeRTOS/Source/portable/MemMang/*.c",
    "FreeRTOS/Source/include/*.h",
    "FreeRTOS/Source/*.c",
    "FreeRTOS/License/**/*",
])
files += partial.copy_files(src / "FreeRTOS-Plus/Source", [
    "FreeRTOS-Plus-TCP/source/portable/BufferManagement/**/*",
    "FreeRTOS-Plus-TCP/source/portable/Compiler/GCC/**/*",
    "FreeRTOS-Plus-TCP/source/include/*.h",
    "FreeRTOS-Plus-TCP/tools/tcp_utilities/**/tcp_*",
    "FreeRTOS-Plus-TCP/source/*.c",
    "FreeRTOS-Plus-TCP/LICENSE.md",
])

for patch in sorted(Path("patches").glob("*.patch")):
    partial.apply_patch(patch)

partial.commit(files, tag)
