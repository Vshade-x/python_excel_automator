import pandas as pd
import os

# ==========================================================
# 1. CONFIGURACIÓN INICIAL Y PARÁMETROS
# ==========================================================

# Archivo de entrada y salida (asumiendo que están en la misma carpeta del script)
ARCHIVO_ENTRADA = 'datos_ventas.csv'
ARCHIVO_SALIDA = 'reporte_ventas_filtrado.xlsx'

# Columnas que queremos ver en el reporte final
COLUMNAS_REPORTE = ['Fecha', 'Producto', 'Total Venta']

# Criterio de automatización: Solo queremos ventas mayores o iguales a 500
VENTA_MINIMA_REQUERIDA = 500 

# ==========================================================
# 2. FUNCIÓN PRINCIPAL
# ==========================================================

def generar_reporte():
    print(f"Iniciando procesamiento de: {ARCHIVO_ENTRADA}...")
    
    # 2.1 Verificación de existencia del archivo
    if not os.path.exists(ARCHIVO_ENTRADA):
        print(f"❌ ERROR: El archivo '{ARCHIVO_ENTRADA}' no se encontró en la carpeta de ejecución.")
        print("Asegúrese de que el archivo CSV esté en la misma ubicación que el script.")
        return

    try:
        # 2.2 Cargar datos del CSV
        df = pd.read_csv(ARCHIVO_ENTRADA)

        # 2.3 CÁLCULO: Crea la columna 'Total Venta'
        df['Total Venta'] = df['Cantidad'] * df['Precio Unitario']

        # 2.4 FILTRADO: Automatiza el proceso seleccionando solo las ventas grandes
        df_filtrado = df[df['Total Venta'] >= VENTA_MINIMA_REQUERIDA]

        # 2.5 SELECCIÓN: Prepara el DataFrame final solo con las columnas requeridas
        df_reporte = df_filtrado[COLUMNAS_REPORTE]

        # 2.6 GUARDAR: Exporta el resultado a un nuevo archivo Excel
        df_reporte.to_excel(ARCHIVO_SALIDA, index=False)

        print("\n==============================================")
        print(f"✅ ¡ÉXITO! Reporte generado y guardado como: {ARCHIVO_SALIDA}")
        print(f"Filas procesadas (Originales): {len(df)}")
        print(f"Filas en el reporte final: {len(df_reporte)} (Ventas >= {VENTA_MINIMA_REQUERIDA})")
        print("==============================================")

    except KeyError as ke:
        print(f"\n❌ ERROR de Columna: Asegúrese de que todas las columnas '{ke}' existan en su CSV y en la lista 'COLUMNAS_REPORTE'.")
    except Exception as e:
        print(f"\n❌ Ocurrió un error inesperado durante el proceso: {e}")

# Ejecutar la función principal
if __name__ == "__main__":
    generar_reporte()