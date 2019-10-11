from intro import Title


# creates the high score page with the list of high scores saved in the json file
class HighScoreScreen:
    def __init__(self, ai_settings, screen, game_stats):
        # list of the scores
        self.score_text = []
        self.score_text.append(Title(ai_settings.bg_color, screen, 'High Scores'))
        for num, value in enumerate(game_stats.high_scores_all, 1):
            self.score_text.append(Title(ai_settings.bg_color, screen, str(num) + '.   ' + str(value),
                                         text_color=(0, 255, 0)))

        # Place each line of text down the screen, in the center
        y_offset = ai_settings.screen_height * 0.15
        for text in self.score_text:
            text.prep_image()
            text.image_rect.centerx = ai_settings.screen_width // 2
            text.image_rect.centery = y_offset
            y_offset += ai_settings.screen_height * 0.15

    def show_scores(self):
        for text in self.score_text:
            text.blitme()
