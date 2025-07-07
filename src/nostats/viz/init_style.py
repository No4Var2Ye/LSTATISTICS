# -*- coding: utf-8 -*-
# =====================================================================
# --- Package: nostats.viz
# =====================================================================

import os
import sys
from pathlib import Path

import numpy as np

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = CURRENT_DIR.parent.parent
# print(f"{PROJECT_DIR}")
sys.path.insert(0, str(PROJECT_DIR))
# print(sys.path)

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from nostats.viz import VizSettings as Settings

# =====================================================================

FONT_PATH = Settings.ASSETS_PATH

# =====================================================================

# print(mpl.matplotlib_fname())

# plt.rcParams["font.sans-serif"] = ['Microsoft YaHei', "Arial"]  # 使用黑体
# font_path = fm.findfont(fm.FontProperties(family="Arial"))
font_path = str(FONT_PATH / "yahei" / "msyh.ttc")
# print(font_path)
plt.rcParams["font.family"] = ['Microsoft YaHei']
# plt.rcParams["font.family"] = fm.FontProperties(fname=font_path).get_name()
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题

# # 英文部分：Times New Roman（学术标准）
# plt.rcParams["font.family"] = "Times New Roman"  # 英文
# plt.rcParams["mathtext.fontset"] = "stix"  # 数学公式风格（类似 LaTeX）

# # 中文部分：宋体/黑体（需系统支持）
# plt.rcParams["font.sans-serif"] = ["SimSun"]  # 宋体（正文）
# # plt.rcParams["font.sans-serif"] = ["SimHei"]  # 黑体（标题）

# =====================================================================

# 设置参数
# plt.style.use('seaborn-white')
plt.figure(figsize=(12, 6))

# 模拟数据 - 收入区间(千美元)
income_bins = np.arange(0, 126, 5)  # 0-125千美元，每5千美元一个区间

# 模拟1973年和1987年的百分比数据
# 假设1987年低收入区间比例更高，高收入区间比例更低
percent_1973 = np.exp(-0.03 * income_bins[:-1]) * 5
percent_1987 = np.exp(-0.025 * income_bins[:-1]) * 6

# 调整使1987年低收入更高，高收入更低
percent_1987[:10] = percent_1973[:10] * 1.2  # 前10个区间(0-50k)增加20%
percent_1987[-5:] = percent_1973[-5:] * 0.8  # 后5个区间(100k+)减少20%

# 绘制直方图
width = 2  # 柱状图宽度
plt.bar(income_bins[:-1], percent_1973, width=width, alpha=0.7, 
        label='1973年', color='blue', edgecolor='black')
plt.bar(income_bins[:-1] + width, percent_1987, width=width, alpha=0.7,
        label='1987年', color='red', edgecolor='black', linestyle='--')

# 添加标签和标题
plt.title('1973年与1987年美国家庭收入对比', fontsize=14)
plt.xlabel('收入(千美元)', fontsize=12)
plt.ylabel('每千美元的百分率', fontsize=12)
plt.legend(fontsize=12)

# 调整坐标轴
plt.xlim(0, 125)
plt.xticks(np.arange(0, 126, 10))
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()