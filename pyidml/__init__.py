import copy
from pyidml.models import Document
from lxml import etree
import zipfile

__version__ = '0.3-dev'
__homepage__ = 'https://github.com/guardian/pyidml'

PACKAGING_NS = '{http://ns.adobe.com/AdobeInDesign/idml/1.0/packaging}'

def load_files(fh):
    """
    Load a zip file into a dicionary of filenames to etree objects.
    """
    d = {}
    zf = zipfile.ZipFile(fh, 'r')
    for filename in zf.namelist():
        if filename.endswith('.xml'):
            d[filename] = etree.fromstring(zf.read(filename))
    return d

def normalize(element_in, files):
    """
    Recursively load all external idPkg references in `element` from `files` 
    into one tree.
    """
    # Copy the element first, as modifying it directly causes problems.
    element = copy.deepcopy(element_in)
    for i, child in enumerate(element):
        # Processing instructions have a function as their tag attribute.
        if isinstance(child.tag, basestring) and child.tag.startswith(PACKAGING_NS):
            src = child.get('src')
            if src is not None:
                root = copy.copy(files[src])
                root.tag = root.tag.replace(PACKAGING_NS, '')
                element[i] = root
        element[i] = normalize(element[i], files)
    return element
    

def parse(fh):
    """
    Returns a document object for a given IDML file handle.
    """
    files = load_files(fh)
    designmap = normalize(files['designmap.xml'], files)
    return Document.from_xml(designmap)


