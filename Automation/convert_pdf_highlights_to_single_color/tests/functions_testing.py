import sys, pymupdf, pytest
sys.path.append("..")
from convert_pdf_highlights_to_single_color import is_rectangles_overlap, merge_rectangles, merg_pass

def test_is_rectangles_overlap():
    assert is_rectangles_overlap(pymupdf.Rect((50, 100, 500, 1000)), pymupdf.Rect((50, 70, 500, 1000))) == True
    assert is_rectangles_overlap(pymupdf.Rect((10, 100, 500, 1000)), pymupdf.Rect((500, 70, 1500, 2000))) == False
    assert is_rectangles_overlap(pymupdf.Rect((0, 0, 0, 0)), pymupdf.Rect((0, 0, 0, 0))) == False
    assert is_rectangles_overlap(pymupdf.Rect((10, 10, 10, 10)), pymupdf.Rect((10, 10, 10, 10))) == False
    assert is_rectangles_overlap(pymupdf.Rect((0, 0, 25, 25)), pymupdf.Rect((20, 20, 50, 50))) == True
    assert is_rectangles_overlap(pymupdf.Rect((0, 0, 25, 25)), pymupdf.Rect((25, 20, 50, 50))) == False
    

def test_merge_rectangles():
    assert merge_rectangles(pymupdf.Rect((0, 0, 0, 0)), pymupdf.Rect((0, 0, 0, 0))) == pymupdf.Rect((0,0,0,0))
    assert merge_rectangles(pymupdf.Rect((10, 10, 10, 10)), pymupdf.Rect((10, 10, 10, 10))) == pymupdf.Rect((10, 10, 10, 10))
    assert merge_rectangles(pymupdf.Rect((0, 100, 200, 200)), pymupdf.Rect((50, 100, 300, 300))) == pymupdf.Rect((0, 100, 300, 300))
    assert merge_rectangles(pymupdf.Rect((500, 500, 1000, 2000)), pymupdf.Rect((200, 200, 700, 1500))) == pymupdf.Rect((200, 200, 1000, 2000))

def test_merg_pass():
    assert merg_pass( [pymupdf.Rect(0,0,50,50), pymupdf.Rect(25,25,75,75), pymupdf.Rect(200,200,300,300)]) == [pymupdf.Rect(0.0, 0.0, 75.0, 75.0), pymupdf.Rect(200.0, 200.0, 300.0, 300.0)]
    assert merg_pass( [pymupdf.Rect(0,0,50,50), pymupdf.Rect(25,25,75,75), pymupdf.Rect(60,60,100,100)]) == [pymupdf.Rect(0, 0, 100, 100)]
    assert merg_pass( [pymupdf.Rect(100,100,200,200), pymupdf.Rect(200,200,500,500), pymupdf.Rect(600,500,1000,1000)]) == [pymupdf.Rect(100,100,200,200), pymupdf.Rect(200,200,500,500), pymupdf.Rect(600,500,1000,1000)]