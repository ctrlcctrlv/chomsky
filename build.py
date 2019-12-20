import fontforge
import unicodedata
font = fontforge.open("Chomsky.sfd")

font.encoding = "UnicodeBMP"

def createSupSub(font, glyph, scPUA):
    font.createChar(scPUA)
    font.createChar(scPUA+1)

    font.selection.select(glyph)
    font.copyReference()
    font.selection.select(scPUA)
    font.paste()
    font[scPUA].transform(psMat.scale(0.65))
    font[scPUA].glyphname = glyph.glyphname + '.sub'
    font.selection.select(scPUA)
    font.copyReference()
    font.selection.select(scPUA+1)
    font.paste()
    font[scPUA+1].transform(psMat.translate(0,500-170))
    font[scPUA+1].glyphname = glyph.glyphname + '.sup'
    return scPUA+2

scPUA = 0xE500
for glyph in [font[ord(str(e))] for e in range(0,10)]:
    scPUA = createSupSub(font, glyph, scPUA)

names = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
subs = ["\u2070", "\u00b9", "\u00b2", "\u00b3"]+[chr(i) for i in range(ord("\u2074"), ord("\u207a"))]
sups = [chr(i) for i in range(ord("\u2080"), ord("\u208a"))]

fn = """
for i, e in enumerate(su{0}s):
    n = names[i]
    font.selection.select(font.findEncodingSlot(n+".su{0}"))
    font.copyReference()
    font.createChar(ord(e))
    font.selection.select(ord(e))
    font.paste()
"""
exec(fn.format("b"))
exec(fn.format("p"))

font.selection.select(("unicode","ranges"),0xE000,0xE0FF)
font.clear()
font.selection.all()
font.unlinkReferences()
font.removeOverlap()
font.mergeFeature("features.fea")
font.generate("dist/Chomsky.otf", flags=("opentype", "old-kern", "no-hints", "no-flex", "winkern"))
#font.generate("dist/ConsentManufacturer.ufo", flags=("opentype", "old-kern", "no-hints", "no-flex", "winkern"))
