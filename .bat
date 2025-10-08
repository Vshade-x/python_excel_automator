@echo off
cls
echo.
echo ======================================================
echo           INICIANDO GENERADOR DE REPORTES
echo ======================================================

REM Llama al interprete de Python para ejecutar el script
"C:\Program Files\Python311\python.exe" generador_reportes.py

echo.
echo ======================================================
echo   PROCESO TERMINADO. Revisa el archivo reporte_ventas_filtrado.xlsx
echo ======================================================

pause