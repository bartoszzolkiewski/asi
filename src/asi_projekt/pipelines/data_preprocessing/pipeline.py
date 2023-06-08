"""
This is a boilerplate pipeline 'data_preprocessing'
generated using Kedro 0.18.9
"""

from asi_projekt.pipelines.data_preprocessing import nodes
from kedro.pipeline import Pipeline, node, pipeline


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=nodes.drop_previous_application_bad_columns,
                inputs="previous_application",
                outputs="previous_application_dropped",
                name="drop_previous_application_columns_node",
            ),
            node(
                func=nodes.drop_application_data_bad_columns,
                inputs="application_data",
                outputs="application_data_dropped",
                name="drop_application_data_columns_node",
            ),
            node(
                func=nodes.merge,
                inputs=["previous_application_dropped", "application_data_dropped"],
                outputs="merged_df",
                name="merge_previous_application_application_data_node",
            ),
            node(
                func=nodes.fix_merged_na,
                inputs="merged_df",
                outputs="merged_df_fixed",
                name="fix_merged_df_na_node",
            ),
        ]
    )
