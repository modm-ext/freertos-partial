# FreeRTOS partial tree

This is just a partial copy of the freertos repository to reduce repository size.
The following paths are extracted:

## FreeRTOS
- `FreeRTOS/Source/portable/GCC/ARM_CM0`
- `FreeRTOS/Source/portable/GCC/ARM_CM3`
- `FreeRTOS/Source/portable/GCC/ARM_CM4F`
- `FreeRTOS/Source/portable/GCC/ARM_CM7`
- `FreeRTOS/Source/portable/MemMang/*.c`
- `FreeRTOS/Source/include/*.h`
- `FreeRTOS/Source/*.c`
- `FreeRTOS/License`

## FreeRTOS-Plus-TCP
- `FreeRTOS-PLUS-TCP/portable/BufferManagement`
- `FreeRTOS-PLUS-TCP/portable/Compiler/GCC`
- `FreeRTOS-PLUS-TCP/include/*.h`
- `FreeRTOS-PLUS-TCP/tools`
- `FreeRTOS-PLUS-TCP/*.c`
- `FreeRTOS-PLUS-TCP/LICENSE_INFORMATION.txt`

More paths may be added in the future.

This repository is updated monthly by TravisCI:
[![](https://travis-ci.org/modm-ext/freertos-partial.svg?branch=master)](https://travis-ci.org/modm-ext/freertos-partial)
