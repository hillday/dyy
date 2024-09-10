# dyy
把遥远的救世主中的关于丁元英的对话提取出来，用来做模型微调。

## 提取
```shell
python ddy.py
```
提取出来会保存到一个数组中，但是有可能会有不正确的数据，需要过滤。执行
```shell
python filter_dyy.py
```
最后得到的dyy_final.json就可以拿来微调