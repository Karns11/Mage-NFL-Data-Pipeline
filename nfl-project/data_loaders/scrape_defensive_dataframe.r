
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

    # any(duplicated(names(team_def_df)))

    # names(team_def_df) <- make.unique(names(team_def_df))

    # team_def_df_filtered <- team_def_df %>%
    #     filter(Rk != '')

    team_def_df
}
