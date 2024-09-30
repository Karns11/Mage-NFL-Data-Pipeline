library("pacman")
p_load(rvest)
p_load(dplyr)

load_data <- function() {
    
    url <- "https://www.pro-football-reference.com/years/2024/opp.htm"
    web_page <- read_html(url)
    team_def <- web_page %>%
        html_node("table") %>%  
        html_table(fill = TRUE) 

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

    colnames(team_def_df_PERGAME) <- c("Rank", "Team", "Games", "PointsAllowed_pg", "YardsAllowed_pg", 
                                   "OffensivePlays_pg", "YardsPerOffensivePlay_pg", "Turnovers_pg", "FumblesLost_pg", 
                                   "FirstDowns_pg", "Completions_pg", "Attempts_pg", "PassingYards_pg", 
                                   "PassingTouchdowns_pg", "Interceptions_pg", "PassingNetYards_pa", 
                                   "PassingFirstDowns_pg", "RushingAttempts_pg", "RushingYards_pg", 
                                   "RushingTouchdowns_pg", "RushingYards_pa", 
                                   "RushingFirstDowns_pg", "Penalties_pg", "PenaltyYards_pg", 
                                   "PenaltyFirstDowns_pg", "OffensiveScore_perc", "Turnover_perc", 
                                   "EXP")

    team_def_df_PERGAME

}

