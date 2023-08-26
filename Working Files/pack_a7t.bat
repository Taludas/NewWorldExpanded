@ECHO off

::this just sets the island name to the executing directories name. 
::if the island name should be fixed:
::set island_name="colony01_m_04"
call :set_islandname "%cd%"

ECHO Applying XML patches 
CD /D %island_name%
START /W xmltest gamedata_original.xml gamedata_patch.xml
MOVE /Y patched.xml gamedata.xml

ECHO Recompressing FileDBs...
START /W /B FileDBReader compress -f gamedata.xml -i ../a7t_Gamedata.xml -c 2 -y -o data
CD ..

ECHO Packing RDA...
START /B RdaConsole pack -f %island_name%/gamedata.data -o %island_name%.a7t -y -v 2
ECHO Finished Packing a7t!

:set_islandname
set island_name=%~n1
goto :eof