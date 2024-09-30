library("pacman")
pacman::p_load(baseballr)

load_data <- function() {
    # Specify your data loading logic here
    # Return value: loaded dataframe
    df <- mlb_schedule(season = 2024, level_ids = "1")
    print(df)
}
