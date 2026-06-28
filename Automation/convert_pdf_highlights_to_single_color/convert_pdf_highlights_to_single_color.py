import pymupdf

doc = pymupdf.open("git_cheat.pdf")

for page in doc:
    for annote in page.annots():
        annote.set_colors(stroke=(1, 0, 0))
        annote.update()

doc.save("output.pdf")
