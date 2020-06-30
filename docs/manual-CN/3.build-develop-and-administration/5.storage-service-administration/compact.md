# Compact

本文档将为您介绍 Compact。

代码中有两种 Compact。一种叫做 minor compact（disable_auto_compactions=false），即写入时小规模的 sst 文件合并，主要保证短时间内的读速度。一种叫做 major compact（submit job compact），通常在凌晨进行，即所有 sst 文件和整体合并，主要保证未来几小时内的读速度。
