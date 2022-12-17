#!/bin/sh
python3 setValueBySensor.py temperature 200
python3 shell.py << EOF
RUN("examp.txt")
EOF