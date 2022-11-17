# opencv 学习





### 几个主要api

1. 读取图片 `imread()`

2. 保存图片 `imwrite()`

3. 命名窗口 `namedWindow()`

4. 设置窗口 `resizeWindow()`

5. 获取键盘按键 `waitKey()`

6. 销毁窗口 `destoryAllWindows()`

7. 视频捕获 `VideoCapture()`

8. 读取视频帧 `capInstance.read()`

9. 录制视频类 `VideoWriter`

10. 设置鼠标回调函数 `setMouseCallback(windowName, onMouse, param=None)`

11. 鼠标回调函数 `onMouse(event, x, y, flags, userdata)`

    >event 与 flags 的定义
    >
    ><img src="https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221028112013207.png" alt="image-20221028112013207"/>
    >
    >![image-20221028112049558](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221028112049558.png)

12. 创建 TrackBar 控件 `createTrackbar(trackbarname, winname, value, count, onChange, userdata)`

13. 获取 TrackBar 值 `getTrackbarPos(trackbarname, winname)`

14. 颜色空间转换 `cvtColor`



## 图像绘制

> * 颜色空间
> * 像素访问
> * 矩阵计算
> * 基本图像的绘制

### 颜色空间

>* RGB: 人眼的色彩空间
>
>opencv默认使用 `BGR`
>
>* HSV/HSB/HSL
>* YUV



#### HSV/HSB

* `Hue`: 色相，即色彩，如红色，蓝色
* `Saturation`: 饱和度，颜色的纯度
* `Value/Brightness`: 明度

![image-20221030111303199](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221030111303199.png)



#### HSL

* `Hue`
* `Saturation`
* `Lightness`



<img src="https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221030111746682.png" />





#### YUV

>YUV是编译true-color颜色空间（color space）的种类，Y'UV, YUV, [YCbCr](https://baike.baidu.com/item/YCbCr?fromModule=lemma_inlink)，[YPbPr](https://baike.baidu.com/item/YPbPr?fromModule=lemma_inlink)等专有名词都可以称为YUV，彼此有重叠。“Y”表示明亮度（Luminance或Luma），也就是灰阶值，“U”和“V”表示的则是色度（Chrominance或Chroma），作用是描述影像色彩及饱和度，用于指定像素的颜色。

几个主要的格式

* YUV 4:2:0
* YUV 4:2:2
* YUV 4:4:4





### Numpy知识点

* OpenCV 中用到的矩阵都要转换为 Numpy 数组
* Numpy 是一个经高度化优化的 python 数值库



#### 创建矩阵

* 创建矩阵`array()`
* 创建全0/1 的矩阵 `zeros()/ones()`
* 全值数组 `full()`
* 单元数组 `identity()/eye()`



#### 检索与赋值 `[y, x]`

* `[y,x]`  
* `[y,x, channel]`





#### 获取子数组 `[:,:]`

> ROI（Regin Of Image）

* `[y1:y2, x1:x2]` 
* `[:, :]` 所有元素
* `[:]` 所有元素



在 opencv 中对图形的操作，都可以转换为对像素点的操作



### Mat

1. Mat是什么？

   > Mat 是 opencv 中一个重要的数据类型 -- 矩阵

![image-20221031113521037](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221031113521037.png)

Mat 头部信息

![image-20221031114557862](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221031114557862.png)





#### Mat 深拷贝和浅拷贝

![image-20221031114823657](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221031114823657.png)



* 浅拷贝

  ```c++
  Mat A
  A = imread(file, IMREAD_COLOR)
  Mat B(A)
  ```

  

* 深拷贝

  ```c++
  cv::Mat::clone()
  cv::Mat::copyTo()
  ```

  在 python 中为 clone()



#### Mat属性

* `shape`
* `size`
* `dtype`



#### 通道的分离和合并

* `split(mat)`
* `merge((ch1,cha2, ...))`



### OpenCV 基本图像的绘制

#### 画线

`line(img, 开始点， 结束点, 颜色...)`

> 参数说明：
>
> Img: 在那个图像上画线
>
> 开始点、结束点：指定线的开始与结束位置
>
> 颜色、线宽、线型
>
> shift: 坐标缩放比例

```python
line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
```

#### 画矩阵

```python
rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
```

#### 画圆形

```python
circle(img, center, radius, color, thickness=None, lineType=None, shift=None)
```

#### 画椭圆

`ellipse(img, 中心点, 长宽的一半, 角度, 开始角度, 结束角度, ...)`

```python
ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness=None, lineType=None, shift=None)
```

![image-20221031144354429](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221031144354429.png)



#### 画多边形

```python
polylines(img, pts, isClosed, color, thickness=None, lineType=None, shift=None)
```

> pts 为多边形定点数组 ,**类型必须为 `np.int32`**



填充多边形

```python
fillPoly(img, pts, color, lineType=None, shift=None, offset=None)
```



#### 绘制字体

```python
putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None)
```







* 绘制api中 `thickness`为 -1 的时候，图形为填充, 多边形填充除外





#### 案例：利用鼠标回调函数和键盘事件绘制基本图形





### 车辆识别

* 基本图像运算与处理
* 形态学
* 轮廓查找







## 图像运算

### 两个图像相加

* ```python
  def add(src1, src2, dst=None, mask=None, dtype=None):
  ```



### 两个图像相减



```python
def subtract(src1, src2, dst=None, mask=None, dtype=None):
```



### 图像乘与图像除

```python
def multiply(src1, src2, dst=None, scale=None, dtype=None):
```

```py
def divide(src1, src2, dst=None, scale=None, dtype=None):
```



### 图像融合

```python
def addWeighted(src1, alpha, src2, beta, gamma, dst=None, dtype=None)
```

>* `alpha` 、`beta` 是权重
>* `gamma` 静态权重
>* ```dst = src1*alpha + src2*beta + gamma;```



### 图像位运算

#### 与

```python
def bitwise_and(src1, src2, dst=None, mask=None)
```

#### 或

```python
def bitwise_or(src1, src2, dst=None, mask=None)
```

#### 非

```python
def bitwise_not(src, dst=None, mask=None)
```

#### 异或

```python
def bitwise_xor(src1, src2, dst=None, mask=None)
```





### 案例： 为图片添加水印

> 步骤：
>
> 1. 导入一张需要添加水印的图片
> 2. 导入/创建 水印图片
> 3. 计算在什么地方添加，将添加的地方变为黑色
> 4. 利用 add 将两张图片叠加到一起



## 图像变换

### 图像的放大与缩小

`def resize(src, dsize, dst=None, fx=None, fy=None, interpolation=None):`

>* `dsize`： 目标尺寸
>
>* `fx`: 图片宽度缩放因子
>
>* `fy`：图片高度缩放因子
>
>* `interpolation`: 缩放插值算法
>
>  ```py
>  INTER_AREA = 3  # 效果最好
>  INTER_BITS = 5
>  INTER_BITS2 = 10
>  INTER_CUBIC = 2  # 三次插值，原图中的16个点
>  INTER_LANCZOS4 = 4
>  INTER_LINEAR = 1  # 双线性插值，原图中的4个点
>  
>  INTER_LINEAR_EXACT = 5
>  
>  INTER_MAX = 7
>  INTER_NEAREST = 0   # 邻近插值，速度快，效果差(默认)
>  
>  INTER_NEAREST_EXACT = 6
>  
>  INTER_TAB_SIZE = 32
>  INTER_TAB_SIZE2 = 1024
>  ```
>
>  



### 图像的翻转

`def flip(src, flipCode, dst=None)`

>* `flipCode`:
>  * `0`： 表示沿 x 进行翻转 (上下)
>  * `正数`: 表示沿 y 轴进行翻转 （左右）
>  * `负数`: 表示沿 两个轴进行翻转 （上下和左右）

### 图像的旋转

`def rotate(src, rotateCode, dst=None)`

>* `rotateCode`:
>  * `ROTATE_90_CLOCKWISE` : 顺时针 90 度
>  * `ROTATE_180`： 180度
>  * `ROTATE_90_COUNTERCLOCKWISE`： 逆时针 90度（顺时针 270）





### 图片的仿射变换

> 什么是仿射变换？
>
> 仿射变换是图像选择、缩放、平移的总和

仿射变换API

`def warpAffine(src, M, dsize, dst=None, flags=None, borderMode=None, borderValue=None)`

> * `M`： 变换矩阵
> * `dsize`: 输出尺寸
> * `flags`: 插值算法
> * `dorderMode`： 边界外推法标志
> * `vorderVAlue`: 填充边界的值





### 仿射变换之图像平移

* 矩阵中每个像素由 (x, y) 组成
* 变换矩阵是一个 2 x 2 的矩阵
* 平移向量为 2 x 1 的向量, 所以在平移矩阵为 2 x 3 的矩阵



### 仿射变换之获取变换矩阵

OpenCV 提供的获取变换矩阵的API:

`def getRotationMatrix2D(center, angle, scale):`

> * `center`： 旋转中心点, `(x, y)`
> * `angle`:  旋转角度(逆时针)
> * `scale`:  缩放比例







### 仿射变换之变换矩阵2

`def getAffineTransform(src, dst)`

>* `src`: 原图中三角形的顶点坐标
>* `dst`: 与原图对应三角形订单坐标





### OpenCV 透视变换

切换坐标系，将一种坐标系（通常为不好进行后续处理的）切换为另一种坐标系（方便处理）

`def warpPerspective(src, M, dsize, dst=None, flags=None, borderMode=None, borderValue=None)`

> * `src`
> * `M`: 变换矩阵(3x3)
> * `dsize`: 目标图像大小
> * `dst`
> * `flags`： 插值算法
> * `dorderMode`： 边界外推法标志
> * `borderValue`： 填充边界的值





#### 获取透视变换矩阵

`def getPerspectiveTransform(src, dst, solveMethod=None)`

>* `src`： 圆图像上的四个点(需要变换位置的四个定位点)
>* `dst`: 目标图像的四个点
>* `solveMethod`: 



案例： 文档扫描修正、作业检测处理的准备工作....





## 图像滤波

### 滤波的作用？

> 一幅图像[经过滤波器]()得到[另一幅图像]();
>
> 其中滤波器又称为[卷积核](),滤波的过程称为[卷积]()



###  卷积的几个基本概念

* 卷积核的大小
* 锚点
* 边界扩充
* 步长



#### 卷积核的大小

卷积核一般是奇数，如 3x3 、5x5 、7x7 等

一方面是增加 `padding`的原因

另一方面是保证**锚点**在中间，防止位置发生偏移



#### 卷积核大小的影响

在深度学习中，卷积核越大，看到的信息（[感受野]()）越多，提取的[特征越好]()，同时计算量越大





#### 锚点

卷积核的正中心点



#### 边界扩充

* 当卷积核大于1且不进行边界扩充，输出尺寸将相应缩小

* 当卷积核以标准方式进行边界扩充，则输出数据的空间尺寸将与输入相等

  ![image-20221107180146251](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221107180146251.png)



#### 计算公式

* `N = (W - F + 2P)/S + 1`

  >* `N`: 输出图像的大小
  >* `W`： 原图大小
  >* `F`： 卷积核的大小
  >* `P`： 扩充的尺寸
  >* `S`： 步长大小



#### 步长

![image-20221107180700771](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221107180700771.png)



### 实战图像卷积



#### 低通滤波、高通滤波

> 低通滤波可以去除噪音或者平滑图像
>
> 高通滤波可以帮助查找图像的边缘



#### 图像卷积API

`def filter2D(src, ddepth, kernel, dst=None, anchor=None, delta=None, borderType=None)`

> * `src`
> * `ddepth`： 期望图片的位深, 图片深度
> * `kernel`： 卷积核
> * `anchor`：锚点， 默认值（-1, -1）表示全集合锚点
> * `delta`： 对每次计算的值加上一个固定值 
> * `borderType`： 边界类型（像素外推法）





### 方盒滤波与均值滤波



#### 方盒滤波卷积核

$$
K = a
\left[
\begin{matrix}
1 & 1 & 1 & ... & 1\\
1 & 1 & 1 & ... & 1 \\
... & ... & ... & ... & ... \\
1 & 1 & 1 & ... & 1 \\
\end{matrix}
\right]
$$



参数 a 的作用

* `normalize = true, a = 1 / W x H`
* `normalize = false, a = 1`



当 `normalize == true`时 , [方盒滤波 == 平均滤波]()



#### 两个滤波API

* 方盒滤波

  `def boxFilter(src, ddepth, ksize, dst=None, anchor=None, normalize=None, borderType=None)`

  >* `ksize` ： 卷积核大小
  >* `normalize`: 是否均值化

* 均值滤波

  `def blur(src, ksize, dst=None, anchor=None, borderType=None)`





### 高斯滤波

![image-20221108140735058](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221108140735058.png)

![image-20221108140813433](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221108140813433.png)

![image-20221108140853064](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221108140853064.png)

#### 高斯滤波API

`def GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None)`

> * `ksize`： 卷积核大小， 可以不是方盒，但是必须正奇数
> * `sigmaX`：X方向的高斯核标准差
> * `sigmaY`： Y 方向的高斯核标准差，如果为 0 ,则和 `sigmaY`相等, 如果两个都为0 ，则根据 `ksize`的宽高来计算





### 中值滤波

#### 什么是中值滤波？

>假设有一个数组`[1556789]`取其中的[中间值]() 作为卷积后的结果值



#### 中值滤波的优点

对[胡椒噪音]()效果明显



![image-20221108145637569](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221108145637569.png)

#### 中值滤波API

`def medianBlur(src, ksize, dst=None)`

>* `ksize`: 孔径线性尺寸;它必须是奇数且大于1，例如:3,5,7…





### 双边滤波

### 什么是双边滤波？

> 双边滤波（Bilateral filter）是一种非线性的滤波方法，是结合图像的空间邻近度和像素值相似度的一种折中处理，同时考虑空域信息和灰度相似性，达到保边去噪的目的

### 双边滤波的优点

1. 可以保留图像边缘
2. 对边缘内的区域进行平滑处理

对于双边滤波的作用是[进行美颜]()



#### 原理

![](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/v2-56856d2c7f8f48337bb5f07f4580d55d_1440w.jpeg)



### API

`def bilateralFilter(src, d, sigmaColor, sigmaSpace, dst=None, borderType=None)`

>* `d`: 使用滤波的像素直径(diameter)
>* `sigmaColor`：值域sigma 
>* `sigmaSpace`：空域sigma







## 高通滤波

作用： 检测边缘



### 常见的高通滤波

* `Sobel`（索贝尔）(高斯)
* `Scharr`（沙尔）
* `Laplacian`（拉普拉斯）



### Sobel 算子

* 先向 x 方向求导
* 再在 y 方向上求导
* 最终结果 : `|G| = |Gx| + |Gy|`

#### API

`def Sobel(src, ddepth, dx, dy, dst=None, ksize=None, scale=None, delta=None, borderType=None)`

>* `ddepth` : 输出图像的深度
>* `dx`: x 方向导数的阶
>* `dy`:  y 方向导数的阶
>* `ksize`： Sobel核的大小， 当值为 `-1`的时候，该API等同于沙尔算子



### Scharr 算子

* 与 Sobel 类似，只不过使用的 kernel 值不同
* Scharr 只能求 x 方向或者 y 方向的边缘



#### API

`def Scharr(src, ddepth, dx, dy, dst=None, scale=None, delta=None, borderType=None)`

>同 Sobel 算子
>
>* `dx`与`dy`满足如下条件：
>  1. 都为整数
>  2. 相加为1



### Laplacian 算子

* 可以同时求两个方向的边缘
* 对噪音敏感, 一般需要先进行去噪再使用拉普拉斯算子计算边缘



#### API

`def Laplacian(src, ddepth, dst=None, ksize=None, scale=None, delta=None, borderType=None)`

>* `ksize`: 算子核大小，满足条件（在[1,31]范围内的奇数）





### 边缘检测 Canny

* 使用 `5 x 5` 的高斯滤波消除噪声
* 计算图像梯度的方向( 0/45/90/135 )
* 取局部最大值
* 阀值计算



![image-20221108163527758](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221108163527758.png)



#### API

`def Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None)`

>* `image`: 8位图像
>* `threshold1` ： 最小的阈值
>* `threshod2`： 最大的阈值
>* `edges`
>* `apertureSize`： Sobel 算子的孔径大小
>* `L2gradient`： 是否





## 形态学图像处理



### 什么是形态学处理？

* 基于图像形态进行处理的一些基本方法
* 这些处理方法基本是对二进制图像进行处理
* 卷积核决定着图像处理后的效果



### 形态学图像处理

* 腐蚀与膨胀
* 开运算
* 闭运算
* 顶帽
* 黑帽



### 图像二值化

#### 什么是二值化？

> * 将图像中的每个像素变成两种值，如 0, 255 
> * 全局二值化
> * 局部二值化



#### 全局二值化API

`def threshold(src, thresh, maxval, type, dst=None) -> retval, dst`

>* `src`: 图像，最好是灰度
>
>* `thresh`: 阈值
>
>* `maxval`： 超过阈值，替换为 maxval
>
>* `type`： 阈值操作类型
>
>  * `THRESH_BINARY`  和`THRESH_BINARY_INV` 
>  * `THRESH_TRUNC`
>  * `THRESH_TOZERO` 和 `THRESH_TOZERO_INV`
>
>  ![image-20221108180332414](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221108180332414.png)



#### 自适应阈值

由于[光照不均匀]()以及阴影的存在，只有一个阈值回使得在阴影除的白色被[二值化成黑色]()

例如采用全局二值化对有阴影的图片进行处理，结果如下：

![image-20221109111615320](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221109111615320.png)

`def adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C, dst=None)`

>* `src`
>
>* `maxValue`
>* `adaptiveMethod`： 计算阈值的方法
>  * `ADAPTIVE_THRESH_MEAN_C `: 计算邻近区域的平均值
>  * `ADAPTIVE_THRESH_GAUSSIAN_C `： 高斯窗口加权平均值
>* `thresholdType`
>  * [THRESH_BINARY](https://docs.opencv.org/4.6.0/d7/d1b/group__imgproc__misc.html#ggaa9e58d2860d4afa658ef70a9b1115576a147222a96556ebc1d948b372bcd7ac59) 
>  * [THRESH_BINARY_INV](https://docs.opencv.org/4.6.0/d7/d1b/group__imgproc__misc.html#ggaa9e58d2860d4afa658ef70a9b1115576a19120b1a11d8067576cc24f4d2f03754)
>* `blockSize`： 邻近区域的大小 （大于1的奇数）
>* `C`： 常量， 应从计算出的平均值或加权平均值中减去



### 腐蚀（Erode）

![image-20221109113807518](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221109113807518.png)



> 腐蚀的原理： 利用(通常是一个一个全为1的)卷积核对图像进行卷积操作，只有当所有像素都为1的情况下，卷积后的结果才为1 

![image-20221109114130120](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221109114130120.png)

![image-20221109114156082](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221109114156082.png)



#### API

`def erode(src, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None)`

>* `src`
>* `kernel`: 腐蚀卷积核, 通常为全1 矩阵
>* `anchor`
>* `iterations`: 迭代次数
>* `borderType`:
>* `borderValue`:



### 获取形态学卷积核

#### 卷积核的类型API

`def getStructuringElement(shape, ksize, anchor=None)`

>* `shape`:  结构元素的形状
>  * `MORPH_RECT `： 矩形
>  * `MORPH_CROSS`：十字
>  * `MORPH_ELLIPSE`：椭圆结构
>* `ksize`:  卷积核大小
>* `anchor`: 默认值 (-1，-1)



### 膨胀（Dilate）

![image-20221109142720745](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221109142720745.png)

>利用卷积核(中心为1)对图像进行卷积操作， 部分为1 ，卷积结果为1



![image-20221109142920742](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221109142920742.png)



#### API

`def dilate(src, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None)`



### 问题？

#### 如果是白底黑字，进行腐蚀与膨胀后会怎样？

> 效果与黑底白字效果正好相反, 腐蚀变膨胀， 膨胀变腐蚀



#### 卷积核是否可以设置为全0?

>不能，没有膨胀效果





### 开运算

> 先腐蚀再膨胀



开运算效果：移除噪点

![image-20221109151604271](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221109151604271.png)

#### API

`def morphologyEx(src, op, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None)`

> * `op`:  形态学运算的类型
>   * `MORPH_ERODE`： 腐蚀
>   * `MORPH_DILATE`: 膨胀
>   * `MORPH_OPEN`: 开运算
>   * `MORPH_CLOSE`： 闭运算
>   * `MORPH_GRADIENT`: 形态梯度
>   * `MORPH_TOPHAT`: 顶帽
>   * `MORPH_BLACKHAT`: 黑帽
>   * `MORPH_THIMISS`



### 闭运算

> 先膨胀再腐蚀



效果

>![image-20221109153026494](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221109153026494.png)





### 形态学梯度

> 梯度 = 原图 - 腐蚀



>作用： 求边缘
>
>![image-20221109160004685](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221109160004685.png)



### 顶帽运算

> 顶帽 = 原图 - 开运算

>效果： 留下噪点
>
>![image-20221109160700314](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221109160700314.png)





### 黑帽运算

> 黑帽 = 原图 - 闭运算



> 作用： 保留闭运算中的噪点
>
> ![image-20221109171348752](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221109171348752.png)





### 小结

> 开运算： 先腐蚀再膨胀，去除大图形外的小图形
>
> 闭运算： 先膨胀再腐蚀，去除大图形内的小图形
>
> 梯度： 求图形的边缘
>
> 顶帽： 原图减开运算，得到大图形外的小图形
>
> 黑帽： 原图减闭运算，得到大图形内的小图形





## 图像轮廓

### 什么是图形轮廓？

> 具有相同[颜色]()或[强度]()的[连续点]()的曲线



### 图像轮廓的作用

* 可以用于图形分析
* 物体的识别和检测



### 注意点

* 为了检测的准确性，需要先对图像进行二值化或 Canny 操作
* 画轮廓时会修改输入的图像



### 轮廓查找API

`def findContours(image, mode, method, contours=None, hierarchy=None, offset=None)-> contours, hierarchy`

>* `image`:  8bit 单通道二值图
>
>* `mode`: 轮廓检索模式   
>
>  * `RETR_EXTERNAL =0 `:  检索外部轮廓
>
>    ![image-20221110094107918](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221110094107918.png)
>
>  * `RETR_LIST =1`: 检索所有轮廓，而不建立任何层次关系
>
>    ![image-20221110094142060](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221110094142060.png)
>
>  * `RETR_CCOMP =2`: 检索所有轮廓并将它们组织到一个两级层次结构中,每层最多两级
>
>    ![image-20221110094249437](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221110094249437.png)
>
>  * `RETR_TREE=3`: 检索所有轮廓并重构嵌套轮廓的完整层次结构（树形结构存储）
>
>    ![image-20221110094411541](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221110094411541.png)
>
>  * `RETR_FLOODFILL `
>
>* `method`: 轮廓逼近算法
>
>  * `CHAIN_APPROX_NONE `: 保存所有轮廓上的点
>  * `CHAIN_APPROX_SIMPLE `： 只保存角点
>  * `CHAIN_APPROX_TC89_L1 `： 
>  * `CHAIN_APPROX_TC89_KCOS `
>
>* `contours`:
>
>* `hierarchy`:
>
>* `offset`: 可选偏移量
>
>
>
>返回值：
>
>* `contours` 查找到的轮廓列表
>* `hierarchy`： 查找到的轮廓之间的层级关系



### 如何绘制轮廓

`def drawContours(image, contours, contourIdx, color, thickness=None, lineType=None, hierarchy=None, maxLevel=None, offset=None)->image`

>* `images`：目标图形
>* `contours`: 目标轮廓列表
>* `contoutIdx`: 绘制的轮廓索引顺序， 负数（通常设置为 -1 ）表示绘制所有轮廓
>* `color`: 绘制颜色
>* `thickness`： 线宽， -1 表示全部填充





### 轮廓的面积和周长

#### 面积

`def contourArea(contour, oriented=None)`

>`contour`: 查找轮廓列表中的某一个轮廓



#### 周长

`arcLength(curve, closed)`

> * `curve`: 轮廓或者曲线
> * `closed`: 曲线是否闭合





### 多边形逼近与凸包

> ![image-20221110103956759](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221110103956759.png)



#### 多边形逼近

`def approxPolyDP(curve, epsilon, closed, approxCurve=None)->approxCurve`

>* `curve`: 曲线
>* `epsilon`:  参数精度
>* `closed`: 曲线是否闭合



#### 凸包

`def convexHull(points, hull=None, clockwise=None, returnPoints=None) -> hull`

> * `points`： 轮廓
> * `hull`: 输出的凸包
> * `clockwise`: 顺时针绘制



### 外接矩形

> * 最小外接矩形
>
> * 最大外接矩形
>
> ![image-20221110140234604](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221110140234604.png)





#### 最小外接矩阵

`def minAreaRect(points)`

> `points`: 轮廓
>
> 返回值类型： `RotatedRect` 包含属性： `x`，`y` `width` ，`height`, `angle`



#### 最大外接矩阵

`def boundingRect(array)`

>* `array`： 轮廓
>* 返回值类型： `Rect`





## 项目1： 车辆检测

### 主要流程

1. 窗口的展示
2. 图像/视频的加载
3. 基本图形的绘制
4. 车辆识别



### 涉及知识点

* 加载视频
* 通过形态学识别车辆
* 对车辆进行统计
* 显示车辆统计信息





### 实战

1. 读视频

2. 去背景

   >大致原理：视频中像素不频繁变化的点视为背景
   >
   >* 创建背景API: `cv.bgsegm.createBackgroundSubtractorMOG([, history[, nmixtures[, backgroundRatio[, noiseSigma]]]]) ->retval`
   >
   >  >* `hsitory`:  历史长度， history = 200, 如果视频为 25fps , 200表示 200/1000 x 25 = 5帧 
   >
   >  相关论文： 《An improved adaptive background mixture model form real-time tracking with shadow detection》





## 特征检测

### 基本知识

#### 特征的场景

1. 图像搜索，如以图搜图
2. 拼图游戏
3. 图像拼接，将两张有关联的图拼接到一起
4. ...



#### 类比：拼图方法

* 寻找特征
* 特征是唯一的
* 可追踪的
* 能比较的



总结：

1. 平坦部分很难找到它在原图中的位置
2. 边缘相对较平坦要好找一些，但也不能一下确定
3. 角点可以一下就能找到其在原图中的位置





#### 什么是特征？

> 图像特征就是指有**意义的图像区域**，具有独特性、易于识别性，比如角点、斑点以及高密度区



#### 角点

* 在特征中最重要的是角点
* 灰度梯度的最大值对应的像素
* 两条线的交点
* 极值点（一阶导数最大值，二阶导数为0）





### `Harris`角点检测

> ![image-20221114144129443](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221114144129443.png)
>
> ![image-20221114144554781](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221114144554781.png)



#### Harris 角点检测API

`def cornerHarris(src, blockSize, ksize, k, dst=None, borderType=None)`

> * `blockSize`: 检测窗口大小
> * `ksize`:  **Sobel**卷积核
> * `k`： 权重系数,经验值，一般取值 0.02 ~ 0.04 之间

![image-20221114150433850](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221114150433850.png)



### `Shi-Tomasi`角点

>`Shi-Tomasi` 是 `Harris`角点检测的改进
>
>`Harris`角点检测算的稳定性和 `k` 有关，而 `k`是个经验值，不好设定最佳值



#### API

`def goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance, corners=None, mask=None, blockSize=None, useHarrisDetector=None, k=None):`

> * `maxCorners`角点的最大数量，<=0 表示无限制（返回检测结果）
> * `qualityLevel`: 角点质量， 小于 1.0 的正数， 一般在 0.01 - 0.1 之间
> * `minDistance` 角点之间的最小欧式距离
> * `userHarrisDetector`： 是否使用 `harris`角点检测，默认 False
> * `mask`： 感兴趣的区域



### `SIFT`

>`Scale-Invariant Feature Transform` 与缩放无关的特征转换



#### 出现原因

* `Harris`角点具有旋转不变的特性

* 但缩放后，原来的角点有可能就不是角点了

  >![image-20221114153811454](https://gitee.com/ChenKuan1110/typora_pic/raw/pic/2022/image-20221114153811454.png)



#### 使用 SIFT 的步骤

1. 创建 SIFT 对象
2. 进行检测， kp = sift.detect(img,...)
3. 绘制关键点, drawKeypoints(gray, kp, img)





### 计算 SIFT 描述子



#### 关键点和描述子（`KeyPoints` vs. `descriptors`）

* 关键点： 位置、大小和方向
* 关键点描述子： 记录了关键点周围对其有贡献的像素点的一组向量值，其不受仿射变换、光照变换等影响
* 描述子作用是进行特征匹配



#### 计算描述子API

`kp, des = sift.compute(img, kp)`



同时计算关键点和描述子

`kp,des = sift.detectAndCompute(img, mask)`

> `mask` ：指定感兴趣的区域



### `SURF`

> `Speeded-Up Robust Features`， 加速鲁棒性特征检测
>
> 优点：
>
> `SIFT`最大的问题在于速度慢，因此才有了 `SURF`



#### 使用步骤

1. 创建 `SURF对象`

   `surf = cv2.xfeatures2d.SURF_create()`

2. 检测计算特征点和描述子

   `kp,des = surf.detectAndCopute(img, mask)`





---



p93