import gzip
import zlib
from v2parser import parse_save


def _write_gzip(path, text):
    with gzip.open(path, 'wb') as fh:
        fh.write(text.encode('utf-8'))


def _write_zlib(path, text):
    with open(path, 'wb') as fh:
        fh.write(zlib.compress(text.encode('utf-8')))


def test_parse_save_gzip(tmp_path):
    content = 'player { name John score 10 } level 5'
    p = tmp_path / 'save.v2'
    _write_gzip(p, content)
    assert parse_save(str(p)) == {
        'player': {'name': 'John', 'score': '10'},
        'level': '5',
    }


def test_parse_save_zlib(tmp_path):
    content = 'outer { inner value }'
    p = tmp_path / 'savez.v2'
    _write_zlib(p, content)
    assert parse_save(str(p)) == {'outer': {'inner': 'value'}}
