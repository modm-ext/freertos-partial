# Script is tested on OS X 10.12
# YOUR MILEAGE MAY VARY

import sys
import shutil
import fnmatch
import subprocess
from pathlib import Path

source_paths = [
    "FreeRTOS/Source/portable/GCC/ARM_CM0",
    "FreeRTOS/Source/portable/GCC/ARM_CM3",
    "FreeRTOS/Source/portable/GCC/ARM_CM4F",
    "FreeRTOS/Source/portable/GCC/ARM_CM7",
    "FreeRTOS/Source/portable/MemMang/*.c",
    "FreeRTOS/Source/include/*.h",
    "FreeRTOS/Source/*.c",
    "FreeRTOS/License",
]

source_paths_tcp = [
	"FreeRTOS-Plus/Source/FreeRTOS-Plus-TCP/portable/BufferManagement",
	"FreeRTOS-Plus/Source/FreeRTOS-Plus-TCP/portable/Compiler/GCC",
	"FreeRTOS-Plus/Source/FreeRTOS-Plus-TCP/include/*.h",
	"FreeRTOS-Plus/Source/FreeRTOS-Plus-TCP/tools",
	"FreeRTOS-Plus/Source/FreeRTOS-Plus-TCP/*.c",
	"FreeRTOS-Plus/Source/FreeRTOS-Plus-TCP/LICENSE_INFORMATION.txt",
]

# clone the repository
print("Cloning FreeRTOS repository...")
if not Path("freertos_src").exists():
    subprocess.run("git clone --jobs=8 --recurse-submodules https://github.com/freertos/freertos.git freertos_src", shell=True)

# remove the sources in this repo
if Path("FreeRTOS").exists():
    shutil.rmtree("FreeRTOS")
if Path("FreeRTOS-Plus-TCP").exists():
    shutil.rmtree("FreeRTOS-Plus-TCP")

print("Copying FreeRTOS sources...")
for pattern in source_paths:
    for path in Path("freertos_src").glob(pattern):
        dest = path.relative_to("freertos_src")
        dest.parent.mkdir(parents=True, exist_ok=True)
        if path.is_dir():
            shutil.copytree(path, dest)
        else:
            shutil.copy2(path, dest)

print("Copying FreeRTOS-Plus-TCP sources...")
for pattern in source_paths_tcp:
    for path in Path("freertos_src").glob(pattern):
        dest = path.relative_to("freertos_src/FreeRTOS-Plus/Source")
        dest.parent.mkdir(parents=True, exist_ok=True)
        if path.is_dir():
            shutil.copytree(path, dest)
        else:
            shutil.copy2(path, dest)

print("Normalizing FreeRTOS newlines and whitespace...")
subprocess.run("sh ./post_script.sh > /dev/null 2>&1", shell=True)

print("Apply FreeRTOS-Plus-TCP patch...")
subprocess.run("git apply -v --ignore-whitespace FreeRTOS_IP.c.patch", shell=True)
