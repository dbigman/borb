import io
from typing import List, Union

from ptext.io.read.read_any_object_transformer import (
    ReadAnyObjectTransformer,
)
from ptext.io.write.write_any_object_transformer import (
    WriteAnyObjectTransformer,
)
from ptext.pdf.canvas.event.event_listener import EventListener
from ptext.pdf.document import Document


class PDF:
    """
    The Portable Document Format (PDF) is a file format developed by Adobe in 1993 to present documents,
    including text formatting and images, in a manner independent of application software, hardware, and operating systems.
    Based on the PostScript language, each PDF file encapsulates a complete description of a fixed-layout flat document,
    including the text, fonts, vector graphics, raster images and other information needed to display it.
    PDF was standardized as ISO 32000 in 2008, and no longer requires any royalties for its implementation.

    PDF files may contain a variety of content besides flat text and graphics including logical structuring elements,
    interactive elements such as annotations and form-fields, layers, rich media (including video content),
    and three-dimensional objects using U3D or PRC, and various other data formats.

    The PDF specification also provides for encryption and digital signatures,
    file attachments, and metadata to enable workflows requiring these features.
    """

    @staticmethod
    def loads(
        file: Union[io.BufferedIOBase, io.RawIOBase],
        event_listeners: List[EventListener] = [],
    ) -> Document:
        return ReadAnyObjectTransformer().transform(
            file, parent_object=None, context=None, event_listeners=event_listeners
        )

    @staticmethod
    def dumps(file: Union[io.BufferedIOBase, io.RawIOBase], document: Document) -> None:
        WriteAnyObjectTransformer().transform(
            object_to_transform=document, context=None, destination=file
        )
