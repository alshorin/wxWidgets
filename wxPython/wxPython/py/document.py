"""Document class."""

__author__ = "Patrick K. O'Brien <pobrien@orbtech.com>"
__cvsid__ = "$Id$"
__revision__ = "$Revision$"[11:-2]

import os

try:
    True
except NameError:
    True = 1==1
    False = 1==0


class Document:
    """Document class."""

    def __init__(self, filename=None):
        """Create a Document instance."""
        self.filename = filename
        self.filepath = None
        self.filedir = None
        self.filebase = None
        self.fileext = None
        if self.filename:
            self.filepath = os.path.abspath(self.filename)
            self.filedir, self.filename = os.path.split(self.filepath)
            self.filebase, self.fileext = os.path.splitext(self.filename)

    def read(self):
        """Return contents of file."""
        f = file(self.filepath, 'rb')
        try:
            return f.read()
        finally:
            f.close()

    def write(self, text):
        """Write text to file."""
        try:
            f = file(self.filepath, 'wb')
            f.write(text)
        finally:
            if f:
                f.close()
