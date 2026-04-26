@ECHO off
SET /p filename=Enter the input file name (leave blank for 'crates.txt'):
IF "%filename%"=="" (
	SET filename=crates.txt
)
IF EXIST ".\py_fds_copy\%filename%" (
	ECHO Running script for file '%filename%'
	ECHO.
	CD py_fds_copy
	py -m main -filename %filename%
) ELSE (
	ECHO File does not exist
)
ECHO.
PAUSE