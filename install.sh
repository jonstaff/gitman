#!/bin/sh

if [ ! -d "/usr/local/bin" ]; then
  echo "/usr/local/bin does not exist"
  exit 1
fi

cp gitman /usr/local/bin || exit 1
chmod +x /usr/local/bin/gitman || exit 1

echo "Gitman successfully installed.  To view available commands, type:"
echo "\n  gitman -h"
