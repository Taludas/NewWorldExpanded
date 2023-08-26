@ECHO off

call :set_islandname "%cd%"

ECHO compressing a7tinfo

::A7tinfo unpacking

START /W /B FileDBReader compress -f %island_name%.xml -c 2 -i ../a7tinfo.xml -y -o .a7tinfo

:set_islandname
set island_name=%~n1
goto :eof