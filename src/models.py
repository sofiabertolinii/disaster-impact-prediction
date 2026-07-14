from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier

def model_choosing(nome_modelo, random_state=42):
    nome_modelo = nome_modelo.lower()
    if nome_modelo == "dt":
        return DecisionTreeClassifier(max_depth=5, random_state=random_state)
    elif nome_modelo == "rf":
        return RandomForestClassifier(n_estimators=100, max_depth=5, random_state=random_state)
    elif nome_modelo == "nn":
        return MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, random_state=random_state)
    elif nome_modelo == "xgboost":
        return XGBClassifier(random_state=random_state, eval_metric='mlogloss')
    else:
        raise ValueError(f"Modelo {nome_modelo} não reconhecido.")