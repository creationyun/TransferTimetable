# TransferTimetable 0.5.1

이 프로그램은 두 역의 시간표를 비교하여 환승 시간표를 도출하는 프로그램입니다.

The program compares the timetables of two stations to derive a transit timetable.

## 실행 방법 (How to run)

이 프로그램은 Python 3.x 으로 작성되어 있으므로, Python 설치가 필요합니다.

This program is written in Python 3.x, so you need to install it.

```shell
$ python timetable_transfer.py path/to/timetable1.txt path/to/timetable2.txt transfer_walk_minute
```

실행하면, 시간표가 `timetable1.txt`인 역에서 시간표가 `timetable2.txt`인 역으로 `transfer_walk_minute` 분 만에 환승했을 때의 실행 결과가 도출됩니다. 원하면 파일 저장도 가능합니다.

After running, the execution result is obtained when you transfer from the station whose timetable is `timetable1.txt`, to the station whose timetable is `timetable2.txt` within `transfer_walk_minute` minutes. If you want, you can also save it as a file.

예를 들어, 다음 명령어를 실행하면:

For example, if you run the following command:

```shell
$ python timetable_transfer.py sinnae/weekday/6_sinnae.txt sinnae/weekday/gyeongchun_chuncheon.txt 2.5
```

6호선 신내역에 도착한 후 경춘선 춘천 방면으로 2.5분 만에 환승했을 때에 대한 환승 시간표가 도출됩니다.

A transfer timetable will be derived for when you arrive at Sinnae station on Line 6 and transfer on Gyeongchun Line for Chuncheon in 2.5 minutes.

## 시간표 파일 구조 (Structure of the timetable file)

시간표 파일 구조는 텍스트 파일이며, 다음과 같이 작성하시면 됩니다.

The timetable file structure is a text file and you can write as follows.

```
[역명] [노선명] [평일/토요일/일요일/공휴일] [열차의 방향]
[행선지] [도착 시간]
[행선지] [도착 시간]
[행선지] [도착 시간]
[행선지] [도착 시간]
...
[행선지] [도착 시간]
```

English:

```
[Station] [Line name] [Weekday/Saturday/Sunday/Holiday] [Train's direction]
[Bound for] [Arrive time]
[Bound for] [Arrive time]
[Bound for] [Arrive time]
[Bound for] [Arrive time]
...
[Bound for] [Arrive time]
```

1. 첫 번째 줄은 역명, 노선명, 일주일 종류, 방향을 입력하시면 됩니다.
   
   In the first line, you can enter the station name, line name, train's workweek type and direction.

   + 역명: 역 이름 (예: 서울역, 강남역, ...)
   + 노선명: 노선 이름 (예: 1호선, 2호선, 공항철도, ...)
   + 평일, 토요일, 일요일, 공휴일 중 일요일/공휴일은 하나로 묶어서 입력하는 것이 좋습니다.
   + 열차의 방향: 상행/하행 중 선택
     + 애매할 경우 방화행 등 대표 행선지를 입력해주셔도 됩니다.

   + Station: A name of subway station (e.g. Seoul_station, Gangnam_station, ...)
   + Line name: A name of subway line (e.g. Line_1, Line_2, Airport_Railroad, ...)
   + It is recommended to enter Sunday/Holiday together in Weekday, Saturday, Sunday, Holiday.
   + Direction of train: choose up or down
     + If you are unsure, you can also enter a representative (bound for) destination, such as For_Banghwa.

2. 두 번째 줄부터 끝까지는 행선지와 도착 시간을 입력하시면 됩니다.
   
   From the second line to the end, you can enter trains' destinations and arrival times.

이 프로그램은 파일을 띄어쓰기로 구분해서 인식하기 때문에, 띄어쓰기가 있을 경우 언더바(_)로 입력해주세요.

This program recognizes files as separated by spaces, so if they have spaces, enter them with underscores (_).

시간표 파일 예시를 확인하고 싶다면 아래에 나와 있는 샘플 파일들을 참고해주시기 바랍니다.

If you want to look for several example files, please refer to the sample files listed below.

## 시간표 파일 샘플 (Sample timetable files)

시간표 디렉토리 구조는 다음과 같습니다:

Timetable directory structure is as follows:

* sinnae: 신내역 (Seoul Metropolitan Subway - Sinnae station)
  * weekday: 평일, saturday: 토요일, sunday_holiday: 일요일/공휴일
    * `6_eungam_loop.txt`: 6호선 응암순환 방면 (Seoul Metro Line 6 - For Eungam Loop)
    * `6_sinnae.txt`: 6호선 신내 도착 (Seoul Metro Line 6 - Sinnae arrival)
    * `gyeongchun_cheongnyangni.txt`: 경춘선 상봉/청량리 방면 (KORAIL Gyeongchun Line - For Sangbong or Cheongnyangni)
    * `gyeongchun_chuncheon.txt`: 경춘선 춘천 방면 (KORAIL Gyeongchun Line - For Chuncheon)

* imae: 이매역 (Seoul Metropolitan Subway - Imae station)
  * weekday: 평일, saturday: 토요일, sunday_holiday: 일요일/공휴일
    * `bundang_wangsimni.txt`: 분당선 왕십리 방면 (KORAIL Bundang Line - For Wangsimni)
    * `bundang_suwon.txt`: 분당선 수원 방면 (KORAIL Bundang Line - For Suwon)
    * `gyeonggang_pangyo.txt`: 경강선 판교 방면 (KORAIL Gyeonggang Line - For Pangyo)
    * `gyeonggang_yeoju.txt`: 경강선 여주 방면 (KORAIL Gyeonggang Line - For Yeoju)

* choji: 초지역 (Seoul Metropolitan Subway - Choji station)
  * weekday: 평일, saturday: 토요일, sunday_holiday: 일요일/공휴일
    * `4_danggogae.txt`: 4호선 당고개 방면 (Seoul Metro/KORAIL Line 4 - For Danggogae)
    * `4_oido.txt`: 4호선 오이도 방면 (Seoul Metro/KORAIL Line 4 - For Oido)
    * `seohae_sosa.txt`: 서해선 소사 방면 (Seohae Line - For Sosa)
    * `seohae_wonsi.txt`: 서해선 원시 방면 (Seohae Line - For Wonsi)

## 수정 내역 (Revision history)

* Version 0.2: requires custom transfer-walk-minutes.
* Version 0.3: 2 timetables require their own information, and destination. More 2 sample files added.
* Version 0.4: add a feature that can save result as a file.
* Version 0.4.1: change from [] to <> in 'Usage: ...', weekend timetable files added.
* Version 0.5: change timetable directory structure, add Imae station sample, add color to timetable.
* Version 0.5.1: More sample timetable files (Choji station) added.