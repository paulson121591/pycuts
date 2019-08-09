## set_draw_color ##

```python
fpdf.set_draw_color(r: int, g: int = -1, b: int = -1)
```

### Description ###

Defines the color used for all drawing operations (lines, rectangles and cell borders). It can be expressed in RGB components or gray scale. The method can be called before the first page is created and the value is retained from page to page.

### Parameters ###

r:
> If `g` and `b` are given, this indicates the red component; if not, this indicates the gray level. The value is between 0 and 255.

g:
> Green component (between 0 and 255).

b:
> Blue component (between 0 and 255).

### See also ###

[set_fill_color](set_fill_color.md), [set_text_color](set_text_color.md), [line](line.md), [rect](rect.md), [cell](cell.md), [multi_cell](multi_cell.md).
