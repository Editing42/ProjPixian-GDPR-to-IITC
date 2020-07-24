# ProjPixian-GDPR-to-IITC

[Read in English](README_EN.md)

将GDPR数据转化为IITC-draw-tool链接。

## 更新内容

2020/07/24

- 更新了对 UPV 操作的匹配，包含 hack, resonator deployed, resonator upgraded，同时验证操作状态为 success。

- 输出新的二合一文件（UPCV.log），用紫色标记 upc，用红色标记仅 upv 的 portal，方便区分。

- 懒得装 pyinstaller，只更新了 py 文件。

## 指南

1. 对于有VC2015的Windows用户，下载 UPCV_Generator.exe 文件，放到任何你喜欢的目录。如果想在MacOS或Linux上运行或者Windows运行报错，则请下载UPCV_Generator.py，并使用python3运行它。

2. GDPR文件之中你只需要game_log.tsv文件，将其复制粘贴到本程序的同一目录下，覆盖同名文件。

3. 运行本工具并按照窗口指令操作。

4. UPC.log 和 UPV.log 应当已经生成了。复制粘贴任意文件里面的内容到IITC-DrawTools Opt-Paste Drawn Items。

## 提示


1. 获取GDPR数据的方法：给Niantic发邮件到邮箱  [privacy@nianticlabs.com](mailto:privacy@nianticlabs.com) 陈述你有权获得由Niantic收集的你的"raw data"。 然后他们很快会回复你（并不会，咕咕咕）。
