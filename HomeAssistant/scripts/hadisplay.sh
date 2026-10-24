#!/bin/bash

(
  while true; do
    if [ -s /tmp/kiosk.png ]; then
      feh --fullscreen --hide-pointer --reload 10 /tmp/kiosk.png
    fi
    sleep 2
  done
) &
