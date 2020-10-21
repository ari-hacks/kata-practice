from collections import Counter
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent.parent.absolute()))
# import utils.decorators as d
# import pytest
"""
Return the count of distinct case-insensitive alphabetic characters and numbers with duplicates
"""
#@d.do_twice
# @pytest.fixture
def duplicate_count(text):
    dict_text = {}
    for key,val in Counter(text.upper()).items():
        if val > 1 : 
            dict_text[key] = val
    return len(dict_text)
 
duplicate_count("aA11")
