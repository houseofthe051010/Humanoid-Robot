from pathlib import Path
import pypdfium2 as pdfium
from pypdf import PdfReader

out=Path(__file__).parent/'drawings';out.mkdir(exist_ok=True)
refs={
 'GIM10015':Path(__file__).parent/'vendor_GIM10015'/'GIM10015'/'GIM10015-9 2D Drawing.pdf',
 'GIM6010':Path(r'C:\Users\rshan\Downloads\Planetary-Reduction-Motor\Planetary Reduction Motor\GIM6010-8\GIM6010-8\GIM6010-8  2D Drawing-Standard Version.pdf'),
}
for label,path in refs.items():
    reader=PdfReader(path)
    text='\n'.join(p.extract_text() for p in reader.pages)
    (out/(label+'.txt')).write_text(text,encoding='utf-8')
    doc=pdfium.PdfDocument(path)
    for i in range(len(doc)):
        doc[i].render(scale=2.5).to_pil().save(out/(label+'_'+str(i)+'.png'))
    print(label,text)
