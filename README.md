# dl-sndexportscript

### 关于仓库

此脚本用于通过vgmstream导出同时有acb和awb的音频文件



### 代码逻辑与实现

vgmstream导出音频文件命令如下：

`test.exe -s 1-o 1.wav 1.awb`

此脚本中，需要读取如下文件的内容：

`soundfile_seq.csv`



### awb与acb文件区分判断

如果音频文件同时存在awb和acb文件，音频及音频流信息往往在awb文件中，若只存在acb文件，则音频及音频流信息皆在acb文件中



### 脚本用法

```python
usage: python dse.py [-fileid] <file_id> [-seqfile] <seqfile> ([-channel] <channel_id> [-ow <int>])

Python Program for Extract Sound Files

optional arguments:
  -h, --help          show this help message and exit
  -fileid [FILEID]    extract file from filelist sequence
  -seqfile [SEQFILE]  specify a file instead of default sequence
  -channel [CHANNEL]  extract channel N from file channels,set 0 or empty extract all single channel
  -ow [OW]            <unavailable> selected set 1 allow export file overwrite, default or set 0 refuse overwrite.
```

`-fileid` :要解压出来序列文件中的id

`-seqfile`:指定一个存储的序列文件(默认为soundfile_seq.csv)

`-channel`:指定一个音频文件的channel所属id来导出，设为0或不填默认导出所有channel的音频

`-ow`:**<暂不可用>**是否覆盖读写
