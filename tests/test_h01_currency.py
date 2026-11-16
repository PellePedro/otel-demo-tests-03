import json  # noqa: F401


def test_h01_cur_nok_0001(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NOK" in codes


def test_h01_cur_nzd_0002(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NZD" in codes


def test_h01_cur_php_0003(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PHP" in codes


def test_h01_cur_pln_0004(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PLN" in codes


def test_h01_cur_ron_0005(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RON" in codes


def test_h01_cur_rub_0006(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RUB" in codes


def test_h01_cur_sek_0007(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SEK" in codes


def test_h01_cur_sgd_0008(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SGD" in codes


def test_h01_cur_thb_0009(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "THB" in codes


def test_h01_cur_try_0010(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "TRY" in codes
