@echo off
rem MS DOS Batch file to run BatchTool

rem Explanation of command-line flags:
rem
rem -Xrunjvm_profiler: Run the virtual machine profiler (jvmprofiler.dll).
rem
rem -Xms8m: Specify the initial size, in bytes, of the memory allocation pool = 8 Megs.
rem
rem -Xmx512m: Specify the maximum size, in bytes, of the memory allocation pool = 512 Megs.

java.exe -Xrunjvm_profiler -Xms8m -Xmx512m -jar batch.jar %*
