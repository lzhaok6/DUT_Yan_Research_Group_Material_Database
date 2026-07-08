# LNG Simulation Parameters

这个仓库用于团队共享和版本管理 LNG 低温设备仿真参数。

第一版保持简单：以 CSV 作为主要数据格式，让 GitHub 可以清楚显示每次修改了哪一行；原始 Excel 文件保存在 `source/` 中作为来源备份。

## 文件结构

```text
data/
  raw/
    simulation_parameters_matrix.csv      # 从 Excel 直接导出的原始矩阵表
  processed/
    simulation_parameters_long.csv        # 推荐维护的长表格式
docs/
  schema.md                               # 字段说明和更新规则
scripts/
  validate_csv.py                         # 简单数据检查
source/
  Simulation_parameters.xlsx              # 原始 Excel 文件备份
```

## 推荐维护方式

日常更新优先修改：

```text
data/processed/simulation_parameters_long.csv
```

每一行代表一个材料的一项参数：

```text
material,property,value_and_source,review_status
```

这样做的好处是：成员修改参数时，GitHub 可以逐行显示修改记录，方便审核和回退。

## 更新流程

1. 新建分支，不直接改 `main`。
2. 修改或新增 CSV 行。
3. 在 `value_and_source` 中保留数值、单位、温度/压力条件和来源。
4. 运行检查脚本：

```bash
python scripts/validate_csv.py
```

5. 提交 Pull Request，由至少一位成员审核后合并。

## 当前数据来源

初始数据来自：

```text
source/Simulation_parameters.xlsx
```

