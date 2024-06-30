import pandas as pd # Importamos la librería pandas para manejar y analizar datos
import os # Importamos el modulo OS para interactuar con el sistema operativo.
from ..decorators.decorators import timeit, logit # Importamos los decoradores personalizados.

@logit # Añadimos el loggin a la funcion.
@timeit # Medimos el tiempo de ejecucion de la funcion
def load_data(data_path):
    """Cargar los datos desde un archivo CSV o excel , en nuestro caso el archivo "products.csv"""
    
    if data_path.endswith(".csv"):
        df = pd.read_csv(data_path) #Cargamos los datos del archivo CSV
    elif data_path.endswith(".xlsx"): 
        df = pd.read_excel(data_path) # Cargamos los datos del archivo excel
    else:
        raise ValueError("Unsupported file format") # Lanzamos un error si el formato del archivo NO es compatible
    # print("Data loaded successfully") # Imprimimos un mensaje indicando que los datos se cargaron correctamente
    return df #Devolvemos el DataFrame con los datos cargados

@logit # Añadimos el loggin a la funcion.
@timeit # Medimos el tiempo de ejecucion de la funcion
def clean_data(df):
    """Limpiamos los datos"""
    df["price"] = df["price"].replace(r"[\$,]" , "", regex=True).astype(float) # Limpiamos y convertimos la columna de precios a tipo float
   # print("Data cleaned Successfully")
    return df # Devolvemos el DataFrame con los datos formateados

@logit # Añadimos el loggin a la funcion.
@timeit # Medimos el tiempo de ejecucion de la funcion
def analyze_data(df):
    """Realizamos un analisis basico de datos,"""
   # print("Basic Data Anakysis:") # Imprimimos un encabezado para el analisis de datos
   # print(df.describe()) #Imprimimos un resumen estadistico de los datos.
   # print("\nProducts with highest prices: ") # Imprimimos un encabezado para los productos con los precios mas altos.
    highestPrices= df.nlargest(5, "price")
   # print(highestPrices) # Imprimimos los 5 productos con los precios mas altos.
    return highestPrices

@logit # Añadimos el loggin a la funcion.
@timeit # Medimos el tiempo de ejecucion de la funcion.
def save_clean_data(df, outputh_path):
    """Guardamos los datos limpios en un archivo CSV"""
    if outputh_path.endswith(".csv"):
       df.to_csv(outputh_path, index=False) # Guardamos los datos en un archivo CSV.
    elif outputh_path.endswith(" .xlsx"):
        df.to_excel(outputh_path, index=False) # Guardamos los datos en un archivo Excel.
    else:
        raise ValueError("Unsupported file format") # Lanzamos un error si el formato del archivo no es compatible
   # print(f"Clean data saved to {outputh_path}")    
    
if __name__ == "__main__": # Permitimos que el script solo se ejecute en este archivo.
    data_path = "data/raw/products.csv" # Definimos la ruta del archivo de datos SIN procesar.
    outputh_path = "data/processed/cleaned_products.csv" # Definimos la ruta del archivo de datos procesados
    
    df = load_data(data_path) # Cargamos los datos de un archivo especifico.
    df = clean_data(df) # Limpiamos los datos cargados
    analyze_data(df) # Realizamos un analisis basico de la data.
    os. makedirs("data/processed", exist_ok=True) # Creamos el directorio para los datos procesados si no existe
    save_clean_data(df, outputh_path) # Guardamos los datos limpios en el archivo especifico.