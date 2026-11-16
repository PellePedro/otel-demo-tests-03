import json  # noqa: F401


def test_h14_l9ecav7kim_eur_0001(api):
    resp = api.get("/api/recommendations", params={"productIds": ["L9ECAV7KIM"], "currencyCode": "EUR"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "L9ECAV7KIM" not in [product["id"] for product in products]


def test_h14_2zyfj3gm2n_gbp_0002(api):
    resp = api.get("/api/recommendations", params={"productIds": ["2ZYFJ3GM2N"], "currencyCode": "GBP"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "2ZYFJ3GM2N" not in [product["id"] for product in products]


def test_h14_0puk6v6ev0_hkd_0003(api):
    resp = api.get("/api/recommendations", params={"productIds": ["0PUK6V6EV0"], "currencyCode": "HKD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "0PUK6V6EV0" not in [product["id"] for product in products]


def test_h14_ls4psxunum_hrk_0004(api):
    resp = api.get("/api/recommendations", params={"productIds": ["LS4PSXUNUM"], "currencyCode": "HRK"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "LS4PSXUNUM" not in [product["id"] for product in products]


def test_h14_9siqt8tojo_huf_0005(api):
    resp = api.get("/api/recommendations", params={"productIds": ["9SIQT8TOJO"], "currencyCode": "HUF"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "9SIQT8TOJO" not in [product["id"] for product in products]


def test_h14_6e92zmyyfz_idr_0006(api):
    resp = api.get("/api/recommendations", params={"productIds": ["6E92ZMYYFZ"], "currencyCode": "IDR"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "6E92ZMYYFZ" not in [product["id"] for product in products]


def test_h14_hqtgwgpnh4_ils_0007(api):
    resp = api.get("/api/recommendations", params={"productIds": ["HQTGWGPNH4"], "currencyCode": "ILS"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "HQTGWGPNH4" not in [product["id"] for product in products]


def test_h14_oljcespc7z_inr_0008(api):
    resp = api.get("/api/recommendations", params={"productIds": ["OLJCESPC7Z"], "currencyCode": "INR"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "OLJCESPC7Z" not in [product["id"] for product in products]


def test_h14_66vchsjnup_isk_0009(api):
    resp = api.get("/api/recommendations", params={"productIds": ["66VCHSJNUP"], "currencyCode": "ISK"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "66VCHSJNUP" not in [product["id"] for product in products]


def test_h14_1ymwwn1n4o_jpy_0010(api):
    resp = api.get("/api/recommendations", params={"productIds": ["1YMWWN1N4O"], "currencyCode": "JPY"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "1YMWWN1N4O" not in [product["id"] for product in products]


def test_h14_l9ecav7kim_krw_0011(api):
    resp = api.get("/api/recommendations", params={"productIds": ["L9ECAV7KIM"], "currencyCode": "KRW"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "L9ECAV7KIM" not in [product["id"] for product in products]


def test_h14_2zyfj3gm2n_mxn_0012(api):
    resp = api.get("/api/recommendations", params={"productIds": ["2ZYFJ3GM2N"], "currencyCode": "MXN"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "2ZYFJ3GM2N" not in [product["id"] for product in products]


def test_h14_0puk6v6ev0_myr_0013(api):
    resp = api.get("/api/recommendations", params={"productIds": ["0PUK6V6EV0"], "currencyCode": "MYR"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "0PUK6V6EV0" not in [product["id"] for product in products]


def test_h14_ls4psxunum_nok_0014(api):
    resp = api.get("/api/recommendations", params={"productIds": ["LS4PSXUNUM"], "currencyCode": "NOK"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "LS4PSXUNUM" not in [product["id"] for product in products]


def test_h14_9siqt8tojo_nzd_0015(api):
    resp = api.get("/api/recommendations", params={"productIds": ["9SIQT8TOJO"], "currencyCode": "NZD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "9SIQT8TOJO" not in [product["id"] for product in products]


def test_h14_6e92zmyyfz_php_0016(api):
    resp = api.get("/api/recommendations", params={"productIds": ["6E92ZMYYFZ"], "currencyCode": "PHP"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "6E92ZMYYFZ" not in [product["id"] for product in products]


def test_h14_hqtgwgpnh4_pln_0017(api):
    resp = api.get("/api/recommendations", params={"productIds": ["HQTGWGPNH4"], "currencyCode": "PLN"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "HQTGWGPNH4" not in [product["id"] for product in products]


def test_h14_oljcespc7z_ron_0018(api):
    resp = api.get("/api/recommendations", params={"productIds": ["OLJCESPC7Z"], "currencyCode": "RON"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "OLJCESPC7Z" not in [product["id"] for product in products]


def test_h14_66vchsjnup_rub_0019(api):
    resp = api.get("/api/recommendations", params={"productIds": ["66VCHSJNUP"], "currencyCode": "RUB"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "66VCHSJNUP" not in [product["id"] for product in products]


def test_h14_1ymwwn1n4o_sek_0020(api):
    resp = api.get("/api/recommendations", params={"productIds": ["1YMWWN1N4O"], "currencyCode": "SEK"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "1YMWWN1N4O" not in [product["id"] for product in products]


def test_h14_l9ecav7kim_sgd_0021(api):
    resp = api.get("/api/recommendations", params={"productIds": ["L9ECAV7KIM"], "currencyCode": "SGD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "L9ECAV7KIM" not in [product["id"] for product in products]


def test_h14_2zyfj3gm2n_thb_0022(api):
    resp = api.get("/api/recommendations", params={"productIds": ["2ZYFJ3GM2N"], "currencyCode": "THB"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "2ZYFJ3GM2N" not in [product["id"] for product in products]


def test_h14_0puk6v6ev0_try_0023(api):
    resp = api.get("/api/recommendations", params={"productIds": ["0PUK6V6EV0"], "currencyCode": "TRY"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "0PUK6V6EV0" not in [product["id"] for product in products]


def test_h14_ls4psxunum_usd_0024(api):
    resp = api.get("/api/recommendations", params={"productIds": ["LS4PSXUNUM"], "currencyCode": "USD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "LS4PSXUNUM" not in [product["id"] for product in products]


def test_h14_9siqt8tojo_zar_0025(api):
    resp = api.get("/api/recommendations", params={"productIds": ["9SIQT8TOJO"], "currencyCode": "ZAR"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "9SIQT8TOJO" not in [product["id"] for product in products]
