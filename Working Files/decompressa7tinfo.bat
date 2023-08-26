@ECHO off

call :set_islandname "%cd%"

ECHO decompressing a7tinfo

::A7tinfo unpacking

START /W FileDBReader decompress -f %island_name%.a7tinfo -i ../a7tinfo.xml -y

:set_islandname
set island_name=%~n1
goto :eof