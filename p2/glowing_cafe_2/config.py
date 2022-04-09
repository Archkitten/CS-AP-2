import json


class Config:
    data = {
        'GAME_TITLE': "Glowing Cafe 2",
        'GAME_ICON': 'img/Zap.png',
        'WIN_SCALE': 0.40,
        'FPS': 60,
        'MUSIC_VOLUME': 0.5,
    }

    @classmethod
    def load_data(cls):
        try:
            with open('config.txt') as config_file:
                Config.data = json.load(config_file)
        except FileNotFoundError:
            pass
        except:
            pass

    @classmethod
    def save_data(cls):
        with open("config.txt", 'w') as config_file:
            json.dump(Config.data, config_file)
