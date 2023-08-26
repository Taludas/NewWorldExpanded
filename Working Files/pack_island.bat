@ECHO off

::this just sets the island name to the executing directories name. 
::if the island name should be fixed:
::set island_name="colony01_m_04"
call :set_islandname "%cd%"

ECHO Applying XML patches 
CD /D %island_name%
START /W xmltest gamedata_original.xml gamedata_patch.xml
MOVE /Y patched.xml gamedata.xml
START /W xmltest rd3d_original.xml rd3d_patch.xml
MOVE /Y patched.xml rd3d.xml
CD ..
START /W xmltest %island_name%_original.xml %island_name%_patch.xml
MOVE /Y patched.xml %island_name%.xml

ECHO Recompressing FileDBs...
CD /D %island_name%
START /W /B FileDBReader compress -f gamedata.xml -i ../../Island_Gamedata.xml -c 2 -y -o data
START /W /B FileDBReader compress -f rd3d.xml -i ../../Island_RD3D.xml -c 2 -y -o data
CD ..

ECHO Packing RDA...
START /B RdaConsole pack -f %island_name%/gamedata.data %island_name%/rd3d.data -o %island_name%.a7m -y -v 2
START /W /B FileDBReader compress -f %island_name%.xml -o a7minfo -i ../a7minfo.xml -c 2 -y
DEL %island_name%.xml
ECHO Finished Packing Island!

:set_islandname
set island_name=%~n1
goto :eof