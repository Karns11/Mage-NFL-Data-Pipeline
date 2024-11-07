if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd

@transformer
def transform(data, *args, **kwargs):
    
    year = kwargs.get('execution_date').strftime("%Y")

    year_int = int(year)
    
    weekly_nfl_data = data[data['season'] == year_int]

    positions_to_filter = ['RB', 'WR', 'TE', 'QB']





    #Rushing yards avg for each position
    
    rushing_yds_each_game = weekly_nfl_data.groupby(['opponent_team', 'week', 'position'], as_index=False)['rushing_yards'].sum()

    rushing_yds_each_game = rushing_yds_each_game[rushing_yds_each_game['position'].isin(positions_to_filter)]

    AVG_rushing_yds_each_game_ALL_POS = rushing_yds_each_game.groupby(['opponent_team', 'position'], as_index=False)['rushing_yards'].mean()

    AVG_rushing_yds_each_game_ALL_POS.rename(columns={'rushing_yards': 'AVG_rushing_yds_allowed', 'opponent_team': 'team'}, inplace=True)




    #receiving yards avg for each position
    
    receiving_yds_each_game = weekly_nfl_data.groupby(['opponent_team', 'week', 'position'], as_index=False)['receiving_yards'].sum()


    receiving_yds_each_game = receiving_yds_each_game[receiving_yds_each_game['position'].isin(positions_to_filter)]

    AVG_receiving_yds_each_game_ALL_POS = receiving_yds_each_game.groupby(['opponent_team', 'position'], as_index=False)['receiving_yards'].mean()

    AVG_receiving_yds_each_game_ALL_POS.rename(columns={'receiving_yards': 'AVG_receiving_yds_allowed', 'opponent_team': 'team'}, inplace=True)




    #passing yards avg for each position
    
    passing_yds_each_game = weekly_nfl_data.groupby(['opponent_team', 'week', 'position'], as_index=False)['passing_yards'].sum()


    passing_yds_each_game = passing_yds_each_game[passing_yds_each_game['position'].isin(positions_to_filter)]

    AVG_passing_yds_each_game_ALL_POS = passing_yds_each_game.groupby(['opponent_team', 'position'], as_index=False)['passing_yards'].mean()

    AVG_passing_yds_each_game_ALL_POS.rename(columns={'passing_yards': 'AVG_passing_yds_allowed', 'opponent_team': 'team'}, inplace=True)




    fantasy_points_each_game = weekly_nfl_data.groupby(['opponent_team', 'week', 'position'], as_index=False)['fantasy_points_ppr'].sum()

    fantasy_points_each_game = fantasy_points_each_game[fantasy_points_each_game['position'].isin(positions_to_filter)]

    AVG_fantasy_points_each_game_ALL_POS = fantasy_points_each_game.groupby(['opponent_team', 'position'], as_index=False)['fantasy_points_ppr'].mean()

    AVG_fantasy_points_each_game_ALL_POS.rename(columns={'fantasy_points_ppr': 'AVG_fantasy_points_ppr_allowed', 'opponent_team': 'team'}, inplace=True)



    FINAL_DF = pd.merge(AVG_rushing_yds_each_game_ALL_POS, AVG_receiving_yds_each_game_ALL_POS, how='left', on=['team', 'position'])

    FINAL_DF = pd.merge(FINAL_DF, AVG_passing_yds_each_game_ALL_POS, how='left', on=['team', 'position'])

    FINAL_DF = pd.merge(FINAL_DF, AVG_fantasy_points_each_game_ALL_POS, how='left', on=['team', 'position'])



    FINAL_DF['processdate'] = kwargs.get('execution_date').strftime("%Y-%m-%d")
    FINAL_DF['week'] = max(weekly_nfl_data['week'])

    return FINAL_DF


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
