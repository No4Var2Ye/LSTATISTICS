import yaml

import matplotlib.pyplot as plt

# 上下文管理 简化资源管理
# open 内置函数 用于打开文件
# as 对象赋值给 f

with open('plot_config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

plt.style.use(config.get('style', 'default'))
plt.rcParams.update(config.get('rc_params', {}))

fig, ax = plt.subplots(figsize=config.get('figure_size', (8, 6)))


for plot_config in config.get('plots', []):
    ax.plot(**plot_config)

ax.set(**config.get('axes_settings', {}))
plt.legend(**config.get('legend_settings', {}))

plt.savefig(config.get('output_file', 'output.png'))
plt.show()
