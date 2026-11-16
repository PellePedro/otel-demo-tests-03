import json  # noqa: F401


def test_h03_l9ecav7kim_nok_0001(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_2zyfj3gm2n_nzd_0002(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_0puk6v6ev0_php_0003(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_ls4psxunum_pln_0004(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_9siqt8tojo_ron_0005(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_6e92zmyyfz_rub_0006(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_hqtgwgpnh4_sek_0007(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_oljcespc7z_sgd_0008(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_66vchsjnup_thb_0009(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_1ymwwn1n4o_try_0010(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_l9ecav7kim_usd_0011(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 21
    assert product["priceUsd"]["nanos"] == 950000000


def test_h03_2zyfj3gm2n_zar_0012(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_0puk6v6ev0_aud_0013(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_ls4psxunum_bgn_0014(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_9siqt8tojo_brl_0015(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_6e92zmyyfz_cad_0016(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_hqtgwgpnh4_chf_0017(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_oljcespc7z_cny_0018(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_66vchsjnup_czk_0019(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_1ymwwn1n4o_dkk_0020(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_l9ecav7kim_eur_0021(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_2zyfj3gm2n_gbp_0022(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_0puk6v6ev0_hkd_0023(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_ls4psxunum_hrk_0024(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_9siqt8tojo_huf_0025(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_6e92zmyyfz_idr_0026(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_hqtgwgpnh4_ils_0027(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_oljcespc7z_inr_0028(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_66vchsjnup_isk_0029(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_1ymwwn1n4o_jpy_0030(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_l9ecav7kim_krw_0031(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_2zyfj3gm2n_mxn_0032(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_0puk6v6ev0_myr_0033(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_ls4psxunum_nok_0034(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_9siqt8tojo_nzd_0035(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_6e92zmyyfz_php_0036(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_hqtgwgpnh4_pln_0037(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_oljcespc7z_ron_0038(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_66vchsjnup_rub_0039(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_1ymwwn1n4o_sek_0040(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_l9ecav7kim_sgd_0041(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_2zyfj3gm2n_thb_0042(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_0puk6v6ev0_try_0043(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_ls4psxunum_usd_0044(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 57
    assert product["priceUsd"]["nanos"] == 80000000


def test_h03_9siqt8tojo_zar_0045(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_6e92zmyyfz_aud_0046(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_hqtgwgpnh4_bgn_0047(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_oljcespc7z_brl_0048(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_66vchsjnup_cad_0049(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_1ymwwn1n4o_chf_0050(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_l9ecav7kim_cny_0051(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_2zyfj3gm2n_czk_0052(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_0puk6v6ev0_dkk_0053(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_ls4psxunum_eur_0054(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_9siqt8tojo_gbp_0055(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_6e92zmyyfz_hkd_0056(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_hqtgwgpnh4_hrk_0057(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_oljcespc7z_huf_0058(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_66vchsjnup_idr_0059(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_1ymwwn1n4o_ils_0060(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_l9ecav7kim_inr_0061(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_2zyfj3gm2n_isk_0062(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_0puk6v6ev0_jpy_0063(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_ls4psxunum_krw_0064(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_9siqt8tojo_mxn_0065(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_6e92zmyyfz_myr_0066(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_hqtgwgpnh4_nok_0067(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_oljcespc7z_nzd_0068(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_66vchsjnup_php_0069(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_1ymwwn1n4o_pln_0070(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_l9ecav7kim_ron_0071(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_2zyfj3gm2n_rub_0072(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_0puk6v6ev0_sek_0073(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_ls4psxunum_sgd_0074(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_9siqt8tojo_thb_0075(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_6e92zmyyfz_try_0076(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_hqtgwgpnh4_usd_0077(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 0
    assert product["priceUsd"]["nanos"] == 990000000


def test_h03_oljcespc7z_zar_0078(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_66vchsjnup_aud_0079(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_1ymwwn1n4o_bgn_0080(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_l9ecav7kim_brl_0081(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_2zyfj3gm2n_cad_0082(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_0puk6v6ev0_chf_0083(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_ls4psxunum_cny_0084(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_9siqt8tojo_czk_0085(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_6e92zmyyfz_dkk_0086(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_hqtgwgpnh4_eur_0087(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_oljcespc7z_gbp_0088(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_66vchsjnup_hkd_0089(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_1ymwwn1n4o_hrk_0090(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_l9ecav7kim_huf_0091(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_2zyfj3gm2n_idr_0092(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_0puk6v6ev0_ils_0093(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_ls4psxunum_inr_0094(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_9siqt8tojo_isk_0095(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_6e92zmyyfz_jpy_0096(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_hqtgwgpnh4_krw_0097(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_oljcespc7z_mxn_0098(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_66vchsjnup_myr_0099(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_1ymwwn1n4o_nok_0100(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_l9ecav7kim_nzd_0101(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_2zyfj3gm2n_php_0102(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_0puk6v6ev0_pln_0103(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_ls4psxunum_ron_0104(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_9siqt8tojo_rub_0105(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_6e92zmyyfz_sek_0106(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_hqtgwgpnh4_sgd_0107(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_oljcespc7z_thb_0108(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_66vchsjnup_try_0109(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_1ymwwn1n4o_usd_0110(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 129
    assert product["priceUsd"]["nanos"] == 950000000


def test_h03_l9ecav7kim_zar_0111(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_2zyfj3gm2n_aud_0112(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_0puk6v6ev0_bgn_0113(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_ls4psxunum_brl_0114(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_9siqt8tojo_cad_0115(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_6e92zmyyfz_chf_0116(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_hqtgwgpnh4_cny_0117(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_oljcespc7z_czk_0118(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_66vchsjnup_dkk_0119(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_1ymwwn1n4o_eur_0120(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_l9ecav7kim_gbp_0121(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_2zyfj3gm2n_hkd_0122(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_0puk6v6ev0_hrk_0123(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_ls4psxunum_huf_0124(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_9siqt8tojo_idr_0125(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_6e92zmyyfz_ils_0126(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_hqtgwgpnh4_inr_0127(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_oljcespc7z_isk_0128(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_66vchsjnup_jpy_0129(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_1ymwwn1n4o_krw_0130(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_l9ecav7kim_mxn_0131(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_2zyfj3gm2n_myr_0132(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_0puk6v6ev0_nok_0133(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_ls4psxunum_nzd_0134(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_9siqt8tojo_php_0135(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_6e92zmyyfz_pln_0136(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_hqtgwgpnh4_ron_0137(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_oljcespc7z_rub_0138(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_66vchsjnup_sek_0139(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_1ymwwn1n4o_sgd_0140(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_l9ecav7kim_thb_0141(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_2zyfj3gm2n_try_0142(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_0puk6v6ev0_usd_0143(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 175
    assert product["priceUsd"]["nanos"] == 0


def test_h03_ls4psxunum_zar_0144(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_9siqt8tojo_aud_0145(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_6e92zmyyfz_bgn_0146(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_hqtgwgpnh4_brl_0147(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_oljcespc7z_cad_0148(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_66vchsjnup_chf_0149(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_1ymwwn1n4o_cny_0150(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_l9ecav7kim_czk_0151(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_2zyfj3gm2n_dkk_0152(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_0puk6v6ev0_eur_0153(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_ls4psxunum_gbp_0154(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_9siqt8tojo_hkd_0155(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_6e92zmyyfz_hrk_0156(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_hqtgwgpnh4_huf_0157(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_oljcespc7z_idr_0158(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_66vchsjnup_ils_0159(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_1ymwwn1n4o_inr_0160(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_l9ecav7kim_isk_0161(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_2zyfj3gm2n_jpy_0162(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_0puk6v6ev0_krw_0163(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_ls4psxunum_mxn_0164(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_9siqt8tojo_myr_0165(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_6e92zmyyfz_nok_0166(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_hqtgwgpnh4_nzd_0167(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_oljcespc7z_php_0168(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_66vchsjnup_pln_0169(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_1ymwwn1n4o_ron_0170(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_l9ecav7kim_rub_0171(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_2zyfj3gm2n_sek_0172(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_0puk6v6ev0_sgd_0173(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_ls4psxunum_thb_0174(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_9siqt8tojo_try_0175(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_6e92zmyyfz_usd_0176(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 69
    assert product["priceUsd"]["nanos"] == 950000000


def test_h03_hqtgwgpnh4_zar_0177(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_oljcespc7z_aud_0178(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_66vchsjnup_bgn_0179(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_1ymwwn1n4o_brl_0180(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_l9ecav7kim_cad_0181(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_2zyfj3gm2n_chf_0182(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_0puk6v6ev0_cny_0183(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_ls4psxunum_czk_0184(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_9siqt8tojo_dkk_0185(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_6e92zmyyfz_eur_0186(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_hqtgwgpnh4_gbp_0187(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_oljcespc7z_hkd_0188(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_66vchsjnup_hrk_0189(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_1ymwwn1n4o_huf_0190(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_l9ecav7kim_idr_0191(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_2zyfj3gm2n_ils_0192(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_0puk6v6ev0_inr_0193(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_ls4psxunum_isk_0194(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_9siqt8tojo_jpy_0195(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_6e92zmyyfz_krw_0196(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_hqtgwgpnh4_mxn_0197(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_oljcespc7z_myr_0198(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_66vchsjnup_nok_0199(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_1ymwwn1n4o_nzd_0200(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_l9ecav7kim_php_0201(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_2zyfj3gm2n_pln_0202(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_0puk6v6ev0_ron_0203(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_ls4psxunum_rub_0204(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_9siqt8tojo_sek_0205(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_6e92zmyyfz_sgd_0206(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_hqtgwgpnh4_thb_0207(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_oljcespc7z_try_0208(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_66vchsjnup_usd_0209(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 349
    assert product["priceUsd"]["nanos"] == 950000000


def test_h03_1ymwwn1n4o_zar_0210(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_l9ecav7kim_aud_0211(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_2zyfj3gm2n_bgn_0212(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_0puk6v6ev0_brl_0213(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_ls4psxunum_cad_0214(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_9siqt8tojo_chf_0215(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_6e92zmyyfz_cny_0216(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_hqtgwgpnh4_czk_0217(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_oljcespc7z_dkk_0218(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_66vchsjnup_eur_0219(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_1ymwwn1n4o_gbp_0220(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_l9ecav7kim_hkd_0221(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_2zyfj3gm2n_hrk_0222(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_0puk6v6ev0_huf_0223(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_ls4psxunum_idr_0224(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_9siqt8tojo_ils_0225(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_6e92zmyyfz_inr_0226(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_hqtgwgpnh4_isk_0227(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_oljcespc7z_jpy_0228(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_66vchsjnup_krw_0229(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_1ymwwn1n4o_mxn_0230(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_l9ecav7kim_myr_0231(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_2zyfj3gm2n_nok_0232(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_0puk6v6ev0_nzd_0233(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_ls4psxunum_php_0234(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_9siqt8tojo_pln_0235(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_6e92zmyyfz_ron_0236(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_hqtgwgpnh4_rub_0237(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_oljcespc7z_sek_0238(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_66vchsjnup_sgd_0239(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_1ymwwn1n4o_thb_0240(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_l9ecav7kim_try_0241(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_2zyfj3gm2n_usd_0242(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 209
    assert product["priceUsd"]["nanos"] == 950000000


def test_h03_0puk6v6ev0_zar_0243(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_ls4psxunum_aud_0244(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_9siqt8tojo_bgn_0245(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_6e92zmyyfz_brl_0246(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_hqtgwgpnh4_cad_0247(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_oljcespc7z_chf_0248(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_66vchsjnup_cny_0249(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_1ymwwn1n4o_czk_0250(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_l9ecav7kim_dkk_0251(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_2zyfj3gm2n_eur_0252(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_0puk6v6ev0_gbp_0253(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_ls4psxunum_hkd_0254(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_9siqt8tojo_hrk_0255(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_6e92zmyyfz_huf_0256(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_hqtgwgpnh4_idr_0257(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_oljcespc7z_ils_0258(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_66vchsjnup_inr_0259(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_1ymwwn1n4o_isk_0260(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_l9ecav7kim_jpy_0261(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_2zyfj3gm2n_krw_0262(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_0puk6v6ev0_mxn_0263(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_ls4psxunum_myr_0264(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_9siqt8tojo_nok_0265(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_6e92zmyyfz_nzd_0266(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_hqtgwgpnh4_php_0267(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_oljcespc7z_pln_0268(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_66vchsjnup_ron_0269(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_1ymwwn1n4o_rub_0270(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_l9ecav7kim_sek_0271(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_2zyfj3gm2n_sgd_0272(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_0puk6v6ev0_thb_0273(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_ls4psxunum_try_0274(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_9siqt8tojo_usd_0275(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 3599
    assert product["priceUsd"]["nanos"] == 0


def test_h03_6e92zmyyfz_zar_0276(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_hqtgwgpnh4_aud_0277(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_oljcespc7z_bgn_0278(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_66vchsjnup_brl_0279(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_1ymwwn1n4o_cad_0280(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_l9ecav7kim_chf_0281(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_2zyfj3gm2n_cny_0282(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_0puk6v6ev0_czk_0283(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_ls4psxunum_dkk_0284(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_9siqt8tojo_eur_0285(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_6e92zmyyfz_gbp_0286(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_hqtgwgpnh4_hkd_0287(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_oljcespc7z_hrk_0288(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_66vchsjnup_huf_0289(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_1ymwwn1n4o_idr_0290(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_l9ecav7kim_ils_0291(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_2zyfj3gm2n_inr_0292(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_0puk6v6ev0_isk_0293(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_ls4psxunum_jpy_0294(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_9siqt8tojo_krw_0295(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_6e92zmyyfz_mxn_0296(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_hqtgwgpnh4_myr_0297(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_oljcespc7z_nok_0298(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_66vchsjnup_nzd_0299(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_1ymwwn1n4o_php_0300(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_l9ecav7kim_pln_0301(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_2zyfj3gm2n_ron_0302(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_0puk6v6ev0_rub_0303(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_ls4psxunum_sek_0304(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_9siqt8tojo_sgd_0305(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_6e92zmyyfz_thb_0306(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_hqtgwgpnh4_try_0307(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_oljcespc7z_usd_0308(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 101
    assert product["priceUsd"]["nanos"] == 960000000


def test_h03_66vchsjnup_zar_0309(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_1ymwwn1n4o_aud_0310(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_l9ecav7kim_bgn_0311(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_2zyfj3gm2n_brl_0312(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_0puk6v6ev0_cad_0313(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_ls4psxunum_chf_0314(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_9siqt8tojo_cny_0315(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_6e92zmyyfz_czk_0316(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_hqtgwgpnh4_dkk_0317(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_oljcespc7z_eur_0318(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_66vchsjnup_gbp_0319(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_1ymwwn1n4o_hkd_0320(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "HKD"
