import os

import matplotlib
from matplotlib import font_manager


def test_import_sets_font():
    """import 시 한글 폰트가 자동 설정되는지 확인."""
    import koreanize_matplotlib  # noqa: F401

    assert matplotlib.rcParams['font.family'] == ['NanumGothic']
    assert matplotlib.rcParams['axes.unicode_minus'] is False


def test_font_path_exists():
    """폰트 파일 경로가 실제로 존재하는지 확인."""
    from koreanize_matplotlib import get_font_path, get_font_ttf_path

    assert os.path.isdir(get_font_path())
    assert os.path.isfile(get_font_ttf_path())


def test_font_registered():
    """NanumGothic 폰트가 matplotlib에 등록되었는지 확인."""
    import koreanize_matplotlib  # noqa: F401

    font_names = [f.name for f in font_manager.fontManager.ttflist]
    assert 'NanumGothic' in font_names
