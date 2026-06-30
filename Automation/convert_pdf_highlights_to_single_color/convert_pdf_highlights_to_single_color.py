import pymupdf

def is_rectangles_overlap(rect1, rect2):
    if rect1.x0 >= rect2.x1 or rect1.x1 <= rect2.x0 or rect1.y0 >= rect2.y1 or rect1.y1 <= rect2.y0:
        return False
    return True

# returns biggest enclosing rectangle
def merge_rectangles(rect1, rect2):
    new_x0 = min(rect1.x0, rect2.x0)
    new_y0 = min(rect1.y0, rect2.y0)
    new_x1 = max(rect1.x1, rect2.x1)
    new_y1 = max(rect1.y1, rect2.y1)
    return pymupdf.Rect(new_x0, new_y0, new_x1, new_y1)

def merg_pass(rectangles):
    result = []
    
    for rect in rectangles:
        merged_flag = False
        overlap_index = None
        
        for i, result_rect in enumerate(result):
            if is_rectangles_overlap(rect, result_rect):
                overlap_index = i
                merged_flag = True
                break
        
        if merged_flag:
           result.append(merge_rectangles(rect, result[overlap_index]))
           result.pop(overlap_index)
        else:
            result.append(rect)
    
    return result

# if __name__ == "__main__":
#     doc = pymupdf.open("git_cheat.pdf")
#     for page in doc:
#         for annote in page.annots():
#             annote.set_colors(stroke=(1, 0, 0))
#             annote.update()

#     doc.save("output.pdf")

test_rects = [pymupdf.Rect(0,0,50,50), pymupdf.Rect(25,25,75,75), pymupdf.Rect(200,200,300,300)]
print(merg_pass(test_rects))