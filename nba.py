from nba_api.stats.endpoints import playercareerstats

class NBA(object):
    @staticmethod
    def get_ad_stats():
        career = playercareerstats.PlayerCareerStats(player_id='203076')
        df = career.get_data_frames()[0]
        return df
    
    def get_games():
        pass
