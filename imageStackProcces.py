import os
import subprocess
"""
通过此代码调用.in的配置文件进行mcgpu运行,以方便批量运行
"""
spectrum_list = ['spectrum100_Copper0.1mm']
thickness_list = range(400, 401, 50) # 模拟厚度范围
repeat_count = 1 # 单张重复次数
histories_per_run = 7e9 # 单次模拟的光子数
base_seed = 2342 # 随机数种子
file_remarks = 'mini_422_bone' # 文件名尾巴

# 模板文件读取
template_path = './MC-GPU_v1.5_lite_m_template.in'

# 读取模板文件内容
with open(template_path, 'r') as file:
    template_content = file.read()

for spectrum in spectrum_list:
    print(f"\n开始处理能谱：{spectrum}--\n")
    for thickness in thickness_list:
        for run in range(1, repeat_count + 1):
            seed = base_seed + run

            print(f"开始处理厚度：{thickness} mm | 第 {run} 次")

            # 替换模板中的占位符
            config_content = template_content.format(
                spectrum=spectrum,
                thickness=thickness,
                seed=seed,
                run=run,
                histories=histories_per_run* (thickness/100),
                fileRemarks=file_remarks
            )

            # 生成 .in 文件
            in_filename = f'config_{spectrum}_{thickness}mm_run{run}.in'
            with open(in_filename, 'w') as file:
                file.write(config_content)

            # 运行 MCGPU 单GPU
            command = f'MCGPULite1.5 {in_filename}'
            print(f'\n正在执行：{command}\n')
            try:
                subprocess.run(command, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f" 模拟失败：{e}")
