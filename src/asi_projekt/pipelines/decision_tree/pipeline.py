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
                func=nodes.feature_scaling,
                inputs="model_input",
                outputs="model_input_scaled",
                name="scale_features_node",
            ),
            node(
                func=nodes.split_data,
                inputs=["model_input_scaled", "params:model_options"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            node(
                func=nodes.train_model,
                inputs=["X_train", "y_train"],
                outputs="decision_tree",
                name="train_model_node",
            ),
            node(
                func=nodes.evaluate_model,
                inputs=["decision_tree", "X_test", "y_test"],
                outputs=None,
                name="evaluate_model_node",
            ),
        ]
    )
