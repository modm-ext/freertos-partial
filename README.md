# FreeRTOS partial tree

This is just a partial copy of the freertos repository to reduce repository size.
The following paths are extracted:

## FreeRTOS

- `FreeRTOS/Source/portable/GCC/ARM_CM0`
- `FreeRTOS/Source/portable/GCC/ARM_CM3`
- `FreeRTOS/Source/portable/GCC/ARM_CM4F`
- `FreeRTOS/Source/portable/GCC/ARM_CM7`
- `FreeRTOS/Source/portable/GCC/ARM_CM33_NTZ`
- `FreeRTOS/Source/portable/MemMang/*.c`
- `FreeRTOS/Source/include/*.h`
- `FreeRTOS/Source/*.c`
- `FreeRTOS/License`

## FreeRTOS-Plus-TCP

- `FreeRTOS-Plus-TCP/source/portable/BufferManagement`
- `FreeRTOS-Plus-TCP/source/portable/Compiler/GCC`
- `FreeRTOS-Plus-TCP/source/include/*.h`
- `FreeRTOS-Plus-TCP/source/*.c`
- `FreeRTOS-Plus-TCP/tools/tcp_utilities/**/tcp_*`
- `FreeRTOS-Plus-TCP/LICENSE.md`

The kernel and Plus-TCP are git submodules of the FreeRTOS LTS repository and
are checked out explicitly by `update.py`.

This repository is updated periodically by GitHub Actions.
