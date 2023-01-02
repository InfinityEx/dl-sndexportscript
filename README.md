# dl-sndexportscript

### 关于仓库

此脚本用于通过vgmstream导出同时有acb和awb的音频文件



### 代码逻辑与实现

vgmstream导出音频文件命令如下：

`test.exe -s 1-o 1.wav 1.awb`

此脚本中，需要读取如下文件的内容：

`soundfile_seq.csv`



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

