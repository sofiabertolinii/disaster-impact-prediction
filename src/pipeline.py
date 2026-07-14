import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, balanced_accuracy_score

def testing(df, target, modelo):
    X = df.drop(columns=[target]).values
    y = df[target].values
    
    if len(df) < 20:
        return None

    kf = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
    balanced_accs, accs, f1s, precs, recs = [], [], [], [], []

    for train_index, test_index in kf.split(X, y):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        modelo.fit(X_train, y_train)
        y_pred = modelo.predict(X_test)

        balanced_accs.append(balanced_accuracy_score(y_test, y_pred))
        accs.append(accuracy_score(y_test, y_pred))
        f1s.append(f1_score(y_test, y_pred, average='weighted'))
        precs.append(precision_score(y_test, y_pred, average='weighted', zero_division=0))
        recs.append(recall_score(y_test, y_pred, average='weighted', zero_division=0))

    return {
        "acc": np.mean(accs),
        "f1": np.mean(f1s),
        "prec": np.mean(precs),
        "rec": np.mean(recs),
        "balanced_acc": np.mean(balanced_accs)
    }   