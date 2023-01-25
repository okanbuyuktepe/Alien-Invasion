import pygame
from pygame import mixer


class Sound:
    """ A class to manage sounds for Alien Invasion."""

    def __init__(self):
        pass

    def play_sound(self, effect):
        """Play the sound."""
        mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()

        music = self._get_sound_file(effect)

        music.set_volume(0.3)
        music.play()

    def _get_sound_file(self, effect):
        """Return the sound file"""
        
        if effect == "ship_hit":
            return mixer.Sound("./sounds/ship_hit")
        elif effect == "new_level":
            return mixer.Sound("./sounds/new_level")
        elif effect == "fire_bullet":
            return mixer.Sound("./sounds/bullet_sound")
        elif effect == "play_button":
            return mixer.Sound("./sounds/play_button.wav")
        elif effect == "game_over":
            return mixer.Sound("./sounds/game_over.wav")
        elif effect == "game_background":
            return mixer.Sound("./sounds/game_background.wav")

    def play_background_music(self):
        """Play the game background music."""
        mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        music = self._get_sound_file("game_background")
        music.set_volume(0.2)
        music.play()

    def stop_sound(self):
        """ Stop all sounds."""
        mixer.stop()
