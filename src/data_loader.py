import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# features lists for each dataset version
# each dataset version has its own specific features created in the iterative data science workflow
FEATURES_VERSOES = {
    1: ["Mês", "populacao", "grupo_de_desastre", "Ano", "Sigla_UF", "estacao_do_ano", "area_km2", "nino3.4", "evento", "soma"],
    2: ["Mês", "populacao", "grupo_de_desastre", "Ano", "Sigla_UF", "estacao_do_ano", "area_km2", "nino3.4", "evento",
        "Rio Gravataí","Rio dos Sinos","Rio Caí","Rio Taquari-Antas","Alto Jacuí","Bacia Hidrográfica dos Rios Vacacaí – Vacacaí Mirim",
        "Baixo Jacuí","Lago Guaíba","Rio Pardo","Rio Tramandaí","Litoral Médio","Rio Camaquã",
        "Bacia Hidrográfica da Lagoa Mirim e do Canal São Gonçalo","Rio Mampituba","Bacia Hidrográfica dos Rios Apuaê – Inhandava",
        "Rio Passo Fundo","Bacia Hidrográfica dos Rios Turvo – Santa Rosa – Santo Cristo","Rio Piratinim",
        "Rio Ibicuí","Rio Quaraí","Rio Santa Maria","Rio Negro","Rio Ijuí","Rio da Várzea","Rios Butuí – Icamaquã"],
    3: ["Mês", "populacao", "grupo_de_desastre", "Ano", "Sigla_UF", "estacao_do_ano", "area_km2", "nino3.4", "evento", 
        "IDHM", "cob_vegetal_2016",
        "Rio Gravataí","Rio dos Sinos","Rio Caí","Rio Taquari-Antas","Alto Jacuí","Bacia Hidrográfica dos Rios Vacacaí – Vacacaí Mirim",
        "Baixo Jacuí","Lago Guaíba","Rio Pardo","Rio Tramandaí","Litoral Médio","Rio Camaquã",
        "Bacia Hidrográfica da Lagoa Mirim e do Canal São Gonçalo","Rio Mampituba","Bacia Hidrográfica dos Rios Apuaê – Inhandava",
        "Rio Passo Fundo","Bacia Hidrográfica dos Rios Turvo – Santa Rosa – Santo Cristo","Rio Piratinim",
        "Rio Ibicuí","Rio Quaraí","Rio Santa Maria","Rio Negro","Rio Ijuí","Rio da Várzea","Rios Butuí – Icamaquã"]
}

# this function load and filter data
# file_path: represents the path to the dataset version
# target: represents wich target is being analized (public loss, private loss, human damage and material damage)
# dataset version: represents wich dataset version is being used for model training and evaluation (v1, v2, v3)
# test: represent wich class filtering configuration is being used
def data_load_filter(file_path, target, dataset_version, test):
    try:
        df = pd.read_csv(file_path, sep=",", low_memory=False, encoding='utf-8')
        if df.shape[1] <= 1:
            df = pd.read_csv(file_path, sep=";", low_memory=False, encoding='utf-8')
    except FileNotFoundError:
        print(f"Error: file not found: {file_path}")
        return None
    except Exception as e:
        try:
            df = pd.read_csv(file_path, sep=",", low_memory=False, encoding='latin1')
            if df.shape[1] <= 1:
                df = pd.read_csv(file_path, sep=";", low_memory=False, encoding='latin1')
        except Exception as e_latin:
            print(f"Error: {file_path}: {e_latin}")
            return None

    # apply the class filtering configuration
    # classes 0 and 1 represents a "yes/no" question
    if test == "0_and_1":
        df[target] = df[target].apply(lambda x: 1 if x > 0 else 0)
    
    # classes 1 to 4 represents how strong will the impact be
    elif test == "1_to_4":
        df = df[df[target] != 0]

    # selects the list of features corresponding to the chosen dataset version
    lista_features = FEATURES_VERSOES.get(dataset_version, [])
    features_para_uso = [col for col in lista_features if col != target and col in df.columns]

    if target not in df.columns:
        return None

    df_reduzido = df[features_para_uso + [target]].copy()

    # data cleaning
    for col in df_reduzido.columns:
        if df_reduzido[col].dtype == 'object' or str(df_reduzido[col].dtype) == 'string':
            if col in ["nino3.4", "anom", "populacao", "area_km2", "soma"]:
                df_reduzido[col] = pd.to_numeric(
                    df_reduzido[col].astype(str).str.replace(',', '.').str.extract(r'(-?\d+\.?\d*)')[0], 
                    errors='coerce'
                )
            else:
                df_reduzido[col] = df_reduzido[col].astype('category').cat.codes

    df_reduzido = df_reduzido.apply(pd.to_numeric, errors='coerce').fillna(0.0)

    # XGBoost class correction
    le = LabelEncoder()
    df_reduzido[target] = le.fit_transform(df_reduzido[target])
    
    return df_reduzido