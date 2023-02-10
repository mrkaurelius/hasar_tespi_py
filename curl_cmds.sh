#!/bin/bash

function hasar_tespit_sorgu(){
curl 'https://dehas-api.csb.gov.tr/api/HasarTespit/HasarTespitAdresSorgu' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'Access-Control-Allow-Origin: *' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -H 'DNT: 1' \
  -H 'Origin: https://hasartespit.csb.gov.tr' \
  -H 'Referer: https://hasartespit.csb.gov.tr/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-gpc: 1' \
  --data-raw '{"sokak":"","binaNo":"","aramaTip":2,"ilKodu":21,"ilceKodu":2040,"mahalleKodu":19727}' \
  --compressed
}


hasar_tespit_sorgu