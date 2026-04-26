@ECHO Tests:
@ECHO.
@python -m coverage run py_fds_copy\tests.py

@ECHO.
@ECHO ==========================================
@ECHO.
@ECHO Coverage report:
@ECHO.
@python -m coverage report --omit=py_fds_copy\tests.py
@PAUSE