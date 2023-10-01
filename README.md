# Formula_CP
Copy formulas in Latex format from any website and save them in a markdown file.

### English

#### Running instructions

First clone the code repository and enter the corresponding file path:

```bash
git clone https://github.com/zhangkai0425/Formula_CP.git
cd Formula_CP
```

Before running, make sure you have the corresponding `Python` library installed:

```bash
pip install requests
pip install beautifulsoup4
```

After installation, directly execute the corresponding  `main.py`  program:

```bash
python main.py
```

For example, if you want to capture all formulas of a `Zhihu` page website (note that only formulas in `Latex` format are included, and only equations are saved, ignoring univariate and irrelevant symbols), enter the corresponding website link `URL` after execution, and the corresponding content will be automatically saved to the `formula.md` file. It is easy to copy, paste and edit.

#### Test case

```bash
(pytorch2021) zhangkaideMacBook-Air:Formula_CP zhangkai$ python main.py
Please input URL:https://zhuanlan.zhihu.com/p/553601317
28 formulas with '=' saved to formula.md
```

This website is a special relativity derivation website, contains more mathematical physics publicity content, now check `formula.md` can see the corresponding formula.

### 简体中文

#### 运行说明

首先克隆代码仓库并进入对应文件路径：

```bash
git clone https://github.com/zhangkai0425/Formula_CP.git
cd Formula_CP
```

在运行之前，请确保安装了对应的`Python`库：

```bash
pip install requests
pip install beautifulsoup4
```

安装完成后，直接执行相应的`main.py`程序：

```bash
python main.py
```

例如，如果想要抓取一个`知乎`的页面网站的全部公式(注意，只包含了`Latex`格式的公式，且仅仅保存等式，忽略单变量和无关的符号)，执行后输入相应的网站链接`URL`即可，对应内容会自动保存到`formula.md`文件当中，可以很方便地进行复制粘贴及编辑操作。

#### 运行实例

```bash
(pytorch2021) zhangkaideMacBook-Air:Formula_CP zhangkai$ python main.py
Please input URL:https://zhuanlan.zhihu.com/p/553601317
28 formulas with '=' saved to formula.md
```

此网站是一个狭义相对论推导的网站，包含了比较多的数学物理公示内容，现在检查`formula.md`可以看到对应的公式了。
