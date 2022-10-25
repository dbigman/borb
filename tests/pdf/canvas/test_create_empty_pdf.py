import unittest
from pathlib import Path

from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF
from tests.test_util import compare_visually_to_ground_truth, check_pdf_using_validator


class TestCreateEmptyPDF(unittest.TestCase):
    """
    This test attempts to extract the text of each PDF in the corpus
    """

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        # find output dir
        p: Path = Path(__file__).parent
        while "output" not in [x.stem for x in p.iterdir() if x.is_dir()]:
            p = p.parent
        p = p / "output"
        self.output_dir = Path(p, Path(__file__).stem.replace(".py", ""))
        if not self.output_dir.exists():
            self.output_dir.mkdir()

    def test_write_document(self):

        # create empty document
        pdf: Document = Document()

        # create empty page
        page: Page = Page()

        # add page to document
        pdf.add_page(page)

        # write
        out_file = self.output_dir / "output.pdf"
        with open(out_file, "wb") as pdf_file_handle:
            PDF.dumps(pdf_file_handle, pdf)

        # compare visually
        compare_visually_to_ground_truth(out_file)
        check_pdf_using_validator(out_file)


if __name__ == "__main__":
    unittest.main()
