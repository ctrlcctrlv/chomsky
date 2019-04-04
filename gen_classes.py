import fontforge
import unicodedata

font = fontforge.open("Chomsky.sfd")
rarr = '→'
o = dict()

for g in font.glyphs():
    try:
        c = chr(g.unicode)
    except ValueError: continue

    nd = unicodedata.normalize('NFD', c)

    #print(g.glyphname, c, nd, rarr, list(c), list(nd))

    # i.e. if character can be decomposed into nd[0] (base) and nd[1] (mark)
    if len(list(nd)) == 2:
        if not nd[0] in o: o[nd[0]] = list()
        o[nd[0]].append(g.glyphname)

o['i'].append("dotlessi")
o['j'].append("dotlessj")
for g, e in sorted(o.items()):
    print("@{0} = [{0} {1}];".format(g, ' '.join(e)))


import string

consider = list(string.ascii_lowercase+string.ascii_uppercase)

if len(consider) != len(o.keys()):
    print("\n# Lonely letters")

for c in consider:
    if c not in o:
        print("@{0} = [{0}];".format(c))
