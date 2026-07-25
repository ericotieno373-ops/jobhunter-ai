from pathlib import Path

from pypdf import PdfReader


class CVService:
    def __init__(self, cv_path: str):
        self.cv_path = Path(cv_path)

    def load_text(self) -> str:
        if not self.cv_path.exists():
            raise FileNotFoundError(
                f"CV not found: {self.cv_path}"
            )

        reader = PdfReader(self.cv_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text