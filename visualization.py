import json
import pandas as pd
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.globals import ThemeType, ChartType, SymbolType


class Visualization:
    jsonDir = 'preData/'
    htmlDir = 'pyHtml/'
    flag = 'boss'

    def create_html(self, chart, name):
        chart.render(self.htmlDir + name + '.html')

    # 平均薪资柱状图
    def salary_chart(self):
        with open(self.jsonDir + 'salary.json', 'r') as f:
            salary = json.load(f)
        x = [i['salaryMean'] for i in salary]
        y = [i['count'] for i in salary]
        c = (
            Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(x)
            .add_yaxis('数量', y)
            .set_global_opts(
                title_opts=opts.TitleOpts(title='python岗位平均薪资统计', subtitle='2025年'),

                # 隐藏 X 轴网格线
                xaxis_opts=opts.AxisOpts(
                    splitline_opts=opts.SplitLineOpts(is_show=False)
                ),

                # 隐藏 Y 轴网格线
                yaxis_opts=opts.AxisOpts(
                    splitline_opts=opts.SplitLineOpts(is_show=False)
                )
            )
        )
        return c, 'salary'

    # 学历饼图
    def degree_chart(self):
        data = [['本科', 264], ['专科', 36]]
        c = (
            Pie()
            .add(
                '',
                data
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="学历要求分布-" + self.flag)
            )
            .set_series_opts(
                label_opts=opts.LabelOpts(
                    formatter="{b} : {d}%"
                )
            )
        )
        return c, 'degree'

    # 经验饼图
    def experience_chart(self):
        df = pd.read_json(self.jsonDir + 'exp.json')
        x = df['jobExperience']
        y = df['count']
        data = list(zip(x, y))
        c = (
            Pie()
            .add(
                '',
                data
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="经验要求分布-" + self.flag)
            )
            .set_series_opts(
                label_opts=opts.LabelOpts(
                    formatter="{b} : {d}%"
                )
            )
        )
        return c, 'experience'

    # 地区地理图
    def district_chart(self):
        with open(self.jsonDir + 'district.json', 'r') as f:
            data = json.load(f)
        data = list(data.items())
        c = (
            Geo()
            .add_schema(
                maptype="上海",
                itemstyle_opts=opts.ItemStyleOpts(
                    area_color="#f5f5f5",  # 地图区域背景色
                    border_color="#404a59"  # 地图边框颜色
                ),
                # 鼠标悬浮高亮配置
                emphasis_itemstyle_opts=opts.ItemStyleOpts(
                    area_color="#78dc88",  # 悬浮时区域颜色
                    border_color="#ffffff"  # 悬浮时边框颜色
                )
            )
            .add(
                series_name="企业数量",  # 系列名称（图例显示）
                data_pair=data,  # 数据列表
                type_=ChartType.EFFECT_SCATTER,  # 涟漪散点类型
                symbol='circle',  # 散点形状（直接用字符串，兼容所有版本）
                symbol_size=12,  # 散点基础大小
            )
            # 4. 配置涟漪效果和标签
            .set_series_opts(
                effect_opts=opts.EffectOpts(
                    scale=6,  # 涟漪扩散最大比例
                    period=8,  # 涟漪动画周期（越小越快）
                    color="#ff6700"
                ),
                # 数值标签配置
                label_opts=opts.LabelOpts(
                    is_show=False,  # 显示数值标签
                    color="#333333",  # 标签颜色
                    font_size=10  # 标签字体大小
                )
            )
            .set_global_opts(
                # 标题配置
                title_opts=opts.TitleOpts(
                    title="上海各区企业数量分布",
                    subtitle="涟漪散点图",
                    title_textstyle_opts=opts.TextStyleOpts(font_size=20),
                    subtitle_textstyle_opts=opts.TextStyleOpts(font_size=14),
                ),
                # 视觉映射配置（数值→颜色渐变）
                visualmap_opts=opts.VisualMapOpts(
                    is_show=True,
                    type_="color",
                    min_=1,
                    max_=60,
                    range_color=["#ffffff", "#4dd0e1", "#0097a7"],  # 浅蓝→天蓝→深蓝
                ),
                # 图例配置
                legend_opts=opts.LegendOpts(
                    is_show=True,
                    textstyle_opts=opts.TextStyleOpts(font_size=12)
                )
            )
        )
        return c, 'district'

    # 位置柱状图
    def location_chart(self):
        df = pd.read_json(self.jsonDir + 'location.json', orient='columns')
        x = df['businessDistrict'].tolist()
        y = df['count'].tolist()
        c = (
            Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(x)
            .add_yaxis('数量', y)
            .set_global_opts(title_opts=opts.TitleOpts(title='位置数量', subtitle='2025年'))
        )
        return c, 'location'

    # 技能词云图
    def skill_chart(self):
        df = pd.read_json(self.jsonDir + 'skills.json', orient='columns')
        x = df['skills'].tolist()
        y = df['count'].tolist()
        words = list(zip(x, y))
        c = (
            WordCloud()
            .add("", words, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
            .set_global_opts(title_opts=opts.TitleOpts(title="技能词云图-diamond"))
        )
        return c, 'skill'

    # 福利词云图
    def welfare_chart(self):
        df = pd.read_json(self.jsonDir + 'welfare.json', orient='columns')
        x = df['welfareList'].tolist()
        y = df['count'].tolist()
        words = list(zip(x, y))
        c = (
            WordCloud()
            .add("", words, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
            .set_global_opts(title_opts=opts.TitleOpts(title="福利词云图-diamond"))
        )
        return c, 'welfare'

    # 组合1
    def dashboard(self):
        page = Page(layout=Page.DraggablePageLayout, page_title="招聘数据可视化大屏")
        c_salary = self.salary_chart()[0]
        c_degree = self.degree_chart()[0]
        c_experience = self.experience_chart()[0]
        c_district = self.district_chart()[0]
        c_location = self.location_chart()[0]
        c_skill = self.skill_chart()[0]
        c_welfare = self.welfare_chart()[0]
        page.add(
            c_salary,
            c_degree,
            c_experience,
            c_district,
            c_location,
            c_skill,
            c_welfare
        )
        output_file = self.htmlDir + 'dashboard.html'
        page.render(output_file)
        print(f"大屏报告已生成：{output_file}")

    # 组合2
    def tab_dashboard(self):
        tab = Tab()
        # 添加图表到选项卡，格式：tab.add(图表对象, "标签页名称")
        tab.add(self.salary_chart()[0], "薪资分布")
        tab.add(self.degree_chart()[0], "学历要求")
        tab.add(self.experience_chart()[0], "经验要求")
        tab.add(self.district_chart()[0], "地区分布")
        tab.add(self.location_chart()[0], "商圈统计")
        tab.add(self.skill_chart()[0], "技能热度")
        tab.add(self.welfare_chart()[0], "福利词云")

        output_file = 'boss直聘数据可视化.html'
        tab.render(output_file)
        print(f"选项卡报告已生成：{output_file}")


if __name__ == '__main__':
    v = Visualization()
    v.tab_dashboard()

    # v.create_html(*v.salary_chart())
    # v.create_html(*v.degree_chart())
    # v.create_html(*v.experience_chart())
    # v.create_html(*v.district_chart())
    # v.create_html(*v.location_chart())
    # v.create_html(*v.skill_chart())
    # v.create_html(*v.welfare_chart())
