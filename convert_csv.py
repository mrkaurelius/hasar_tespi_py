import json

example_rescord = '''
[
    {
        "uid": "1675926979855_62201",
        "id": 0,
        "il": "Kahramanmara\u015f",
        "ilce": "Af\u015fin",
        "sokak": "1009",
        "mahalle": "AF\u015e\u0130NBEY",
        "binaNo": "1",
        "durum": "Y\u0131k\u0131k",
        "kullanimDurum": null,
        "fotoCount": null,
        "askiKodu": "FFMJ8",
        "itirazDurumu": "",
        "aciklama": "Y\u0131k\u0131k",
        "tahliyeDurumu": "",
        "deprem_adi": "Kahramanmara\u015f Pazarc\u0131k",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "2023-02-06T00:00:00",
        "planlanmisYikimSaati": null
    }
]
'''


obj = json.loads(example_rescord)

# TODO