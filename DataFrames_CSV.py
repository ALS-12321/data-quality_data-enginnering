import pandas as pd

# Rutas de los archivos
file_paths = {
    'Hospital_Records': r'C:\Users\DREP\Downloads\Archivos CSV\Hospital_Records.txt',
    'Surgeries_and_Procedures': r'C:\Users\DREP\Downloads\Archivos CSV\Surgeries_and_Procedures.txt',
    'Laboratory_Examinations_Conducted': r'C:\Users\DREP\Downloads\Archivos CSV\Laboratory_Examinations_Conducted.txt',
    'Hospital_Pharmaceuticals': r'C:\Users\DREP\Downloads\Archivos CSV\Hospital_Pharmaceuticals.txt',
    'Patient_Clinical_History': r'C:\Users\DREP\Downloads\Archivos CSV\Patient_Clinical_History.txt',
    'Doctor_Profiles': r'C:\Users\DREP\Downloads\Archivos CSV\Doctor_Profiles.txt',
}

# Cargar y verificar datos
def load_and_verify_data(file_path):
    try:
        data = pd.read_csv(file_path, delimiter=',')  # Cambia el delimitador si es necesario
        return data
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {file_path}.")
    except pd.errors.ParserError as e:
        print(f"Error al analizar el archivo {file_path}: {e}")

# Cargar todos los DataFrames
dataframes = {name: load_and_verify_data(path) for name, path in file_paths.items()}

# Ejemplo de acceso a un DataFrame
for name, df in dataframes.items():
    if df is not None:
        print(f"DataFrame {name}:")
        print(df.head(101))
        print("\n")
