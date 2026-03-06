# Transformer 架构可视化 (Manim)

![Cyberpunk Aesthetic](https://img.shields.io/badge/Style-Cyberpunk-00f2ff)
![Manim](https://img.shields.io/badge/Render-Manim_CE-bc13fe)
![LaTeX](https://img.shields.io/badge/LaTeX-Required-39ff14)

## 📖 简介

本项目提供了一个生产级的 Python 脚本，基于 **Manim** 引擎生成 Transformer 深度学习架构的动态可视化动画。通过“黑客矩阵”式的视觉美学，生动演绎从 RNN 瓶颈到 Transformer 核心机制的完整演进过程。

## ✨ 核心功能

*   **🎨 赛博朋克视觉风格**
    *   采用霓虹蓝 (`#00f2ff`)、荧光绿 (`#39ff14`) 与赛博紫 (`#bc13fe`) 的高对比度配色。
    *   动态呼吸的网格背景与光效，营造沉浸式科技感。

*   **🧠 全流程原理解析**
    1.  **RNN 的局限性**：可视化长距离依赖丢失问题。
    2.  **自注意力机制**：展示单词间的全局关联。
    3.  **QKV 投影**：查询、键、值矩阵的线性变换过程。
    4.  **缩放点积注意力**：数学公式的动态推导与计算流。
    5.  **多头注意力**：并行子空间的拆分与融合。
    6.  **位置编码**：正弦波与输入向量的叠加。
    7.  **Transformer Block**：残差连接与层归一化的堆叠结构。

*   **⚡ 专业公式渲染**
    *   使用 `MathTex` 类呈现高质量 LaTeX 数学公式。
    *   精确展示 Transformer 复杂的数学原理。

*   **💻 Web 交互界面**
    *   提供现代化的 React 界面，方便查看、复制代码及阅读使用指南。

## 🚀 快速开始

### 1. 环境准备

确保本地已安装 Python (3.8+)、FFmpeg 和 LaTeX 环境 (如 MiKTeX 或 TeX Live)。

安装 Manim 社区版：
```bash
pip install manim
```

### 2. 获取脚本

启动 Web 应用，点击界面上的 **"复制代码"** 按钮，将内容保存为 `transformer_flow.py`。

### 3. 渲染动画

在终端中运行以下命令生成 MP4 视频：

**预览模式 (480p, 快速渲染):**
```bash
manim -pql transformer_flow.py TransformerFlow
```

**高清模式 (1080p, 生产质量):**
```bash
manim -pqh transformer_flow.py TransformerFlow
```

## 🛠️ 技术栈

*   **前端**: React 19, Tailwind CSS v4, Framer Motion
*   **动画引擎**: Manim Community Edition (Python)
*   **图标库**: Lucide React

---

*Designed for educational visualization and technical presentations.*
