# 本项目的 AI 入口

本增补版发布仓库为 `monadgccg754678-ctrl/claude-setup-guide-windows-ipad`，后续本版更新只从此仓库下载。原教程基线来自 `ninedaywoo-web/claude-setup-guide` v1.0.20；以下主体沿用原版，新增第16章记录 Windows＋iPad 实操差异。公开版客户读取和下载不需要邀请码或申请权限，不进入原作者组织私有领取流程。

本增补版仓库为 monadgccg754678-ctrl/claude-setup-guide-windows-ipad；用户发本仓库链接开始或恢复带做时，先读 references/12-latest-start.md，实时下载并校验最新完整包；成功前不推荐 VPS、不复用本地旧 Skill 或更新缓存。成功后只从返回的新目录读取资料，显示版本并保留原进度。用户仅给本地文件夹时读取 SKILL.md 的日常规则。开始前必须完整阅读 references/01-network.md 和 references/02-browser-iphone.md，其余章节按阶段读。

维护项目时，Markdown 是正文源文件，图片使用仓库内相对路径。禁止加入在线文档依赖、原帖链接、用户私人 IP 或凭据。更新用户提供的文字时保留其表达，不大幅改写。

发布修改时同步 version.json 与 CHANGELOG.md，运行 python3 scripts/manifest.py，再运行 python3 -m unittest discover -s tests。更新只改课程和脚本；.local/ 是使用者的数据，不提交、不覆盖。

## 本地补充版约定
保留原版带做结构，同时阅读 SKILL.md 新增的本地补充说明。本仓库的 start/check/apply 只访问 monadgccg754678-ctrl/claude-setup-guide-windows-ipad，不能下载原上游覆盖本地增补。
Windows＋iPad 对照 references/16-windows-ipad-apple-practice.md；不要把本次案例成功当作全套网络已验收。
