if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import nfl_data_py as nfl
import pandas as pd

@data_loader
def load_data(*args, **kwargs):

    win_totals = nfl.import_win_totals([2024])

    return win_totals


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'