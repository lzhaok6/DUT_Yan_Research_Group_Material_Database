# Contributing

## 修改原则

- 优先修改 `data/processed/simulation_parameters_long.csv`。
- 不要直接覆盖或删除已有来源信息。
- 如果同一参数有多个来源，新增一行，不要把旧值直接抹掉。
- 如果某个值存在争议，把 `review_status` 标为 `needs_review`。

## 建议状态

```text
imported_from_excel
needs_review
reviewed
deprecated
```

## 提交信息建议

```text
Add LNG vapor viscosity reference
Update UPE thermal conductivity source
Mark LNG density value for review
```

## Pull Request 内容建议

请简单写清楚：

- 改了哪个材料
- 改了哪个参数
- 数据来源是什么
- 是否需要别人复核

