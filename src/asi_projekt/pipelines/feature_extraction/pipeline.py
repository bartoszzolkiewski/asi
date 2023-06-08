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
            )
        ]
    )
