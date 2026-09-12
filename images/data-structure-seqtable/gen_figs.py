# -*- coding: utf-8 -*-
"""生成《数据结构 —— 顺序表》博客配图"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.font_manager as fm

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

OUT = 'D:/blog/my-blog01/source/images/data-structure-seqtable/'

C_BOX = '#dce9f7'
C_EMPTY = '#f7f7f7'
C_EDGE = '#2c5f8d'


def draw_cells(ax, x0, y0, cells, w=1.0, h=1.0, fs=13):
    for i, (txt, color) in enumerate(cells):
        x = x0 + i * w
        ax.add_patch(Rectangle((x, y0), w, h, facecolor=color,
                               edgecolor=C_EDGE, linewidth=1.5))
        if txt:
            ax.text(x + w / 2, y0 + h / 2, txt, ha='center', va='center',
                    fontsize=fs, color='#1a1a1a')


# ============ 图1：数组内存模型 ============
fig, ax = plt.subplots(figsize=(11, 5.6))
ax.set_xlim(-1.6, 11.4)
ax.set_ylim(-2.6, 4.2)
ax.axis('off')

ax.text(5.0, 3.75, '数组内存模型：长度 vs 有效元素个数', ha='center',
        fontsize=16, fontweight='bold', color='#1a1a1a')

vals = ['12', '23', '45', '31', '56', '82', '', '', '', '']
cells = [(v, C_BOX if v else C_EMPTY) for v in vals]
draw_cells(ax, 0, 1.0, cells, w=1.0, h=1.0, fs=14)

# 下标
for i in range(10):
    ax.text(0.5 + i, 0.62, str(i), ha='center', va='center',
            fontsize=11, color='#555')

# 左侧标注
ax.text(-0.45, 1.5, 'int arr[10]', ha='right', va='center',
        fontsize=13, family='monospace', color='#2c5f8d')

# 有效元素括号（对齐到 0~5 号格）
ax.annotate('', xy=(0, 2.45), xytext=(6, 2.45),
            arrowprops=dict(arrowstyle='-', color='#66bb6a', lw=3))
ax.text(3.0, 2.72, '有效元素 6 个（下标 0~5）', ha='center', fontsize=13,
        color='#2e7d32', fontweight='bold')

# 长度括号（下移，避开 cur 箭头）
ax.annotate('', xy=(0, -1.35), xytext=(10, -1.35),
            arrowprops=dict(arrowstyle='-', color='#c62828', lw=3))
ax.text(4.3, -1.72, '数组长度 10（容量）', ha='center', fontsize=13,
        color='#c62828', fontweight='bold')

# cur 箭头（从格子下方引出，画在长度线之上，停顿在元素尾部）
ax.annotate('', xy=(6, 0.92), xytext=(6, 0.0),
            arrowprops=dict(arrowstyle='->', color='#e65100', lw=2.5))
ax.text(6.35, 0.15, 'cur = 6', ha='left', va='center',
        fontsize=12.5, color='#e65100', fontweight='bold')
ax.text(6.35, -0.35, '既是元素个数，\n也是下一个插入位置的下标',
        ha='left', va='center', fontsize=11, color='#e65100')

# 右侧标注
ax.text(11.0, 1.5, '内存\n连续', ha='center', va='center', fontsize=12,
        color='#2c5f8d', fontweight='bold')

plt.tight_layout()
plt.savefig(OUT + 'array-memory-model.png', dpi=150, bbox_inches='tight',
            facecolor='white')
plt.close()
print('OK array-memory-model.png')
