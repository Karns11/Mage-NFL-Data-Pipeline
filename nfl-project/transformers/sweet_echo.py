if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd

@transformer
def transform(data, *args, **kwargs):

    data = pd.DataFrame(data)

    data = data.drop(columns=data.filter(like='Unnamed').columns)

    data.columns = (
        data.columns
        .str.replace(' ', '_')
        .str.lower()
    )

    #data = data[data['season'] == 2024].sort_values(by='week', ascending=False)


    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'