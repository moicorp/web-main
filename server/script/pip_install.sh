#!/bin/bash

set -eux -o pipefail

pip3 install -r requirements.txt \
  --index-url https://repo.fury.io/emoji-gen/ --extra-index-url https://pypi.org/simple
