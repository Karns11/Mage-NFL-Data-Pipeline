if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import nfl_data_py as nfl


@data_loader
def load_data(*args, **kwargs):

    now = kwargs.get('execution_date')

    year = int(now.strftime("%Y"))

    years_list = [year]

    seasonal_data = nfl.import_seasonal_data(years_list)

    return seasonal_data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
