"""
This is a boilerplate pipeline 'feature_extraction'
generated using Kedro 0.18.9
"""

from kedro.pipeline import Pipeline, node, pipeline
from asi_projekt.pipelines.feature_extraction import nodes


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=nodes.set_column_types,
                inputs="merged_df_fixed",
                outputs="feature_dataframe",
                name="set_merged_df_column_types_node",
            ),
            node(
                func=nodes.attach_dummies,
                inputs="feature_dataframe",
                outputs="model_input",
                name="attach_dummies_for_categorical_node",
            ),
            node(
                func=nodes.feature_scaling,
                inputs="model_input",
                outputs="model_input_scaled",
                name="scale_features_node",
            ),
            node(
                func=nodes.export_schema,
                inputs="model_input_scaled",
                outputs="model_schema",
                name="export_schema_node",
            ),
            node(
                func=nodes.split_data,
                inputs=["model_input_scaled", "params:model_options"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
        ]
    )
