if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import nfl_data_py as nfl


@data_loader
def load_data(*args, **kwargs):

    now = kwargs.get('execution_date')

    year = int(now.strftime("%Y"))

    try:

        years_list = [year - 5, year - 4, year - 3, year - 2, year - 1, year]

        pbp_data = nfl.import_pbp_data(years_list)

        print('current year worked. List used:', years_list)
    
    except NameError:

        years_list = [year - 5, year - 4, year - 3, year - 2, year - 1]

        pbp_data = nfl.import_pbp_data(years_list)

        print('current year did NOT work. List used:', years_list)


    return pbp_data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
