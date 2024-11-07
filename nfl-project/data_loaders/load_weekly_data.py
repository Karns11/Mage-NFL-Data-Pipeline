if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import nfl_data_py as nfl


@data_loader
def load_data(*args, **kwargs):

    now = kwargs.get('execution_date')

    year = int(now.strftime("%Y"))

    year_list = [year - 11, year - 10, year - 9, year - 8, year - 7, year - 6, year - 5, year - 4, year - 3, year - 2, year - 1, year]

    weekly_data = nfl.import_weekly_data(year_list)


    return weekly_data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
