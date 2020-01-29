# TransferTimetable 0.4

이 프로그램은 두 역의 시간표를 비교하여 환승 시간표를 도출하는 프로그램이다.

The program compares the timetables of two stations to derive a transit timetable.

## 실행 방법 (How to run)

이 프로그램은 Python 3.x 으로 작성되어 있으므로, Python 설치가 필요하다.

This program is written in Python 3.x, so you need to install it.

```
python timetable_transfer.py [timetable1.txt] [timetable2.txt] [transfer_walk_minute]
```

실행하면, 시간표가 timetable1.txt인 역에서 시간표가 timetable2.txt인 역으로 transfer_walk_minute 만에 환승했을 때의 실행 결과가 도출된다. 파일 저장도 가능하다.

After running, the execution result is obtained when I transfer from the station whose timetable is timetable1.txt, to the station whose timetable is timetable2.txt within transfer_walk_minute time. You can also save it as a file.

## 시간표 파일 샘플 (Sample timetable files)

```sinnae_6_eungam_loop_weekday.txt```: 서울 지하철 6호선 신내역 평일 응암순환 방면 시간표

```sinnae_6_sinnae_weekday.txt```: 서울 지하철 6호선 신내역 평일 신내 도착 시간표

```sinnae_GC_cheongnyangni_weekday.txt```: 수도권 전철 경춘선 신내역 평일 상봉/청량리 방면 시간표

```sinnae_GC_chuncheon_weekday.txt```: 수도권 전철 경춘선 신내역 평일 춘천 방면 시간표

## 수정 내역

* Version 0.2: requires custom transfer-walk-minutes.
* Version 0.3: 2 timetables require their own information, and destination. More 2 sample files added.
* Version 0.4: add a feature that can save result as a file.