# -*- coding: utf-8 -*-
"""生成插入/删除移动过程图"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

OUT = 'D:/blog/my-blog01/source/images/data-structure-seqtable/'

C_BOX = '#dce9f7'
C_EMPTY = '#f7f7f7'
C_EDGE = '#2c5f8d'
C_HL = '#ffd6a5'
C_NEW = '#a8d5a2'


def row(ax, y, vals, hl=None, new=None, w=1.0, h=0.85, fs=13, label=None):
    """画一行格子；hl=高亮下标集合，new=新插入值"""
    hl = hl or []
    for i, v in enumerate(vals):
        x = i * w
        if new is not None and i == new[0]:
            color, txt = C_NEW, new[1]
        elif i in hl:
            color, txt = C_HL, v
        else:
            color, txt = (C_BOX if v != '' else C_EMPTY), v
        ax.add_patch(Rectangle((x, y), w, h, facecolor=color,
                               edgecolor=C_EDGE, linewidth=1.4))
        if txt != '':
            ax.text(x + w / 2, y + h / 2, txt, ha='center', va='center',
                    fontsize=fs, color='#1a1a1a')
    if label:
        ax.text(-0.3, y + h / 2, label, ha='right', va='center',
                fontsize=11.5, color='#555')


subs = ['', '', '', '', '', '']

# ============ 图2：插入元素的过程 ============
fig, ax = plt.subplots(figsize=(10, 6.4))
ax.set_xlim(-2.2, 8.6)
ax.set_ylim(-0.9, 7.2)
ax.axis('off')

ax.text(3.2, 6.85, '在 pos=0 处插入 200（从后往前移动）', ha='center',
        fontsize=15, fontweight='bold', color='#1a1a1a')

row(ax, 5.65, ['1', '2', '3', '4', '5', '', ''], label='初始')
ax.text(-2.1, 6.05, 'length=5', ha='left', va='center', fontsize=11,
        color='#c62828', family='monospace')
ax.text(-2.1, 5.65, '', ha='left', va='center', fontsize=11)

steps = [
    ('i=4', ['1', '2', '3', '4', '5', '5', ''], [4, 5]),
    ('i=3', ['1', '2', '3', '4', '4', '5', ''], [3, 4]),
    ('i=2', ['1', '2', '3', '3', '4', '5', ''], [2, 3]),
    ('i=1', ['1', '2', '2', '3', '4', '5', ''], [1, 2]),
    ('i=0', ['1', '1', '2', '3', '4', '5', ''], [0, 1]),
]
y = 4.35
for lab, vals, hl in steps:
    row(ax, y, vals, hl=hl, label=lab)
    y -= 0.92

# 插入结果
row(ax, y, ['', '1', '2', '3', '4', '5', ''], new=(0, '200'), label='写入')
ax.text(-2.1, y + 0.42, '200 落到 pos=0', ha='left', va='center',
        fontsize=11, color='#2e7d32')

plt.tight_layout()
plt.savefig(OUT + 'insert-move.png', dpi=150, bbox_inches='tight',
            facecolor='white')
plt.close()
print('OK insert-move.png')

# ============ 图3：删除元素的过程 ============
fig, ax = plt.subplots(figsize=(10, 4.6))
ax.set_xlim(-2.2, 8.6)
ax.set_ylim(-0.7, 5.2)
ax.axis('off')

ax.text(3.2, 4.9, '删除 pos=1 的元素 23（从前往后移动）', ha='center',
        fontsize=15, fontweight='bold', color='#1a1a1a')

row(ax, 3.75, ['12', '23', '45', '31', '56', '', ''], hl=[1],
    label='初始')
ax.text(-2.1, 4.17, '要删 23', ha='left', va='center', fontsize=11,
        color='#c62828')

row(ax, 2.55, ['12', '45', '31', '56', '', '', ''], hl=[1, 2],
    label='i=2')
ax.text(-2.1, 2.97, '45→左移', ha='left', va='center', fontsize=11,
        color='#555')

row(ax, 1.35, ['12', '45', '31', '56', '', '', ''], hl=[2, 3],
    label='i=3')
ax.text(-2.1, 1.77, '31→左移', ha='left', va='center', fontsize=11,
        color='#555')

row(ax, 0.15, ['12', '45', '31', '56', '', '', ''], hl=[3, 4],
    label='i=4')
ax.text(-2.1, 0.57, '56→左移', ha='left', va='center', fontsize=11,
        color='#555')

ax.text(3.2, -0.45, '结果：length=4，末尾空出一格', ha='center',
        fontsize=12, color='#2e7d32', fontweight='bold')

plt.tight_layout()
plt.savefig(OUT + 'delete-move.png', dpi=150, bbox_inches='tight',
            facecolor='white')
plt.close()
print('OK delete-move.png')
