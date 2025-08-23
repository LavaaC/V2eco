from v2eco.mod_io import load_mod


def test_load_mod(tmp_path):
    text = """
    california = {
        owner = USA
        goods = {
            grain = 10
            timber = 5
        }
    }
    texas = {
        owner = MEX
        goods = {
            cotton = 8
        }
    }
    """
    p = tmp_path / "test.mod"
    p.write_text(text)
    states = load_mod(str(p))
    assert len(states) == 2
    ca = next(s for s in states if s.name == "california")
    assert ca.owner == "USA"
    grain = next(g for g in ca.goods if g.name == "grain")
    assert grain.craftsmen == 10
