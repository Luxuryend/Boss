from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType  # 移除 SymbolType 导入（无需再用）

# 原始数据
data = [
    ["浦东新区", 95],
    ["黄浦区", 40],
    ["徐汇区", 60],
    ["闵行区", 88],
    ["松江区", 75],
    ["长宁区", 85],
    ["静安区", 78],
    ["普陀区", 62],
    ["虹口区", 58],
    ["杨浦区", 63],
    ["宝山区", 55],
    ["嘉定区", 60],
    ["金山区", 45],
    ["青浦区", 68],
    ["奉贤区", 52],
    ["崇明区", 42]
]

# 1. 创建 Geo 地理图对象，设置基本配置
geo = (
    Geo(
        # 初始化配置：图表宽度/高度、页面标题
        init_opts=opts.InitOpts(page_title="上海各区数据涟漪散点图")
    )
    # 2. 设置地图类型为“上海”
    .add_schema(
        maptype="上海",
        # 地图样式配置
        itemstyle_opts=opts.ItemStyleOpts(
            border_color="#404a59",  # 地图边框颜色
            area_color="#f5f5f5",  # 地图区域背景色
        ),
        # 鼠标悬浮高亮配置
        emphasis_itemstyle_opts=opts.ItemStyleOpts(
            area_color="#5F6FFF",  # 悬浮时区域颜色
            border_color="#ffffff"  # 悬浮时边框颜色
        )
    )
    # 3. 添加涟漪散点数据（核心修正：symbol 用字符串 'circle'）
    .add(
        series_name="区域数值",  # 系列名称（图例显示）
        data_pair=data,  # 数据列表
        type_=ChartType.EFFECT_SCATTER,  # 涟漪散点类型
        symbol='circle',  # 散点形状（直接用字符串，兼容所有版本）
        symbol_size=12,  # 散点基础大小
    )
    # 4. 配置涟漪效果和标签
    .set_series_opts(
        # 涟漪效果配置
        effect_opts=opts.EffectOpts(
            scale=6,  # 涟漪扩散最大比例
            period=8,  # 涟漪动画周期（越小越快）
            color="#ff6700"  # 涟漪颜色（橙色）
        ),
        # 数值标签配置
        label_opts=opts.LabelOpts(
            is_show=False,  # 显示数值标签
            color="#333333",  # 标签颜色
            font_size=10  # 标签字体大小
        )
    )
    # 5. 全局配置
    .set_global_opts(
        # 标题配置
        title_opts=opts.TitleOpts(
            title="上海各区数据可视化",
            subtitle="涟漪散点图（数值越大，涟漪越明显）",
            title_textstyle_opts=opts.TextStyleOpts(font_size=20),
            subtitle_textstyle_opts=opts.TextStyleOpts(font_size=14),
        ),
        # 视觉映射配置（数值→颜色渐变）
        visualmap_opts=opts.VisualMapOpts(
            is_show=True,
            type_="color",
            min_=40,
            max_=95,
            range_color=["#e0f7fa", "#4dd0e1", "#0097a7"],  # 浅蓝→天蓝→深蓝
        ),
        # 图例配置
        legend_opts=opts.LegendOpts(
            is_show=True,
            textstyle_opts=opts.TextStyleOpts(font_size=12)
        )
    )
)

# 6. 渲染生成 HTML 文件
geo.render("上海各区涟漪散点地理图.html")
print("图表已生成！请打开「上海各区涟漪散点地理图.html」查看")
