import pymupdf

doc = pymupdf.open("git_cheat.pdf")

for page in doc:
    for annote in page.annots():
        annote.set_colors(stroke=(1, 0, 0))
        annote.update()


def is_rectangles_overlap(rect1, rect2):
    if rect1.x0 >= rect2.x1 or rect1.x1 <= rect2.x0 or rect1.y0 >= rect2.y1 or rect1.y1 <= rect2.y0:
        return False
    return True

doc.save("output.pdf")