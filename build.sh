#!/bin/bash
>&2 echo Compressing SFD…
>&2 echo Building…
fontforge -lang=py -script build.py
if [[ "$STOP" =~ ^[Yy]$ ]]; then
    exit
fi
# Generate a WOFF, if posssible
hash sfnt2woff 2>/dev/null && sfnt2woff dist/Chomsky.otf

INSTALLDIR=$HOME/.fonts/c
if [[ "$INSTALL" =~ ^[Yy]$ ]]; then
    mkdir -p $INSTALLDIR
    cp dist/Chomsky.otf $INSTALLDIR
    echo cp dist/Chomsky.otf $INSTALLDIR
    >&2 echo "Installed"
fi

cd tex
./gen.sh
if [[ "$VIEW" =~ ^[Yy]$ ]]; then
    okular chomsky.pdf
fi
cd ..
