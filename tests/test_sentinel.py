import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from datalayer_sentinel import validate_datalayer

class TestSentinel(unittest.TestCase):
    def test_val(self):
        dl = Path(__file__).resolve().parent.parent / "examples" / "sample_page_datalayer.json"
        sc = Path(__file__).resolve().parent.parent / "schema" / "ecommerce_datalayer_schema.json"
        ok, _ = validate_datalayer(str(dl), str(sc))
        self.assertTrue(ok)

if __name__ == "__main__":
    unittest.main()
