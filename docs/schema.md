# Data Schema

主要数据文件：

```text
data/processed/simulation_parameters_long.csv
```

## 字段说明

| 字段 | 含义 | 示例 |
| --- | --- | --- |
| `material` | 材料或流体名称 | `LNG` |
| `property` | 参数名称，建议包含英文、单位和必要条件 | `密度 density (kg/m^3)` |
| `value_and_source` | 参数值、单位、温度/压力条件、文献或网页来源 | `414 (...)` |
| `review_status` | 审核状态 | `imported_from_excel` |

## 录入建议

- 数值、单位、温度条件尽量写在同一个单元格里，避免以后不知道适用范围。
- 来源优先写 DOI、论文、标准、手册；网页链接可以作为临时来源。
- 如果来源只是搜索结果页，建议后续替换为更稳定的来源。
- 同一个材料同一个参数如果有多个不同来源，保留多行，并在 `value_and_source` 中说明条件差异。

