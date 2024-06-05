# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

import subprocess
from dataclasses import dataclass
from typing import List
from os.path import expanduser

from anki.sound import AVTag, TTSTag
from aqt import mw
from aqt.sound import av_player

import aqt.tts
import json

# we subclass the default voice object to store the speechd language code
@dataclass
class CliVoice(aqt.tts.TTSVoice):
    cmd: list[str]

#class CliVoicePlayer(TTSProcessPlayer):
class CliVoicePlayer(aqt.tts.TTSProcessPlayer):
    # this is called the first time Anki tries to play a TTS file
    def get_available_voices(self) -> List[aqt.tts.TTSVoice]:
        voices = []
        with open(expanduser("~/.config/anki-tts-shell.json"), "r") as config_file:
            for voice in json.loads(config_file.read())["voices"]:
                voices.append(CliVoice(**voice))
        return voices  # type: ignore

    # this is called on a background thread, and will not block the UI
    def _play(self, tag: AVTag) -> None:
        #get the avtag
        assert isinstance(tag, TTSTag)
        match = self.voice_for_tag(tag)
        text = tag.field_text.strip()
        if match and hasattr(match.voice, "cmd") and text:
            subprocess.run(match.voice.cmd, input=text.encode('utf-8'))

# register our handler
av_player.players.append(CliVoicePlayer(mw.taskman))
