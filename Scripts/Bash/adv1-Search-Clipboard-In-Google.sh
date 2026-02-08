#!/bin/bash
# Description: Search the current clipboard content in Google
xdg-open "https://google.com/search?q=$(wl-paste)" 2>/dev/null
