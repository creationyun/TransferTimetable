# TransferTimetable 0.3

이 프로그램은 파이썬으로 작성되었으며, 두 역의 시간표를 비교하여 환승 시간표를 도출합니다.

The program is written in Python, and it compares the timetables of two stations to derive a transit timetable.

## 실행 방법 (How to run)

```
python timetable_transfer.py [timetable1.txt] [timetable2.txt] [transfer_walk_minute]
```

시간표가 timetable1.txt인 역에서 시간표가 timetable2.txt인 역으로 transfer_walk_minute 만에 환승했을 때의 실행 결과가 도출된다.

The execution result is obtained when I transfer from the station whose timetable is timetable1.txt, to the station whose timetable is timetable2.txt within transfer_walk_minute time.

## 시간표 파일 샘플 (Sample timetable files)

```sinnae_6_eungam_loop_weekday.txt```: 서울 지하철 6호선 신내역 평일 응암순환 방면 시간표

```sinnae_6_sinnae_weekday.txt```: 서울 지하철 6호선 신내역 평일 신내 도착 시간표

```sinnae_GC_cheongnyangni_weekday.txt```: 수도권 전철 경춘선 신내역 평일 상봉/청량리 방면 시간표

```sinnae_GC_chuncheon_weekday.txt```: 수도권 전철 경춘선 신내역 평일 춘천 방면 시간표

## 수정 내역

* Version 0.2: requires custom transfer-walk-minutes.
* Version 0.3: 2 timetables require their own information, and destination. More 2 sample files added.