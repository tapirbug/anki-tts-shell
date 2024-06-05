ADDON_DIR := $(HOME)/.local/share/Anki2/addons21/anki-tts-shell

.PHONY: install
install:
	mkdir -p $(ADDON_DIR)
	cp -f __init__.py $(ADDON_DIR)
