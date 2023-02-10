import requests
import pprint
import json

# TODO error handling, logging
# TODO input cok buyurse concurrent hale getirilebilir, suanlik o kadar buyuk bir input yok

# deprem olan 10 il, diger illerde istenirse eklenebilir
target_iller = {
    "46": "Kahramanmaraş",
    "27": "Gaziantep",
    "44": "Malatya",
    "21": "Diyarbakır",
    "79": "Kilis",
    "63": "Şanlıurfa",
    "02": "Adıyaman",
    "31": "Hatay",
    "80": "Osmaniye",
    "01": "Adana",
}


def get_ilceler(il_id: str) -> dict:
    ''' 
    il kodundan ilceleri cekme

    response object
    {'items': [{'id': 1107, 'ad': 'Afşin', 'ilId': 46}, {'id': 1694, 'ad': 'Türkoğlu', 'ilId': 46}],
    'hasError': False, 'message': 'İşlem Başarılı.'}
    '''

    ilceler = requests.get(
        "https://dehas-api.csb.gov.tr/api/HasarTespit/GetIleGoreIlceler?id={}".format(il_id)).json()["items"]
    # print(ilceler)  # debug
    return ilceler


def get_mahalleler(ilce_id: str) -> dict:
    '''
    ilce kodundan mahalleleri cekme
    '''

    mahalleler = requests.get(
        "https://dehas-api.csb.gov.tr/api/HasarTespit/GetIlceyeGoreMahalleler?id={}".format(ilce_id)).json()["items"]
    # print(mahalleler)  # debug
    return mahalleler


def get_results(mahalled_id: int, ilce_id: int, il_id: int) -> dict:
    '''
    mahlle id'sinden hasarli binalari cekme

    params
    curl ... --data-raw '{"sokak":"","binaNo":"","aramaTip":2,"ilKodu":21,"ilceKodu":2040,"mahalleKodu":19727}'

    response object
    {"liste":[{"uid":"1675859903081_11031","id":0,"il":"Diyarbakır","ilce":"Çermik","sokak":"MENZİL/1","mahalle":"ÇUKUR",
    "binaNo":"2A","durum":"Hasarsız","kullanimDurum":null,"fotoCount":null,"askiKodu":"FHCZN","itirazDurumu":"",
    "aciklama":"Hasarsız","tahliyeDurumu":"","deprem_adi":"Kahramanmaraş Pazarcık","deprem_siddeti":"7.7",
    "deprem_tarihi":"2023-02-06T00:00:00","planlanmisYikimSaati":null}],"hasError":false,"message":"İşlem Başarılı."}
    '''

    url = "https://dehas-api.csb.gov.tr/api/HasarTespit/HasarTespitAdresSorgu"
    # params = {"sokak": "", "binaNo": "", "aramaTip": 2,
    #           "ilKodu": 21, "ilceKodu": 2040, "mahalleKodu": 19727}

    try:
        params = {"sokak": "", "binaNo": "", "aramaTip": 2,
                  "ilKodu": il_id, "ilceKodu": ilce_id, "mahalleKodu": mahalled_id}
        resp = requests.post(url, json=params).json()
    except Exception as e:
        print(e)
    return resp


def get_all():
    ''' target_iller'de ki tum iller icin hasarli binalari cek '''

    results = []

    il_kodlari = list(target_iller.keys())

    # cok pythonic degil ama idare eder
    for il_id in il_kodlari:
        print("il_id: {}".format(il_id))  # debug
        ilceler = get_ilceler(il_id)
        # iceler icin loop
        for i in range(len(ilceler)):
            ilce_id = ilceler[i]['id']
            print("ilce_id: {}".format(ilce_id))  # debug
            mahalleler = get_mahalleler(ilce_id)
            # print("mahalleler: {}".format(mahalleler)) # debug
            for j in range(len(mahalleler)):
                mah_id = mahalleler[j]['id']
                print("mah_id: {}".format(mah_id))  # debug
                result = get_results(mah_id, ilce_id, il_id)["liste"]
                results.extend(result)
            # break
        # break

    # TODO dosyaya json olarak yaz
    with open('results.json', 'w') as f:
        f.write(json.dumps(results, indent=4))


def main():
    get_all()


main()
