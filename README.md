# EisenTodo 项目要求

EisenTodo 是一个基于艾森豪威尔矩阵的待办事项管理工具，旨在帮助用户更有效地管理任务的优先级。核心功能如下：

1. **借鉴艾森豪威尔矩阵来处理 todo list 的优先级**：将任务分为四个象限（紧急重要、紧急不重要、重要不紧急、不紧急不重要）。
  
2. **借鉴卡牌的美观在电脑屏幕上呈现 4 个卡牌**：在屏幕上以卡牌形式呈现四个象限的任务（紧急重要、紧急不重要、重要不紧急、不紧急不重要）。（**卡牌暂未实现**）
  
3. **可增删改查具体的 todo 任务和子任务**：提供添加、删除、编辑和查看任务及子任务的功能。 

## TODO 四个字母的英文单字理解

### 重要且紧急（Urgent - Important）

* **Triumph（胜利；战胜）**：这个单词体现了面对这类关键且紧急的任务时，需要以取得胜利的决心去处理。例如，在应对突发的公共卫生事件时，医疗团队和政府部门必须“triumph” over（战胜）困难，迅速调配资源、控制疫情，这是关乎生命安全和社会稳定的重要且紧急事务。

### 重要不紧急（Important - Not Urgent）

* **Objective（目标；目的）**：代表着对于长期发展至关重要，但不需要立即完成的事务。比如个人的职业发展“objective”，像计划在未来几年内获得某个专业认证或者晋升到特定职位，这是重要的长期规划，虽然不紧急，但对个人职业成长有深远意义。

### 紧急不重要（Urgent - Not Important）

* **Delegate（委托；委派）**：当遇到紧急但对核心事务不重要的事情时，“delegate”这个策略很实用。例如，在忙碌的工作中接到一个紧急的会议邀请，但会议内容和自己主要工作无关，就可以“delegate”（委派）同事去参加，自己专注于重要事务。

### 不重要不紧急（Not Important - Not Urgent）

* **Overlook（忽视；忽略）**：用于表示对于这类既不重要也不紧急的事情，应该有意识地不去关注。比如一些无意义的闲聊或者低价值的娱乐活动，为了更高效地利用时间和精力，我们可以“overlook”（忽视）它们，将精力集中在更有价值的事务上。

## 代码实现思路

本项目利用人工智能工具（豆包和 GitHub Copilot）来辅助开发，旨在帮助用户更有效地管理任务优先级。由于开发者几乎完全不会编程，因此采用了以下方法来设计和优化代码的功能模块和架构，以方便能够简单审核 AI 生成的代码：

1. **第一性原理**：从最基本的原理出发，简化问题，确保每个功能模块都围绕艾森豪威尔矩阵和 ToDo List 的核心需求进行设计。
  
2. **极简主义**：聚焦于核心功能，去除不必要的复杂性，确保代码简洁明了，提升用户体验。
  
3. **单用户单设备**：设计适用于单用户单设备的场景，确保应用在这种环境下的高效运行。
  
4. **采用 CSV 文件**：将任务信息写入 CSV 文件，方便本地存放和备份，以及跨设备导入。
  
5. **用户体验**：注重用户界面的美观和操作的便捷性，借鉴卡牌的美观在电脑屏幕上呈现 4 个卡牌（紧急重要、紧急不重要、重要不紧急、不紧急不重要）。
  
本项目使用 Python 的 Kivy 框架实现，确保跨平台的兼容性和良好的用户界面体验。

## 代码文件的功能描述

以下是 EisenTodo 中的 Python 文件的功能说明：

1. **task_model.py**

   - 功能说明：

     - 主要用于定义任务的数据模型，即 Task 类。

     - 通过属性限定和构造方法，确保任务对象各个属性（如任务名称、描述、进度、类别等）的合法性与完整性。

     - 提供将任务对象转换为字典形式的方法（to_dict）和从字典数据创建任务对象的方法（from_dict），用于数据持久化和恢复。

2. **task_persistence.py**

   - 功能说明：

     - 处理任务数据与外部存储（如 CSV 文件）之间的持久化交互。

     - 封装方法如 save_tasks（保存任务列表到 CSV 文件）、load_tasks（从 CSV 文件加载任务数据）、import_tasks（从外部 CSV 文件导入任务数据）、export_tasks（导出任务数据到 CSV 文件）。

     - 进行细致的错误处理，确保任务数据在存储和读取过程中的稳定性、准确性和完整性。

3. **task_logic.py**

   - 功能说明：

     - 作为业务逻辑核心模块，衔接任务数据模型与持久化操作。

     - 提供任务管理相关的业务逻辑，如 add_task（添加任务）、edit_task（编辑任务）、delete_task（删除任务）、get_tasks_by_category（按类别获取任务）、filter_tasks（筛选任务）、sort_tasks（排序任务）。

     - 处理各种边界情况和异常，保证业务逻辑的健壮性。

4. **main.py**

   - 功能说明：

     - 作为 Kivy 应用的入口，负责构建用户界面，管理不同的屏幕展示（通过 ScreenManager 实现多屏幕架构）。

     - 集成任务管理功能到界面操作中（如通过弹窗实现添加、编辑、删除等操作）。

     - 处理界面元素的色彩主题应用、动画效果展示和提示信息显示，保障用户的流畅体验。

5. **input_validation.py**

   - 功能说明：

     - 集中处理各种用户输入的验证逻辑。

     - 包含验证函数如 validate_task_name（验证任务名称）、validate_task_progress（验证任务进度）、validate_task_category（验证任务类别）。

     - 确保输入数据的合法性，提升应用的用户输入数据把控能力。

6. **animation_effects.py**

   - 功能说明：

     - 封装界面动画效果相关的逻辑代码。

     - 提供动画效果函数如 show_success_animation（操作成功提示动画）、show_error_animation（操作失败提示动画）、task_list_item_animation（任务列表项动画）。

     - 统一管理动画效果代码，方便在不同需要动画展示的地方复用。

7. **file_path_utils.py**

   - 功能说明：

     - 处理文件路径相关的通用操作。

     - 包含函数如 validate_file_path（检查文件路径合法性和权限）、create_directory_for_path（为文件路径创建目录）。

     - 集中规范文件路径相关操作，减少其他模块中的耦合代码，增强代码的可维护性和通用性。

8. **popup_handlers.py**

   - 功能说明：

     - 处理各种弹窗的显示和逻辑。

     - 包含函数如 show_add_task_popup（显示添加任务弹窗）、show_edit_task_popup（显示编辑任务弹窗）、show_delete_task_popup（显示删除任务弹窗）、show_tasks_by_category_popup（显示按类别查看任务弹窗）、show_filter_tasks_popup（显示筛选任务弹窗）、show_sort_tasks_popup（显示排序任务弹窗）、show_backup_tasks_popup（显示备份任务数据弹窗）、show_restore_tasks_popup（显示恢复任务数据弹窗）。

     - 通过弹窗与用户交互，实现任务的增删改查功能。

9. **popup_utils.py**

   - 功能说明：

     - 提供创建通用的输入框和按钮的函数。

     - 包含函数如 create_text_input（创建带有提示文本和输入过滤器的输入框）、create_button（创建带有文本和回调函数的按钮）。

     - 方便在弹窗中复用输入框和按钮的创建逻辑。

10. **utils.py**

    - 功能说明：

      - 提供配置和实用函数。

      - 包含全局颜色主题字典 COLOR_THEME、配置文件路径 CONFIG_PATH、函数如 apply_color_theme（应用颜色主题）、save_last_path（保存最后使用的路径）、show_success_message（显示操作成功提示）、show_error_message（显示操作失败提示）。

      - 统一管理配置和实用函数，方便在不同模块中复用。

通过这样的代码文件拆分，各个模块各司其职，功能更加明确独立，代码整体的结构更加清晰，也更易于后续的维护、扩展以及团队协作开发等工作的开展。

## 编译运行 EisenTodo 应用的方法

以下是在 VS Code 中组织和编译运行 EisenTodo 应用的一般步骤和相关建议：

### 1. 项目文件夹结构创建

在本地磁盘上创建一个专门的项目文件夹，比如命名为 `EisenTodo`。然后将以下 10 个 Python 文件（`task_model.py`、`task_persistence.py`、`task_logic.py`、`main.py`、`input_validation.py`、`animation_effects.py`、`file_path_utils.py`、`popup_handlers.py`、`popup_utils.py`、`utils.py`）都放到这个项目文件夹内。

### 2. 虚拟环境搭建（可选但推荐）

* **安装 `virtualenv`（如果尚未安装）**：

在 VS Code 的集成终端中执行如下命令（如果已安装可跳过）：

    pip install virtualenv

* **创建虚拟环境**：在项目文件夹的根目录下，执行以下命令创建虚拟环境（以创建名为 venv 的虚拟环境为例）：

    virtualenv venv

* **激活虚拟环境**：

    - **Windows**： 在终端中执行：

    .\venv\Scripts\activate

    - **Linux**：在终端中执行： 

    source venv/bin/activate

      - **macOS**：在终端中执行： 

    source venv/bin/activate

激活虚拟环境后，命令行提示符前面会显示虚拟环境名称，如 (venv) 开头，表示当前处于虚拟环境内。

### 3. 安装项目依赖

根据代码实际使用的第三方库，在激活虚拟环境后的终端中使用 `pip` 安装对应的依赖包。例如，如果使用了 `kivy`，执行：

    pip install kivy

### 4.VS Code 设置

* **Python 解释器**：打开 VS Code 后，按下 Ctrl + Shift + P（Windows、Linux）或者 Command + Shift + P（Mac）组合键，在弹出的命令面板中输入 “Python: Select Interpreter”，然后选择刚才激活的虚拟环境对应的 Python 解释器。
  
* **运行配置**：
  

    - 点击 VS Code 左侧的 “运行和调试” 图标，然后点击 “创建 `launch.json` 文件”，选择 “Python” 环境。

    - 在生成的 `launch.json` 文件中，配置启动项。假设要运行 `main.py` 作为主程序启动应用，可以配置如下内容：

    {
    
        "version": "1.0.0",
    
        "configurations": [
    
            {
    
                "name": "Python: Main",
    
                "type": "python",
    
                "request": "launch",
    
                "program": "${workspaceFolder}/main.py",
    
                "console": "integratedTerminal"
    
            }
    
        ]
    
    }

### 5. 编译跨平台应用

#### 桌面应用（以 `kivy` 为例）

* **安装 `kivy` 的相关构建工具**：例如，对于 Windows，需要安装 Visual C++ Build Tools；对于 Linux，可能需要安装对应系统的开发包；对于 Mac，一般需要安装 Xcode 命令行工具。
  
* **使用构建工具打包应用**：可以使用 `pyinstaller` 作为打包工具。需要先安装 `pyinstaller`：
  

    pip install pyinstaller

然后在项目根目录下的终端中执行以下命令（以生成 Windows 可执行文件为例）：

    pyinstaller --name EisenTodo --onefile main.py

上述命令会将应用打包成一个名为 EisenTodo.exe（Windows 下）的可执行文件，放在 dist 文件夹内。

#### 移动应用（以 kivy 为例且主要针对 Android）

* **安装 Android 开发相关工具和依赖**： 需要安装 Java Development Kit（JDK）、Android SDK 以及 `buildozer`（通过 `pip install buildozer` 安装）。
  
* **配置 `buildozer`**： 在项目根目录下创建一个名为 `buildozer.spec` 的配置文件，例如：
  

    [app]
    
    
    # 应用名称
    
    title = EisenTodo
    
    # 应用包名
    
    package.name = eisentodo
    
    # 应用版本
    
    package.version = 0.1
    
    # 应用的入口 Python 文件
    
    source.dir = .
    
    source.include_exts = py,png,jpg,kv,atlas
    
    requirements = kivy
    
    
    [buildozer]
    
    
    # Android 相关配置
    
    android.sdk = <YOUR_ANDROID_SDK_PATH>
    
    android.ndk = <YOUR_ANDROID_NDK_PATH>
    
    android.api = 33
    
    android.minapi = 21
    
    
    # 构建输出目录
    
    bin = $HOME/.buildozer/android/app

将 <YOUR_ANDROID_SDK_PATH> 和 <YOUR_ANDROID_NDK_PATH> 替换为实际安装的路径。

* **使用 `buildozer` 打包应用**： 在项目根目录下的终端中执行：

    buildozer android debug

这个命令会下载所需的 Android 相关依赖、编译代码并最终生成一个 `.apk` 文件，放在 `bin` 目录指定的路径下。

通过上述步骤，可以在 VS Code 中组织好代码、配置好开发环境，然后依据不同平台的特性使用对应的工具去尝试编译和打包跨平台应用。
