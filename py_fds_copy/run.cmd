@ECHO off
SET /p filename=Enter the input file name (leave blank for 'crates.txt'):
IF "%filename%"=="" (
	SET filename=crates.txt
)
IF EXIST ".\%filename%" (
	ECHO Running script for file '%filename%'
	ECHO.
	py -m main -filename %filename%
) ELSE (
	ECHO File does not exist
)
ECHO.
PAUSE