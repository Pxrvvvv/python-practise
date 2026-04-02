import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.dragon("Hello,"+ sys.argv[1]) # We can also use cowsay.tux() or cowsay.dragon() or cowsay.trex() or cowsay.turkey() instead of cowsay.cow()

