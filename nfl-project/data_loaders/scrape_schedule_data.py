if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import nfl_data_py as nfl

@data_loader
def load_data(*args, **kwargs):
    now = kwargs.get('execution_date')

    year = int(now.strftime("%Y"))

    year_list = [year]
    
    schedule_df = nfl.import_schedules(year_list)

    return schedule_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
