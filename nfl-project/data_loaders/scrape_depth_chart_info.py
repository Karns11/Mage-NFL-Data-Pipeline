if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import nfl_data_py as nfl
import pandas as pd


@data_loader
def load_data(*args, **kwargs):

    depth_Chart = nfl.import_depth_charts([2024])

    return depth_Chart


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
