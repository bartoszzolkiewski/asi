"""
This is a boilerplate pipeline 'decision_tree'
generated using Kedro 0.18.9
"""

from kedro.pipeline import Pipeline, node, pipeline
from asi_projekt.pipelines.decision_tree import nodes

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=nodes.train_model,
                inputs=["X_train", "y_train", "params:grid_search_options"],
                outputs="decision_tree",
                name="train_decision_tree_model_node",
            ),
            node(
                func=nodes.evaluate_model,
                inputs=["decision_tree", "X_test", "y_test"],
                outputs="decision_tree_metrics",
                name="evaluate_decision_tree_model_node",
            ),
        ]
    )
