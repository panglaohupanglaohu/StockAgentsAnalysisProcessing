# Investment simulation domain

本包将承载 `SimulationRun`、`RunConfigSnapshot`、`DecisionRecord`、`PortfolioState`、`OrderIntent`、成本/滑点和 checkpoint 元数据。

领域对象不暴露 TradingAgents 内部 graph state，并且所有输入必须带 `as_of` 决策时间。真实券商执行不属于当前范围。
