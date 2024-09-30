library("pacman")
p_load(dplyr)

transform <- function(df_1, ...) {
    # Specify your transformation logic here
    # Return value: transformed dataframe.
    df_1$processdate <- global_vars['execution_date']

    df_1
}
