@echo off
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
allure serve reports/allure-results

@REM allure generate reports/allure-results -o reports/allure-report --clean
@REM allure open reports/allure-report