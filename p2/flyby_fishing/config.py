# GAME_TITLE = "Flyby Fishing"
#
# WIN_SCALE = 0.8
#
# FPS = 60
#
# MUSIC_VOLUME = 1.0

import json


class Config:
    data = {
        'GAME_TITLE': "Flyby Fishing",
        'WIN_SCALE': 0.8,
        'FPS': 60,
        'MUSIC_VOLUME': 0.5,
        'FISH_COUNT': 0
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


# with open('data.txt', 'w') as test_file:
#     json.dump(data, test_file)
#
# with open('data.txt') as test_file:
#     data = json.load(test_file)


# def load_data():
#     global data
#     try:
#         with open('config.txt') as config_file:
#             data = json.load(config_file)
#     except FileNotFoundError:
#         pass


# def save_data():
#     global data
#     with open("config.txt", 'w') as config_file:
#         json.dump(data, config_file)
