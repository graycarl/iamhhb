try:
    import sass
except ImportError:
    raise Exception("You need to `pip install libsass` first")

import codecs
from pipeline.compilers import CompilerBase
from django.conf import settings


class LibSassCompiler(CompilerBase):
    """Compiler that uses libsass."""

    output_extension = 'css'

    def match_file(self, filename):
        """Check files extension to use them."""
        return filename.endswith(('.scss', '.sass'))

    def compile_file(self, infile, outfile, outdated=False, force=False):
        """Process sass file."""
        myfile = codecs.open(outfile, 'w', 'utf-8')

        if settings.DEBUG:
            myfile.write(sass.compile(filename=infile))
        else:
            myfile.write(sass.compile(filename=infile,
                                      output_style='compressed'))
        return myfile.close()
