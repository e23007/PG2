# python3 convert.py produceSales.xlsx

import sys
import ezsheets

if len(sys.argv) < 2:
    sys.exit('Usage python convert.py src')

ss = ezsheets.upload(sys.argv[1])
ss.title = ss.title + '.conv'

ss.downloadAsPDF()