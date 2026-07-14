import pandas as pd
from data_loader import data_load_filter
from models import model_choosing
from pipeline import testing

# DM_per_capita_classe: material damage discretized
# PEPL_per_capita_classe: public loss discretized
# PEPR_per_capita_classe: private loss discretized
# PCT_DH_diretos_classe: human damage percentage discretized
target_list = ["DM_per_capita_classe", "PEPL_per_capita_classe", "PEPR_per_capita_classe", "PCT_DH_diretos_classe"]
modelos_para_testar = ["dt", "rf", "nn", "xgboost"]
versoes_dataset = [1, 2, 3]
filters = ["0_to_4", "0_and_1", "1_to_4"]

dataset_version = {
    1: "data/v1.csv",
    2: "data/v2.csv",
    3: "data/v3.csv"
}

final_results = []

for versao in versoes_dataset:
    file_path = dataset_version.get(versao)
    
    for filter in filters:
        for alvo in target_list:
            
            df_rodada = data_load_filter(file_path, alvo, versao, filter)
            if df_rodada is None:
                continue
                
            for nome_mod in modelos_para_testar:
                print(f"Dataset V{versao} | Filter: {filter} | Target: {alvo} | Model: {nome_mod}")
                
                # model choosing
                modelo = model_choosing(nome_mod)
                
                # cross-validation
                metricas = testing(df_rodada, alvo, modelo)
                
                # metrics validation
                if metricas is not None:
                    metricas.update({
                        "Dataset_Versao": versao,
                        "Filtro_Classe": filter,
                        "Alvo": alvo,
                        "Modelo": nome_mod
                    })
                    final_results.append(metricas)
                else:
                    print(f"Insufficiente amount of data (lines: {len(df_rodada)})")

if len(final_results) > 0:
    df_resultados = pd.DataFrame(final_results)
    df_resultados.to_csv("experiments_results.csv", index=False)
else:
    print("Error: no result was saved.")