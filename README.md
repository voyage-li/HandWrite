# HandWrite

模仿手写字迹

- [pillow 库简单学习](https://www.osgeo.cn/pillow/reference/)

```python
ImageDraw.text(xy, text, fill=None, font=None, anchor=None, spacing=4, align='left', direction=None, features=None, language=None, stroke_width=0, stroke_fill=None, embedded_color=False)
```

xy -- 文本的锚点坐标。

text -- 要绘制的字符串。如果它包含任何换行符，则文本将传递到 multiline_text() 。

fill -- 用于文本的颜色。

font -- 安 ImageFont 实例。

anchor -- 文本锚点对齐方式。确定锚点相对于文本的相对位置。默认对齐方式为左上角。看见 文本锚点 有效值。对于非 TrueType 字体，此参数将被忽略。。。注意：此参数在 Pillow 的早期版本中存在，但仅在版本 8.0.0 中实现。

spacing -- 如果文本传递给 multiline_text() ，行之间的像素数。

align -- 如果将文本传递给 multiline_text() ， "left" ， "center" 或 "right" 。确定线条的相对对齐方式。使用 anchor 参数指定对齐方式。 xy 。

direction -- 文本的方向。它可以 "rtl" （从右到左）， "ltr" （从左到右）或 "ttb" （从上到下）。需要 libraqm。。版本 2.0 ADDED:：4

features -- 文本布局期间使用的 OpenType 字体功能的列表。例如，这通常用于打开默认情况下未启用的可选字体功能 "dlig" 或 "ss01" ，但也可以用于关闭默认字体功能，例如 "-liga" 禁用连字或 "-kern" 禁用字距调整。要获取所有支持的功能，请参阅 OpenType docs . 需要 libraqm。。版本 2.0 ADDED:：4

language -- 文本的语言。不同的语言可以使用不同的字形或连字。此参数告诉文本使用哪种语言的字体，并根据需要应用正确的替换（如果可用）。应该是一个 BCP 47 language code . 需要 libraqm。。版本添加：：6.0.0

stroke_width -- 文本笔划的宽度。。版本号：6.2.0

stroke_fill -- 用于文本笔划的颜色。如果未给出，将默认为 fill 参数。。版本号：6.2.0

embedded_color -- 是否使用字体嵌入颜色字形(COLR、CBDT、SBIX)。。。添加的版本：：8.0.0
