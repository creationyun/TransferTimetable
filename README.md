# TransferTimetable 1.0.2

![Python application](https://github.com/creationyun/TransferTimetable/workflows/Python%20application/badge.svg)

The program compares the timetables of two stations to derive a transit timetable.

## How To Run

This program is written in Python 3.x, so you need to install Anaconda or Python. (Virtual environment recommended)

```shell
$ pip install -r requirements.txt
$ python transfer_timetable.py path/to/timetable1.txt path/to/timetable2.txt transfer_walk_minute
```

After running, the execution result is obtained when you transfer from the station whose timetable is `timetable1.txt`, to the station whose timetable is `timetable2.txt` within `transfer_walk_minute` minutes. If you want, you can also save it as a file.

For example, if you run the following command:

```shell
$ python transfer_timetable.py sinnae/weekday/6_sinnae.txt sinnae/weekday/gyeongchun_chuncheon.txt 2.5
```

A transfer timetable will be derived for when you arrive at Sinnae station on Line 6 and transfer on Gyeongchun Line for Chuncheon in 2.5 minutes.

## Internal Structure of the Timetable File

The timetable file structure is a text file and you can write as follows.

```
[Station] [Line name] [Weekday/Saturday/Sunday/Holiday] [Train's direction]
[Bound for] [Arrive time]
[Bound for] [Arrive time]
[Bound for] [Arrive time]
[Bound for] [Arrive time]
...
[Bound for] [Arrive time]
```

1. In the first line, you can enter the station name, line name, train's workweek type and direction.

   + Station: A name of subway station (e.g. Seoul_station, Victoria_station, ...)
   + Line name: A name of subway line (e.g. Metropolitan_Line, Circle_Line, ...)
   + Weekday/Saturday/Sunday/Holiday: The day which the timetable is in.
     + It is recommended to enter Sunday/Holiday together in the [Weekday/Saturday/Sunday/Holiday] field.
   + Direction of train: choose up or down
     + If you are unsure, you can also enter a representative (bound for) destination, such as For_Aldgate.
   
2. From the second line to the end, you can enter trains' destinations and arrival times.

This program recognizes the file contents as separated by spaces, so if they have spaces, enter them with underscores (_).

If you want to look for several example files, please refer to the sample files listed below.

## Sample Timetable Files

Timetable directory structure is as follows:

* sinnae: Seoul Metropolitan Subway - Sinnae station
  * weekday, saturday, sunday_holiday (Sunday and Holiday)
    * `6_eungam_loop.txt`: Seoul Metro Line 6 - For Eungam Loop
    * `6_sinnae.txt`: Seoul Metro Line 6 - Sinnae arrival
    * `gyeongchun_cheongnyangni.txt`: KORAIL Gyeongchun Line - For Sangbong or Cheongnyangni
    * `gyeongchun_chuncheon.txt`: KORAIL Gyeongchun Line - For Chuncheon
* imae: Seoul Metropolitan Subway - Imae station
  * weekday, weekend_holiday (Saturday, Sunday and Holiday)
    * `suinbundang_wangsimni.txt`: KORAIL Suin·Bundang Line - For Wangsimni
    * `suinbundang_incheon.txt`: KORAIL Suin·Bundang Line - For Incheon
    * `gyeonggang_pangyo.txt`: KORAIL Gyeonggang Line - For Pangyo
    * `gyeonggang_yeoju.txt`: KORAIL Gyeonggang Line - For Yeoju
* choji: Seoul Metropolitan Subway - Choji station
  * weekday, weekend_holiday (Saturday, Sunday and Holiday)
    * `4_danggogae.txt`: Seoul Metro/KORAIL Line 4 - For Danggogae
    * `4_oido.txt`: Seoul Metro/KORAIL Line 4 - For Oido
    * `seohae_sosa.txt`: Seohae Line - For Sosa
    * `seohae_wonsi.txt`: Seohae Line - For Wonsi
    * `suinbundang_wangsimni.txt`: KORAIL Suin·Bundang Line - For Wangsimni
    * `suinbundang_incheon.txt`: KORAIL Suin·Bundang Line - For Incheon
* daegok: Seoul Metropolitan Subway - Daegok station
  * weekday, weekend_holiday (Saturday, Sunday and Holiday)
    * `3_daehwa.txt`: Seoul Metro/KORAIL Line 3 - For Daehwa
    * `3_ogeum.txt`: Seoul Metro/KORAIL Line 3 - For Ogeum
    * `gyeonguijungang_munsan.txt`: KORAIL Gyeongui·Jungang Line - For Munsan
    * `gyeonguijungang_seoul_yongmun.txt`: KORAIL Gyeongui·Jungang Line - For Yongmun or Seoul station
* olympic_park: Seoul Metropolitan Subway - Olympic Park station
  * weekday, weekend_holiday (Saturday, Sunday and Holiday)
    * `5_banghwa.txt`: Seoul Metro Line 5 - For Banghwa
    * `5_macheon.txt`: Seoul Metro Line 5 - For Macheon
    * `9a_gaehwa.txt`: Seoul Metro Line 9 - For Gaehwa (All stop train)
    * `9e_gimpo_intl_airport.txt`: Seoul Metro Line 9 - For Gimpo International Airport (Express train)
    * `9a_vhs_medical_center.txt`: Seoul Metro Line 9 - For VHS Medical Center (All stop train)
    * `9e_vhs_medical_center.txt`: Seoul Metro Line 9 - For VHS Medical Center (Express train)
* sosa: Seoul Metropolitan Subway - Sosa station
  * weekday, weekend_holiday (Saturday, Sunday and Holiday)
    * `1_soyosan.txt`: Seoul Metro/KORAIL Line 1 - For Soyosan
    * `1_incheon.txt`: Seoul Metro/KORAIL Line 1 - For Incheon
    * `seohae_sosa.txt`: Seohae Line - Sosa arrival
    * `seohae_wonsi.txt`: Seohae Line - For Wonsi

# 환승 시간표 1.0.2

이 프로그램은 두 역의 시간표를 비교하여 환승 시간표를 도출하는 프로그램입니다.

## 실행 방법

이 프로그램은 Python 3.x 으로 작성되어 있으므로, Anaconda 혹은 Python 설치가 필요합니다. (Virtual environment 권장)

```shell
$ pip install -r requirements.txt
$ python transfer_timetable.py path/to/timetable1.txt path/to/timetable2.txt transfer_walk_minute
```

실행하면, 시간표가 `timetable1.txt`인 역에서 시간표가 `timetable2.txt`인 역으로 `transfer_walk_minute` 분 만에 환승했을 때의 실행 결과가 도출됩니다. 원하면 파일 저장도 가능합니다.

예를 들어, 다음 명령어를 실행하면:

```shell
$ python transfer_timetable.py sinnae/weekday/6_sinnae.txt sinnae/weekday/gyeongchun_chuncheon.txt 2.5
```

6호선 신내역에 도착한 후 경춘선 춘천 방면으로 2.5분 만에 환승했을 때의 환승 시간표가 도출됩니다.

## 시간표 파일 내부 구조

시간표 파일 구조는 텍스트 파일이며, 다음과 같이 작성하시면 됩니다.

```
[역명] [노선명] [평일/토요일/일요일/공휴일] [열차의 방향]
[행선지] [도착 시간]
[행선지] [도착 시간]
[행선지] [도착 시간]
[행선지] [도착 시간]
...
[행선지] [도착 시간]
```

1. 첫 번째 줄은 역명, 노선명, 일주일 종류, 방향을 입력하시면 됩니다.

   + 역명: 역 이름 (예: 서울역, 강남역, ...)
   + 노선명: 노선 이름 (예: 1호선, 분당선, ...)
   + 평일, 토요일, 일요일, 공휴일 중 일요일/공휴일은 하나로 묶어서 입력하는 것이 좋습니다.
   + 열차의 방향: 상행/하행 중 선택
     + 애매할 경우 방화행 등 대표 행선지를 입력해주셔도 됩니다.

2. 두 번째 줄부터 끝까지는 행선지와 도착 시간을 입력하시면 됩니다.

이 프로그램은 파일 내용을 띄어쓰기로 구분해서 인식하기 때문에, 띄어쓰기가 있을 경우 언더바(_)로 입력해주세요.

시간표 파일 예시를 확인하고 싶다면 아래에 나와 있는 샘플 파일들을 참고해주시기 바랍니다.

## 시간표 파일 샘플

시간표 디렉토리 구조는 다음과 같습니다:

* sinnae: 신내역
  * weekday: 평일, saturday: 토요일, sunday_holiday: 일요일/공휴일
    * `6_eungam_loop.txt`: 6호선 응암순환 방면
    * `6_sinnae.txt`: 6호선 신내 도착
    * `gyeongchun_cheongnyangni.txt`: 경춘선 상봉/청량리 방면
    * `gyeongchun_chuncheon.txt`: 경춘선 춘천 방면
* imae: 이매역
  * weekday: 평일, weekend_holiday: 주말(토/일)/공휴일
    * `suinbundang_wangsimni.txt`: 수인·분당선 왕십리 방면
    * `suinbundang_incheon.txt`: 수인·분당선 인천 방면
    * `gyeonggang_pangyo.txt`: 경강선 판교 방면
    * `gyeonggang_yeoju.txt`: 경강선 여주 방면
* choji: 초지역
  * weekday: 평일, weekend_holiday: 주말(토/일)/공휴일
    * `4_danggogae.txt`: 4호선 당고개 방면
    * `4_oido.txt`: 4호선 오이도 방면
    * `seohae_sosa.txt`: 서해선 소사 방면
    * `seohae_wonsi.txt`: 서해선 원시 방면
    * `suinbundang_wangsimni.txt`: 수인·분당선 왕십리 방면
    * `suinbundang_incheon.txt`: 수인·분당선 인천 방면
* daegok: 대곡역
  * weekday: 평일, weekend_holiday: 주말(토/일)/공휴일
    * `3_daehwa.txt`: 3호선 대화 방면
    * `3_ogeum.txt`: 3호선 오금 방면
    * `gyeonguijungang_munsan.txt`: 경의중앙선 문산 방면
    * `gyeonguijungang_seoul_yongmun.txt`: 경의중앙선 용문/서울역 방면
* olympic_park: 올림픽공원역
  * weekday: 평일, weekend_holiday: 주말(토/일)/공휴일
    * `5_banghwa.txt`: 5호선 방화 방면
    * `5_macheon.txt`: 5호선 마천 방면
    * `9a_gaehwa.txt`: 9호선 개화 방면 (일반열차)
    * `9e_gimpo_intl_airport.txt`: 9호선 김포공항 방면 (급행열차)
    * `9a_vhs_medical_center.txt`: 9호선 중앙보훈병원 방면 (일반열차)
    * `9e_vhs_medical_center.txt`: 9호선 중앙보훈병원 방면 (급행열차)
* sosa: 소사역
  * weekday: 평일, weekend_holiday: 주말(토/일)/공휴일
    * `1_soyosan.txt`: 1호선 소요산 방면
    * `1_incheon.txt`: 1호선 인천 방면
    * `seohae_sosa.txt`: 서해선 소사 도착
    * `seohae_wonsi.txt`: 서해선 원시 방면

## 수정 내역 (Revision history)

* Version 0.2: required custom transfer-walk-minutes.
* Version 0.3: modified timetables to deal with their own information, and destination, and more 2 sample files.
* Version 0.4: added a feature that can save result as a file.
* Version 0.4.1: changed from [] to <> in 'Usage: ...', weekend timetable files added.
* Version 0.5: changed timetable directory structure, add Imae station sample, add color to timetable.
* Version 0.5.1: added more sample timetable files (Choji station).
* Version 0.6: separated `README.md` into 2 sections in different languages, and changed result file type (TXT -> HTML).
* Version 0.7: applied bootstrap 4.4 to the result file.
* Version 0.7.1: added requirements.txt, and replaced UNIX coloring to colorama package (for OS compatibility)
* Version 0.7.2: patched vulnerability of input(), and added .idea (PyCharm) project settings
* Version 0.7.3: specified encoding='UTF8'
* Version 0.8: applied a code that filters destination's terminal train
* Version 1.0: applied \<div class = row, col\> tags, upgraded bootstrap 4.4.1 to 4.5.3
* Version 1.0.1: integrated saturday + sunday_holiday to weekend_holiday (except Sinnae station), and applied big timetable update due to COVID-19 pandemic
* Version 1.0.2: added banner in README and Sosa station timetable sample
* Version 1.0.3: separated all stop and express train in Line 9

