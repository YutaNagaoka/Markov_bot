#!/bin/sh

echo $1 | open_jtalk \
  -x <dictionary_data> \
  -m <voice_data> \
  -ow /dev/stdout \
  | aplay --quiet
