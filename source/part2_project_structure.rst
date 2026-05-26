项目资源管理目录创建
==========================

良好的项目组织结构是高效开发的基础，尤其对于 Godot 这类灵活的场景驱动引擎，本节提供了一份可参考复用的目录架构。

项目组织的核心原则
....................

Godot 采用基于场景（Scene）的工作流，每个场景都是包含节点、脚本和资源的自包含单元。资源应就近存放于使用它们的场景附近，而非全局集中管理。例如：

.. code-block:: text

   characters/
   └── player/
       ├── player.tscn          # 玩家场景
       ├── player.cs            # 玩家控制脚本
       └── textures/            # 专属纹理
           ├── idle.png
           └── run.png

**为何按场景分组优于按类型分组？**

当需要复用角色时，直接复制 ``entities/player`` 文件夹到新项目，所有依赖资源自动包含。若采用集中式纹理目录，则需手动收集分散资源极易遗漏。

在后续新建场景管理时也应该根据这个原则去管理你的项目的新场景和资源路径。

资源隔离与可见性控制
............................

有一些 Godot 不需要读取的文档文件夹，建议通过创建一个 ``.gdignore`` 文件阻止 Godot 导入特定目录，既加速初始导入，又避免无关资源污染文件系统面板：

.. code-block:: powershell

   # Windows 命令，在项目根目录下创建 .gdignore
   type nul > .gdignore

直接复制给 AI 的内容：

> 请按以下顺序操作：
> 1. 先在 Godot 中新建一个空项目（确保 .NET 已激活）
> 2. 在该项目中，参考以下目录结构创建文件夹框架（只创建文件夹，不需要实际代码和资源）
> 3. 之后再根据需求逐步编写脚本和创建场景
>
> 目录名和文件名遵循命名规范：

.. code-block:: text

   project.godot               # 项目配置文件（自动生成）

   addons/                     # 第三方插件资源

   assets/                     # 全局共享资源
   ├── fonts/                  # 字体文件
   ├── shaders/                # 全局着色器
   └── audio/                  # 音效与音乐

   scenes/                     # 游戏场景
   ├── ui/                     # UI界面
   │   ├── main_menu.tscn
   │   └── hud.cs
   └── levels/                 # 游戏关卡
       └── forest/             # 森林关卡资源组
           ├── level_forest.tscn
           └── trees/          # 专属树木模型

   entities/                   # 游戏实体
   ├── player/                 # 玩家角色（独立模块）
   │   ├── player.tscn
   │   ├── scripts/            # 专属脚本
   │   └── animations/         # 动画资源
   └── enemies/
       ├── goblin/             # 哥布林实例
       └── boss/               # BOSS实例

   systems/                    # 游戏系统
   ├── state_machines/         # 状态机实现
   │   ├── state.cs            # 状态基类
   │   └── state_machine.cs    # 状态管理器
   └── dialogue_system/        # 对话系统

命名规范：

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - 内容
     - 规范
     - 示例
   * - C# 脚本文件
     - PascalCase
     - ``PlayerController.cs``
   * - 场景文件 (.tscn)
     - PascalCase
     - ``MainMenu.tscn``
   * - 场景节点/组件
     - PascalCase
     - ``HitBox``、``AnimatedSprite2D``
   * - 普通资源文件
     - snake_case
     - ``enemy_idle.png``、``jump_sound.wav``
   * - 文件夹
     - snake_case
     - ``dialog_system``、``animations``
   * - 着色器 (.gdshader)
     - snake_case
     - ``outline_shader.gdshader``
   * - 信号/事件
     - snake_case + 过去式
     - ``health_changed``、``damage_taken``
   * - 枚举值
     - CONSTANT_CASE
     - ``EnemyType.GOBLIN_WARRIOR``
