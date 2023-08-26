@ECHO off

call :set_islandname "%cd%"

ECHO unpacking a7t

::A7M unpacking
START /W /B RdaConsole ^extract -f %island_name%.a7t -o %island_name% -y

CD /D %island_name%

START /W /B FileDBReader decompress -f gamedata.data -i ../a7t_Gamedata.xml -y 
MOVE /Y gamedata.xml gamedata_original.xml

IF NOT exist gamedata_patch.xml (
    ECHO ^<ModOps^> > gamedata_patch.xml 
    ECHO. >> gamedata_patch.xml
    ECHO ^<^/ModOps^> >> gamedata_patch.xml 
)

CD .. 

:set_islandname
set island_name=%~n1
goto :eof