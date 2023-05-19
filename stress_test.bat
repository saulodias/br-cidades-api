@echo off

set "JMETER_HOME=C:\Program Files\apache-jmeter-5.5"
set "TEST_PLAN=stress_test.jmx"
set "RESULTS_FILE=test_results.jtl"

if exist "%RESULTS_FILE%" (
    del "%RESULTS_FILE%"
    echo File "%RESULTS_FILE%" deleted.
)

python csv_generator.py

"%JMETER_HOME%\bin\jmeter" -n -t "%TEST_PLAN%" -l "%RESULTS_FILE%"