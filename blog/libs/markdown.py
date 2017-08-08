import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html


class TocMixin:
    """TOC mixin for Renderer
    https://github.com/lepture/mistune-contrib/blob/master/mistune_contrib/toc.py
    """

    def reset_toc(self):
        self.toc_tree = []
        self.toc_count = 0

    def header(self, text, level, raw=None):
        rv = '<h%d id="toc-%d">%s</h%d>\n' % (
            level, self.toc_count, text, level
        )
        self.toc_tree.append((self.toc_count, text, level, raw))
        self.toc_count += 1
        return rv

    def render_toc(self, level=3):
        """Render TOC to HTML.
        :param level: render toc to the given level
        """
        return ''.join(self._iter_toc(level))

    def _iter_toc(self, level):
        first_level = None
        last_level = None

        if not self.toc_tree:
            return

        yield '<ul class="ui list table-of-content">\n'

        for toc in self.toc_tree:
            index, text, l, raw = toc

            if l > level:
                # ignore this level
                continue

            if first_level is None:
                # based on first level
                first_level = l
                last_level = l
                yield '<li><a href="#toc-%d">%s</a>' % (index, text)
            elif last_level == l:
                yield '</li>\n<li><a href="#toc-%d">%s</a>' % (index, text)
            elif last_level == l - 1:
                last_level = l
                yield '<ul>\n<li><a href="#toc-%d">%s</a>' % (index, text)
            elif last_level > l:
                # close indention
                yield '</li>'
                while last_level > l:
                    yield '</ul>\n</li>\n'
                    last_level -= 1
                yield '<li><a href="#toc-%d">%s</a>' % (index, text)

        # close tags
        yield '</li>\n'
        while last_level > first_level:
            yield '</ul>\n</li>\n'
            last_level -= 1

        yield '</ul>\n'


class HighlightMixin:
    """Code Highlight Mixin for Renderer"""

    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)


class Renderer(TocMixin, HighlightMixin, mistune.Renderer):
    pass
