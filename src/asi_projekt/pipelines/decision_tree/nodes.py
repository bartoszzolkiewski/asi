"""
This is a boilerplate pipeline 'decision_tree'
generated using Kedro 0.18.9
"""

import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> DecisionTreeClassifier:
	model = DecisionTreeClassifier()
	param_grid = {
		"min_samples_split": [2, 3, 4, 5],
		"min_samples_leaf": [2, 3, 4, 5],
        "splitter": ['best'],
	}
    
	grid_search = GridSearchCV(model, param_grid, cv=3, n_jobs=-1, verbose=10)
	grid_search.fit(X_train, y_train)
	return grid_search.best_estimator_


def evaluate_model(model: DecisionTreeClassifier, X_test: pd.DataFrame, y_test: pd.Series) -> dict:
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    return {
        'accuracy': {'value': accuracy, 'step': 0},
    }
