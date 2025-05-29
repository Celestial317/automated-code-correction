def wrap(text, cols):
    lines = []
    while len(text) > cols:
        end = text.rfind(' ', 0, cols + 1)
        if end == -1:
            end = cols
        line, text = text[:end], text[end:]
        lines.append(line)
    # After the loop, if there's any remaining text (which will be <= cols in length),
    # it needs to be added to the lines list.
    if text:
        lines.append(text)
    return lines