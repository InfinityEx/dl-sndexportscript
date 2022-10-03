# dl-sndexportscript

### 关于仓库

此脚本用于通过vgmstream导出同时有acb和awb的音频文件



### 代码逻辑与实现

vgmstream导出音频文件命令如下：

`test.exe -s 1-o 1.wav 1.awb`

此脚本中，需要读取如下两个文件的内容：

`soundfile_seq.csv`

`acbseq/voc_chr_mainstory_01_01.csv`

其中，`soundfile_seq.csv` 记录的是osf文件夹中的文件结构(只记录不重复的文件名)，并根据顺序给每个文件名固定的序列id，如下表格所示

| index  | acb_seq             |
| ------ | ------------------- |
| 1      | vo_chr_100001_call  |
| 2      | vo_chr_100001_story |
| 3      | vo_chr_100002_call  |
| ...... | ......              |

目前`soundfile_seq.csv` 中的文件只包含了localize.ja_jp.sound.v.story目录下的音频文件

acbseq目录下的`voc_chr_mainstory_01_01.csv` 记录的是对应awb文件的序列，具体格式如下表：

| id     | index                       |
| ------ | --------------------------- |
| 1      | VO_CHR_MAINSTORY_01_01_0001 |
| 2      | VO_CHR_MAINSTORY_01_01_0002 |
| 3      | VO_CHR_MAINSTORY_01_01_0003 |
| 4      | VO_CHR_MAINSTORY_01_01_0004 |
| 5      | VO_CHR_MAINSTORY_01_01_0005 |
| 6      | VO_CHR_MAINSTORY_01_01_0006 |
| 7      | VO_CHR_MAINSTORY_01_01_0007 |
| 8      | VO_CHR_MAINSTORY_01_01_0008 |
| 9      | VO_CHR_MAINSTORY_01_01_0009 |
| 10     | VO_CHR_MAINSTORY_01_01_0010 |
| ...... | ......                      |

awb文件的序列可以通过查看acb文件得到，通过16进制文本查看器在对应acb文件中搜索“CueIndex”即可找到文件中记录的有关对应awb文件的序列信息，如在`voc_chr_mainstory_01_01.acb` 文件中可以找到`voc_chr_mainstory_01_01.awb`文件的序列，`voc_chr_mainstory_01_01.acb`文件中关于序列的记录如下：

```c
CueName CueName CueIndex VO_CHR_100001_CALL_0001 VO_CHR_100001_CALL_0002 VO_CHR_100001_CALL_0003 VO_CHR_100001_CALL_0004 VO_CHR_100001_CALL_0005 VO_CHR_100001_CALL_0011 VO_CHR_100001_CALL_0012 VO_CHR_100001_CALL_0013 VO_CHR_100001_CALL_0014 VO_CHR_100001_CALL_0015 VO_CHR_100001_CALL_0016 VO_CHR_100001_CALL_0017 VO_CHR_100001_CALL_0018 VO_CHR_100001_CALL_0019 VO_CHR_100001_CALL_0020 VO_CHR_100001_CALL_0021 VO_CHR_100001_CALL_0022 VO_CHR_100001_CALL_0023 VO_CHR_100001_CALL_0024 VO_CHR_100001_CALL_0025 VO_CHR_100001_CALL_0026 VO_CHR_100001_CALL_0027 VO_CHR_100001_CALL_0028 VO_CHR_100001_CALL_0029 VO_CHR_100001_CALL_0030
```

通过excel整理以上数据即可得到前表

由此，在脚本所在目录，在地址栏输入cmd回车，输入以下命令即可将`voc_chr_mainstory_01_01.awb`文件中所有声道的音频按照序列导出：

```python
python dse.py --fileid 1184
```

如果需要导出`voc_chr_mainstory_01_01.awb`中指定声道，如第5个声道的数据，输入一下命令：

```python
python dse.py --fileid 1184 --channel 5
```



### 脚本用法

```python
usage: python dse.py [--fileid] <file_id> ([--channel] <channel_id>)

Python Program for Extract Sound Files

optional arguments:
  -h, --help           show this help message and exit
  --fileid [FILEID]    extract file from filelist sequence
  --channel [CHANNEL]  extract channel N from file channels,set 0 or empty extract all single channel
```

