"""
TMDB-TOP300 电影榜单数据统计案例
参考 07_practice.ipynb 中的完整工作，封装为函数形式
"""
import os

from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import pandas as pd

# 展示中文
plt.rcParams['font.sans-serif'] = ['SimHei']

# 数据文件路径（相对脚本所在目录，保证任意工作目录下均可运行）
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'movies.csv')
SAVE_PATH = os.path.join(BASE_DIR, 'data', 'TMDB-TOP300.png')


def load_data() -> pd.DataFrame:
    """加载电影数据并处理缺失值

    int64 : 整型数字（不支持空值）
    Int64 : 整型数字（支持空值）
    float64 : 浮点型数字（支持空值）
    """
    df = pd.read_csv(
        DATA_PATH,
        usecols=['电影名', '年份', '上映时间', '类型', '时长', '评分', '语言'],
        dtype={'年份': 'Int64'}
    )

    # 缺失值处理：年份为空时，取上映时间的前4位（即年份）进行填充
    df['年份'] = df['年份'].fillna(df['上映时间'].str[:4])

    return df


def draw_year_chart(axes: Axes, df: pd.DataFrame) -> None:
    """需求一：统计TOP300的电影中，每一年上映的电影数量的变化（折线图）"""
    # 分组统计
    year_count = df.groupby('年份')['年份'].count()

    # 组装数据
    # x轴数据
    min_year = year_count.index.min()
    max_year = year_count.index.max()
    x = [i for i in range(min_year, max_year + 1)]

    # y轴数据（得到key=i就填充value，否则填充0）
    y = [int(year_count.get(i, 0)) for i in x]

    # 绘制折线图
    axes.plot(x, y, color='g')
    axes.set_title('每年电影数量变化折线图')
    axes.set_xlabel('年份', fontsize=12)
    axes.set_ylabel('电影数量', fontsize=12)

    axes.set_xticks(x[::10])                          # 设置x轴刻度
    axes.set_yticks([i for i in range(0, 31, 3)])     # 设置y轴刻度
    axes.grid(linestyle='--', alpha=0.3)


def draw_language_chart(axes: Axes, df: pd.DataFrame) -> None:
    """需求二：统计对比不同语言的电影数量（柱状图）"""
    # 统计不同语言对应的电影数量
    language_count = df.groupby('语言')['语言'].count().sort_values(ascending=False)

    x_language = language_count.index.tolist()
    y_language_count = language_count.values.tolist()

    # 绘制柱状图
    axes.bar(x_language, y_language_count, color='g')
    axes.set_title('不同语言电影数量柱状图')
    axes.set_xlabel('语言', fontsize=12)
    axes.set_ylabel('数量', fontsize=12)

    axes.set_yticks([i for i in range(0, 181, 30)])   # 设置y轴刻度
    axes.grid(linestyle='--', alpha=0.3)              # 添加网格
    axes.tick_params(axis='x', rotation=90)           # x轴标签旋转90度


def draw_type_chart(axes: Axes, df: pd.DataFrame) -> None:
    """需求三：统计对比不同类型电影数量（柱状图）"""
    # 统计不同类型电影数量（一部电影可能包含多个类型，需要拆分逐一计数）
    type_count = {}
    for types in df['类型'].str.split(","):
        for type in types:
            if type in type_count:
                type_count[type] += 1
            else:
                type_count[type] = 1

    x = list(type_count.keys())
    y = list(type_count.values())

    # 绘制柱状图
    axes.bar(x, y, color='g')
    axes.set_title('不同类型的数量')
    axes.set_xlabel('类型', fontsize=12)
    axes.set_ylabel('电影数量', fontsize=12)

    axes.set_yticks([i for i in range(0, 201, 25)])
    axes.grid(linestyle='--', alpha=0.3)


def draw_score_chart(axes: Axes, df: pd.DataFrame) -> None:
    """需求四：统计对比各个评分的电影占比（饼状图）"""
    # 统计各个评分的数量
    score_count = df.groupby('评分')['评分'].count().sort_values(ascending=False)

    # 合并小数据（比例小于6%）--> 其他
    total = score_count.sum()
    large_scores = score_count.loc[score_count >= total * 0.06]  # 大数据，比例大于6%
    small_scores = score_count.loc[score_count < total * 0.06]   # 小数据，比例小于6%
    if small_scores.shape[0] > 0:
        large_scores['其他'] = small_scores.sum()

    scores = large_scores.index.tolist()
    scores_values = large_scores.values.tolist()

    # 绘制饼状图（startangle为起始角度）
    axes.pie(scores_values, labels=scores, autopct='%1.1f%%', startangle=90, radius=1.2)
    axes.set_title('不同评分电影占比饼状图', fontsize=12, y=1.1)
    axes.legend(loc='lower center', ncol=4, bbox_to_anchor=(0.5, -0.2))


def main() -> None:
    """主流程：创建画布 -> 加载数据 -> 绘制四个子图 -> 保存并展示"""
    # 创建子图（解包操作）
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 12), dpi=100)
    # 添加画布标签 - x=0.5 : x轴位置, y=0.93 : y轴位置
    fig.suptitle('TMDB-TOP300电影榜单数据统计', fontsize=23, x=0.5, y=0.95)
    fig.subplots_adjust(hspace=0.8, wspace=0.3)

    # 获取子图
    axes1: Axes = axes[0, 0]  # 第一个子图
    axes2: Axes = axes[0, 1]  # 第二个子图
    axes3: Axes = axes[1, 0]  # 第三个子图
    axes4: Axes = axes[1, 1]  # 第四个子图

    # 加载数据
    df = load_data()

    # 依次绘制四个子图
    draw_year_chart(axes1, df)       # 需求一：每年电影数量折线图
    draw_language_chart(axes2, df)   # 需求二：不同语言数量柱状图
    draw_type_chart(axes3, df)       # 需求三：不同类型数量柱状图
    draw_score_chart(axes4, df)      # 需求四：不同评分占比饼状图

    # 保存图片
    plt.savefig(SAVE_PATH)

    plt.show()  # 展示画布


if __name__ == '__main__':
    main()
