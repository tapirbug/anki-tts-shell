# Anki TTS Speech Dispatcher
Add speech synthesis support via CLI tool to Anki.

You can configure it to use any CLI tool, language or voice you like, for example `spd-say` or `ekho`.

## Configuring voices
To add support for a new language, provide a configuration file

If you want to use a different tool like [ekho](https://eguidedog.net/ekho.php)
instead of `spd-say`, provide a configuration file in `~/.config/anki-tts-shell.json`.

For each language, provide a language code, and a command that can speak the text if it is written to the programs stdin:
```
{
    "voices": [
        {
            "code": "zh_CN",
            "cmd": [ "ekho", "--file=-" ]
        }
    ]
}
```

## Thanks
This add-on is based on the work of subdomain on https://github.com/sudomain/anki-TTS-speech-dispatcher