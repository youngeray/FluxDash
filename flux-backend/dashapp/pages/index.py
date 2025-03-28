import dash
from dash import html,dcc,callback,Input,Output
import feffery_antd_components as fac
import feffery_antd_charts as fact
import random


dash.register_page(__name__)

def dash_card(description,direciton='vertical',size='small'):
    return fac.AntdCard(
        fac.AntdSpace(
            description,
            direction=direciton,
            size = size,
        ),
        headStyle={'display': 'none'}, 
    )


layout = fac.AntdSpace(
    [
        fac.AntdRow([
            fac.AntdCol(
                dash_card(
                    [
                        fac.AntdStatistic(title='总销售额', value=126560),
                        fact.AntdTinyLine(
                            data=[random.randint(20, 70) for _ in range(18)],
                            height=40,width=200,smooth=True
                        ),
                        fac.AntdText('日销售额 12,423', type='secondary')
                    ]),
                flex = '1'  
            ),
            fac.AntdCol(
                dash_card(
                    [
                        fac.AntdStatistic(title='访问量', value=8846),
                        fact.AntdTinyArea(
                            data=[random.randint(20, 70) for _ in range(18)],
                            height=40,width=200,smooth=True,areaStyle={'fill':'#6c35de'}
                        ),
                        fac.AntdText('日访问量 1,234', type='secondary')

                    ]),
                flex = '1'  
            ),
            fac.AntdCol(
                dash_card(
                    [
                        fac.AntdStatistic(title='支付笔数', value=6560),
                        fact.AntdTinyColumn(
                            data=[random.randint(20, 70) for _ in range(18)],
                            height=40,
                            width=200,
                        ),
                        fac.AntdText('转化率 60%', type='secondary')

                    ]),
                flex = '1'
            ),
            fac.AntdCol(
                dash_card(
                    [fac.AntdStatistic(title='运营活动效果', value='78%'),
                    fact.AntdProgress(
                        height=40,width=200,percent=0.78, color=['#25b1bf', '#E8EDF3']
                    ),
                    fac.AntdRow([fac.AntdText('周同比 12%', type='secondary'),fac.AntdIcon(icon='antd-rise', style={'color': 'red'}),fac.AntdDivider(direction='vertical'),fac.AntdText('日同比 8%', type='secondary'),fac.AntdIcon(icon='antd-fall', style={'color': 'green'})])
                ]),
                flex = '1'
            ),
            
        ],gutter=16),
        fac.AntdRow([
            fac.AntdCol(
                dash_card(
                    fac.AntdTabs(
                       items = [
                        {
                           'key':'1',
                           'label':'销售额',
                           'children':fac.AntdRow(
                              [
                                fac.AntdCol([
                                    fac.AntdText(''),
                                    fact.AntdColumn(
                                        data=[
                                            {
                                            '日期' :f'2025-0{i}',
                                            '销售额' :random.randint(50, 100),
                                            '类型' :f'类型{j}'
                                            } for i in range(1,10) for j in range(1,4)
                                        ],
                                        yAxis={'title': {'text': ''}},
                                        xField='日期',
                                        yField='销售额',
                                        seriesField='类型',
                                        isStack=False,
                                        color = [],
                                        label={},
                                        width=800,
                                        height=300,
                                    ),],
                                    flex = '3'
                              ),
                                fac.AntdCol([
                                    fac.AntdText('门店销售额排名',strong=True),
                                    fac.AntdTable(
                                       columns=[{'title':'排名','dataIndex':'排名','width':100},{'title':'门店','dataIndex':'门店','width':200},{'title':'销售额','dataIndex':'销售额','width':200}],
                                       data=[{'排名':i,'门店':f'工专路{i}号店','销售额':random.randint(500, 10000)} for i in range(1,7)],
                                       pagination=False,
                                       showHeader=False,
                                       

                                    ),
                                    ], 
                                    flex = '2',                                  
                                ),

                            ],
                            gutter=20,
                            justify='space-between' 
                           )
                        },

                       ] 
                    )
                ),
                flex = '4'
            ),
        ],gutter=10),
        fac.AntdRow([
           fac.AntdCol(
                dash_card(
                    [ 
                        fact.AntdLiquid(
                            percent=0.75,
                            outline={
                                'border': 4,
                                'distance': 8,
                            },
                            wave={
                                'length': 128,
                            },height=160,width=160
                        ),
                        fac.AntdText('销售额 126,560', type='secondary')
                    ],
                    direciton='horizontal',
                    size='large'
                    ),
                flex = '1' 
           ),
           fac.AntdCol(
                dash_card(
                    [ 
                        fact.AntdRose(
                            data=[
                                {
                                    'class': f'门店{i}',
                                    'value': random.randint(50, 100),
                                }
                                for i in range(1, 7)
                            ],
                            xField='class',
                            yField='value',
                            seriesField='class',
                            radius=0.9,
                            innerRadius=0.4,
                            height=160,
                            label={'offset': -15},
                        )

                    ]
                    ),
                flex = '1' 
           ),
           fac.AntdCol(
                dash_card(
                    [
                        
                        fact.AntdFunnel(
                            data=[
                                {
                                    'stage': '商机数量',
                                    'number': 253,
                                },
                                {
                                    'stage': '回访数量',
                                    'number': 151,
                                },
                                {
                                    'stage': '签单数量',
                                    'number': 113,
                                },
                                {
                                    'stage': '回款数量',
                                    'number': 87,
                                },
                            ],
                            xField='stage',
                            yField='number',
                            legend=False,
                            height=160,
                        ),

                    ]
                    ),
                flex = '1'
           ), 
        ],gutter=16)
    ],
    direction='vertical',
    style = {'width':'90%','margin':20},

)

