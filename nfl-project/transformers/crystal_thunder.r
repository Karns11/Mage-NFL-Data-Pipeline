library("pacman")
p_load(dplyr)

transform <- function(df_1, ...) {
    team_def <- df_1
    colnames(team_def) <- team_def[1, ] 
    team_def <- team_def[-1, ]  

    team_def_df <- as.data.frame(team_def)

    any(duplicated(names(team_def_df)))

    names(team_def_df) <- make.unique(names(team_def_df))

    team_def_df_filtered <- team_def_df %>%
        filter(Rk != '')


    team_def_df_PERGAME <- team_def_df_filtered
    team_def_df_PERGAME[, 3:28] <- lapply(team_def_df_filtered[, 3:28], as.numeric)


    team_def_df_filtered[, 3:28] <- lapply(team_def_df_filtered[, 3:28], as.numeric)
    team_def_df_PERGAME[, 3:28] <- team_def_df_filtered[, 3:28] / team_def_df_filtered$G


    team_def_df_PERGAME$`Y/P` <- team_def_df_filtered$`Y/P`
    team_def_df_PERGAME$`NY/A` <- team_def_df_filtered$`NY/A`
    team_def_df_PERGAME$TD.1 <- team_def_df_filtered$TD.1
    team_def_df_PERGAME$`Y/A` <- team_def_df_filtered$`Y/A`
    team_def_df_PERGAME$`Sc%` <- team_def_df_filtered$`Sc%`
    team_def_df_PERGAME$`TO%` <- team_def_df_filtered$`TO%`
    team_def_df_PERGAME$G <- team_def_df_filtered$G

    team_def_df_PERGAME
}
