# 文档
相应的文档请查看
https://moi-doc.vercel.app/


# 这是什么？

moi (Moving Object Visualization, 读作movie去掉v, 因为i比v可爱所以保留i) 是一个基于taichi的仿真工具包。我们希望打造一个用于图形学仿真算法验证与创新的轮子，让你摆脱多余的工作，直接关注于最核心的仿真算法。这可以被认为是一个实验的**底座**台子，你可以在上面安插上自己的算法。


我们选择使用taichi的原因是它非常适合仿真算法的开发：有极好的可移植性，并且已经为我们造好了许多轮子。但这还不够，我们想要的是开门见山：**直接从核心代码到可以放到论文里的渲染图。**通用性往往是易用性的大敌。我们希望API简单直接，专注于它应该干的事情，不要”多管闲事“。

# 我们需要什么？

**一切都是为了直接服务于图形学仿真科研**。


我们将moi分为两大部分：第一部分我们称之为**基础设施**Infra, 第二部分我们称之为**算法**Algo。

## 基础设施
在这个流水线上，我们需要以下轮子：

1. 针对于线性方程组求解的数学库: Math
2. 读取和保存常见网格的功能: MeshIO
3. 流体的表面重建: SurfRecon
4. 离线渲染(path tracer): Render
5. 便于Debug的日志库：Logger
...

除此之外，我们可能还想要

1. 碰撞检测和碰撞: CollisionHandling
2. 邻域搜索: NeighborSearch
3. 稀疏空间数据结构: Octree, BVH, etc..
...

## 算法
当然，光有一个底座是不行的，假如你没有往底座上放东西，那底座的意义就没有了。因此我们打算复现主流的仿真算法。现在在计划表里的有：

- SPH
- MPM
- PBD
- LBM

# 设计原则
我们的设计哲学是：**一切从最简化出发**。

简单易用是我们的第一考虑。所有API一定要清晰简单。我们不希望有太多细碎的东西，因此包装模块时不需要暴露太多接口，而且单一模块的功能要完整。**不要**为了代码的复用、代码的通用性、甚至是性能而把模块设计搞得太复杂。该复制时就复制。

我们希望：**一觉醒来，即使你把之前的东西全部忘光了，也能在五分钟内上手使用这个轮子。**

此外，为了保证能够快速做出来一个“大概凑合能用”的轮子，在前期我们可以开手脚借助现有的开源代码。去调用他们已有的API。

## 文档

文档是我们的核心。对我们来说，**只要代码中有的，必然要在文档中有，否则这些代码就是废代码**。在开发任何新功能前，先利用文档描述好你想要设计的功能，并且在你完成这个功能之后，也要及时更新文档。

我们希望保证用户想要查找什么功能的时候，立马就能找到简单清晰的文档。好的文档应该向MATLAB学习。也就是写文档的时候假想自己是老师，在耐心地给人讲解知识。文档应该描述如下几点：

1. 这个API的基本功能
2. 输入参数的具体含义
3. 返回参数的具体含义
4. 简单的例子（必须要有）
5. 你在设计这个API时的考虑（可选）
6. 与之相关的API

为了不让用户迷惑，设计任何功能的时候请务必更新其文档。使用没有文档的功能相当于盲人摸象。没人能忍受这种事情，即使是过上几个月的你自己。

## 测试
我们认为，测试驱动开发是十分必要的。如果你写了某些功能，一定要记得测试。最好留下测试的代码。就那么放着就行，只要别破坏其他的代码。测试是为了提高人们对代码的信心。后来的人也很有必要对这段代码保持信心。当然不好写的测试也不必强求。

测试程序建议直接写在相应模块的内部的test文件夹内。我们目前尚且不需要测试框架。我们想要的是每个以test_为前缀命名的py文件都可以独立运行，且尽量只依赖于所测试的模块。测试的结果要么输出数值，要么输出可视化窗口，亦或是可以查看的OBJ等格式。总之我们希望做到：**只要用户运行某个测试文件，立马就能看到一个结果，并能够与正确结果进行对比**。

我们期望所有的测试都可以作为教学的例子。他们即是测试，又是教会了用户怎么使用。
