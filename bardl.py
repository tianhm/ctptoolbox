#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'chengzhi'

from datetime import datetime
from api import TqApi
from downloader import DataDownloader

api = TqApi("SIM")
# 下载从 2018-01-01 到 2018-06-01 的 cu1805,cu1807,IC1803 分钟线数据，所有数据按 cu1805 的时间对齐
# 例如 cu1805 夜盘交易时段, IC1803 的各项数据为 N/A
# 例如 cu1805 13:00-13:30 不交易, 因此 IC1803 在 13:00-13:30 之间的K线数据会被跳过
#

instrumentid = "KQ.i@SHFE.rb"
klinefile ='rb0000.csv'

kd = DataDownloader(api, symbol_list=[instrumentid], dur_sec=180,
                    start_dt=datetime(2009, 3, 1), end_dt=datetime.now(), csv_file_name=klinefile)
# 下载从 2018-05-01 到 2018-07-01 的 T1809 盘口Tick数据

while not kd.is_finished():
    api.wait_update()
    print("progress: kline: %.2f%%" % kd.get_progress())
