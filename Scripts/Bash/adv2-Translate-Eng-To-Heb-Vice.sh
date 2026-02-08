#!/bin/bash
# Description: Translate clipboard content between English and Hebrew
declare -A Lang
Lang=(["English"]="English" ["Hebrew"]="Hebrew")

PS3="Choose source language: "
select input_lang in "${!Lang[@]}"; do
    if [[ "$input_lang" == "English" ]]; then
        xdg-open "https://translate.google.com/?sl=en&tl=iw&text=$(wl-paste)" 2>/dev/null
        break
    else
        xdg-open "https://translate.google.com/?sl=iw&tl=en&text=$(wl-paste)" 2>/dev/null
        break
    fi
done
