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

# clone the repository
print("Cloning FreeRTOS repository...")
if not Path("freertos_src").exists():
    subprocess.run("git clone https://github.com/cjlano/freertos.git freertos_src", shell=True)

# remove the sources in this repo
if Path("FreeRTOS").exists():
    shutil.rmtree("FreeRTOS")

print("Copying FreeRTOS sources...")
for pattern in source_paths:
    for path in Path("freertos_src").glob(pattern):
        dest = path.relative_to("freertos_src")
        dest.parent.mkdir(parents=True, exist_ok=True)
        if path.is_dir():
            shutil.copytree(path, dest)
        else:
            shutil.copy2(path, dest)

